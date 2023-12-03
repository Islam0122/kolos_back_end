from django.db import transaction
from ..models import Invoice, InvoiceItems, ReturnInvoice, ReturnInvoiceItems
from .serializers import InvoiceSerializer, InvoiceItemsSerializer, ReturnInvoiceSerializer,\
    ReturnInvoiceItemsSerializer
from rest_framework import generics
from rest_framework import viewsets, status
from rest_framework.response import Response


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
                    defaults=return_product_data
                )
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

#список купленных товаров передаваемого ДИСТ
class DistributorInvoiceItemsView(generics.ListAPIView):
    serializer_class = InvoiceItemsSerializer

    def get_queryset(self):
        distributor_id = self.kwargs['distributor_id']

        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)

        queryset = InvoiceItems.objects.filter(invoice__distributor__id=distributor_id, quantity__gt=0)

        if start_date and end_date:
            queryset = queryset.filter(invoice__sale_date__range=[start_date, end_date])

        return queryset


#список возвращенных товаров передаваемого ДИСТ

class ReturnInvoiceListByDistributor(generics.ListAPIView):
    serializer_class = ReturnInvoiceItemsSerializer

    def get_queryset(self):
        distributor_id = self.kwargs['distributor_id']
        queryset = ReturnInvoiceItems.objects.filter(return_invoice__distributor__id=distributor_id)
        return queryset

