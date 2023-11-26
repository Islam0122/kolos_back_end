from django.db.models import Q
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse as json_resp
from django_filters.rest_framework import DjangoFilterBackend
from product import models as product_models
from product.api import serializers as product_ser

import seeder_beer as sd



def seeder_start(request):
    sd.seed()
    return json_resp({'status': 'success'})


class ProductItemViewSet(ModelViewSet):
    serializer_class = product_ser.ProductItemSerializer
    lookup_field = 'pk'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'identification_number']

    def get_queryset(self):
        queryset = product_models.Product.objects.filter(is_archived=False)

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
    queryset = product_models.Product.objects.filter(is_archived=True)
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


class TypeViewSet(ModelViewSet):
    queryset = product_models.Product.objects.all()
    serializer_class = product_ser.ProductTypeSerializer
    lookup_field = 'pk'