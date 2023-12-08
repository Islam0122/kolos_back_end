from django.db import transaction
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView

from ..models import Invoice, InvoiceItems, ReturnInvoice, ReturnInvoiceItems
from .serializers import InvoiceSerializer, InvoiceItemsSerializer, ReturnInvoiceSerializer,\
    ReturnInvoiceItemsSerializer, SearchSerSeles, ClueSearchSerializer
from rest_framework import generics
from rest_framework import viewsets, status
from rest_framework.response import Response

from distributor.models import Distributor

from product.models import ProductNormal


class InvoiceItemsViewSet(generics.ListCreateAPIView):
    queryset = InvoiceItems.objects.all()
    serializer_class = InvoiceItemsSerializer


class InvoiceItemsViewSetDet(generics.RetrieveUpdateDestroyAPIView):
    queryset = InvoiceItems.objects.all()
    serializer_class = InvoiceItemsSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        products = InvoiceItems.objects.filter(invoice=instance)
        products_serializer = InvoiceItemsSerializer(products, many=True)
        response_data = serializer.data
        response_data['products_invoice'] = products_serializer.data
        return Response(response_data)

    def create(self, request, *args, **kwargs):
        products_invoice_data = request.data.pop('products_invoice', None)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = serializer.save()
        if products_invoice_data:
            for product_data in products_invoice_data:
                InvoiceItems.objects.create(invoice=instance, **product_data)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ReturnInvoiceViewSet(viewsets.ModelViewSet):
    queryset = ReturnInvoice.objects.all()
    serializer_class = ReturnInvoiceSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        products = ReturnInvoiceItems.objects.filter(return_invoice=instance)
        products_serializer = ReturnInvoiceItemsSerializer(products, many=True)
        response_data = serializer.data
        response_data['products_return_invoice'] = products_serializer.data
        return Response(response_data)

    def create(self, request, *args, **kwargs):
        return_invoice_items_data = request.data.pop('return_product', None)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        with transaction.atomic():
            for return_product_data in return_invoice_items_data or []:
                return_item, created = ReturnInvoiceItems.objects.update_or_create(
                    return_invoice=instance,
                    invoice_item_id=return_product_data['invoice_item_id'],
                    defaults={'quantity': return_product_data['quantity'], 'state': return_product_data['state']}
                )
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

#список купленных товаров передаваемого ДИСТ
class DistributorInvoiceItemsView(generics.ListAPIView):
    serializer_class = InvoiceItemsSerializer

    def get_queryset(self):
        distributor_id = self.kwargs.get('distributor_id')  # Или откуда у вас берется distributor_id

        distributor = get_object_or_404(Distributor, id=distributor_id)

        queryset = InvoiceItems.objects.filter(invoice__distributor=distributor, quantity__gt=0).order_by('-id')

        # Фильтрация по комбинированным полям без учета регистра и акцентов (для PostgreSQL)
        search_query = self.request.query_params.get('search_query', None)
        if search_query:
            queryset = queryset.filter(
                Q(product__name__iregex=fr'.*{search_query}.*') |
                Q(product__identification_number__iregex=fr'.*{search_query}.*')
            )

        category_filter = self.request.query_params.get('category', None)
        if category_filter:
            queryset = queryset.filter(product__category__title__iexact=category_filter)

        # Фильтрация по дате
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)

        # if start_date and end_date:
        #     # Если указаны обе даты, ищем в интервале между ними
        #     queryset = queryset.filter(invoice__sale_date__range=[start_date, end_date])
        #
        # elif end_date:
        #     # Если указана только начальная дата, ищем по ней
        #     queryset = queryset.filter(invoice__sale_date__lte=end_date)
        #
        # return queryset

        if start_date and end_date:
            # Если указаны обе даты, ищем в интервале между ними
            queryset = queryset.filter(invoice__sale_date__range=[start_date, end_date])
        elif start_date:
            # Если указана только начальная дата, ищем по ней
            queryset = queryset.filter(invoice__sale_date__gte=start_date)

        elif end_date:
            # Если указана только начальная дата, ищем по ней
            queryset = queryset.filter(invoice__sale_date__lte=end_date)

        return queryset


