from django.db.models import Q
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from product import models as product_models
from product.api import serializers as product_ser
from product.models import ProductNormal
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from product.choices import State


class ChangeStateAndMoveView(APIView):


    def post(self, request, product_id, *args, **kwargs):
        product = get_object_or_404(ProductNormal, id=product_id)
        print(product)
        new_state = request.data.get("new_state")
        print(new_state)

        if new_state in [State.NORMAL, State.DEFECT]:
            print('444')
            product.state = new_state
            print(new_state)
            print(product)
            product.save()
            return JsonResponse({'message': 'Состояние продукта успешно изменено.'})
        else:
            return JsonResponse({'error': 'Неверное состояние продукта.'}, status=400)


class ProducDefecttItemViewSet(ModelViewSet):
    serializer_class = product_ser.ProductDefectSerializer
    lookup_field = 'pk'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'identification_number']

    def get_queryset(self):
        queryset = product_models.ProductDefect.objects.filter(product__is_archived=False, product__state='defect')
        print(queryset)

        # Фильтрация по комбинированным полям без учета регистра и акцентов (для PostgreSQL)
        search_query = self.request.query_params.get('search_query', None)
        if search_query:
            queryset = queryset.filter(
                Q(name__iregex=fr'.*{search_query}.*') |
                Q(identification_number__iregex=fr'.*{search_query}.*')
            )

        # Фильтрация по отдельным полям без учета регистра (для PostgreSQL)
        state_filter = self.request.query_params.get('state', None)
        if state_filter:
            queryset = queryset.filter(state__iexact=state_filter)

        category_filter = self.request.query_params.get('category', None)
        if category_filter:
            queryset = queryset.filter(category__title__iexact=category_filter)

        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_archived = True
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)



class ProductItemViewSet(ModelViewSet):
    serializer_class = product_ser.ProductItemSerializer
    lookup_field = 'pk'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'identification_number']

    def get_queryset(self):
        queryset = product_models.ProductNormal.objects.filter(is_archived=False, state='normal')

        # Фильтрация по комбинированным полям без учета регистра и акцентов (для PostgreSQL)
        search_query = self.request.query_params.get('search_query', None)
        if search_query:
            queryset = queryset.filter(
                Q(name__iregex=fr'.*{search_query}.*') |
                Q(identification_number__iregex=fr'.*{search_query}.*')
            )

        # Фильтрация по отдельным полям без учета регистра (для PostgreSQL)
        state_filter = self.request.query_params.get('state', None)
        if state_filter:
            queryset = queryset.filter(state__iexact=state_filter)

        category_filter = self.request.query_params.get('category', None)
        if category_filter:
            queryset = queryset.filter(category__title__iexact=category_filter)

        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_archived = True
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)




class ArchivedProductView(ModelViewSet):
    queryset = product_models.ProductNormal.objects.filter(is_archived=True)
    serializer_class = product_ser.ProductItemSerializer
    lookup_field = 'pk'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'identification_number']

    # restore -> product
    def restore(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_archived = False
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class Search(APIView):
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['name']

    def get(self, request, format=None):
        queryset = product_models.ProductNormal.objects.filter(is_archived=False)

        search_query = request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(name__iregex=fr'.*{search_query}.*')
            )

        # Получаем уникальные имена и категории
        unique_names_and_categories = queryset.values_list('name', 'category').distinct()

        # Создаем список словарей с уникальными именами и категориями
        result_data = [{'name': name, 'category': category} for name, category in unique_names_and_categories]

        serializer = product_ser.SearchSer(result_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)