#список возвращенных товаров передаваемого ДИСТ

class ReturnInvoiceListByDistributor(generics.ListAPIView):
    serializer_class = ReturnInvoiceItemsSerializer

    def get_queryset(self):
        distributor_id = self.kwargs.get('distributor_id')  # Или откуда у вас берется distributor_id

        queryset = ReturnInvoiceItems.objects.filter(return_invoice__distributor__id=distributor_id).order_by('-id')


        # Фильтрация по комбинированным полям без учета регистра и акцентов (для PostgreSQL)
        search_query = self.request.query_params.get('search_query', None)
        if search_query:
            queryset = queryset.filter(
                Q(invoice_item__product__name__iregex=fr'.*{search_query}.*') |
                Q(invoice_item__product__identification_number__iregex=fr'.*{search_query}.*')
            )

        category_filter = self.request.query_params.get('category', None)
        if category_filter:
            queryset = queryset.filter(invoice_item__product__category__title__iexact=category_filter)

        # Фильтрация по дате
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)

        if start_date and end_date:
            # Если указаны обе даты, ищем в интервале между ними
            queryset = queryset.filter(return_invoice__return_date__range=[start_date, end_date])
        elif start_date:
            # Если указана только начальная дата, ищем по ней
            queryset = queryset.filter(return_invoice__return_date__gte=start_date)

        elif end_date:
            # Если указана только начальная дата, ищем по ней
            queryset = queryset.filter(return_invoice__return_date__lte=end_date)

        return queryset


class SearchSold(generics.ListAPIView):
    serializer_class = SearchSerSeles

    def get_queryset(self):
        distributor_id = self.kwargs.get('distributor_id')  # Или откуда у вас берется distributor_id

        distributor = get_object_or_404(Distributor, id=distributor_id)

        queryset = InvoiceItems.objects.filter(invoice__distributor=distributor, quantity__gt=0)

        # Фильтрация по комбинированным полям без учета регистра и акцентов (для PostgreSQL)
        search_query = self.request.query_params.get('search_query', None)
        if search_query:
            queryset = queryset.filter(
                Q(product__name__iregex=fr'.*{search_query}.*') |
                Q(product__identification_number__iregex=fr'.*{search_query}.*')
            )

        category_filter = self.request.query_params.get('category', None)
        if category_filter:
            queryset = queryset.filter(product__category__title__iexact=category_filter)


        # return queryset
        print(queryset)
        # Получаем уникальные имена и категории
        unique_names_and_categories = queryset.values_list('product__name', 'product__category').distinct()
        print(unique_names_and_categories)

        # Создаем список словарей с уникальными именами и категориями
        result_data = [{'name': name, 'category': category} for name, category in unique_names_and_categories]
        #
        serializer = SearchSerSeles(result_data, many=True)
        # breakpoint()
        return serializer.data

class SearchReturned(generics.ListAPIView):
    serializer_class = ClueSearchSerializer

    def get_queryset(self):
        distributor_id = self.kwargs.get('distributor_id')  # Или откуда у вас берется distributor_id

        queryset = ReturnInvoiceItems.objects.filter(return_invoice__distributor__id=distributor_id)


        # Фильтрация по комбинированным полям без учета регистра и акцентов (для PostgreSQL)
        search_query = self.request.query_params.get('search_query', None)
        if search_query:
            queryset = queryset.filter(
                Q(invoice_item__product__name__iregex=fr'.*{search_query}.*') |
                Q(invoice_item__product__identification_number__iregex=fr'.*{search_query}.*')
            )

        category_filter = self.request.query_params.get('category', None)
        if category_filter:
            queryset = queryset.filter(invoice_item__product__category__title__iexact=category_filter)

        # Фильтрация по дате
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)

        if start_date and end_date:
            # Если указаны обе даты, ищем в интервале между ними
            queryset = queryset.filter(return_invoice__return_date__range=[start_date, end_date])
        elif start_date:
            # Если указана только начальная дата, ищем по ней
            queryset = queryset.filter(return_invoice__return_date__gte=start_date)

        elif end_date:
            # Если указана только начальная дата, ищем по ней
            queryset = queryset.filter(return_invoice__return_date__lte=end_date)

        return queryset
