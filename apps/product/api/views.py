from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse as json_resp
from django_filters.rest_framework import DjangoFilterBackend

from product import models as product_models
from product.api import filters as product_filters
from product.api import serializers as product_ser

import seeder_beer as sd


def seeder_start(request):
    sd.seed()
    return json_resp({'status': 'success'})


class ProductItemViewSet(ModelViewSet):
    queryset = product_models.Product.objects.filter(is_archived=False)
    serializer_class = product_ser.ProductItemSerializer
    lookup_field = 'pk'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'identification_number']
    filterset_class = product_filters.ProductFilter

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_archived = True
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ArchivedProductView(ModelViewSet):
    queryset = product_models.Product.objects.filter(is_archived=True)
    serializer_class = product_ser.ProductItemSerializer
    lookup_field = 'pk'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'identification_number']
    filterset_class = product_filters.ProductFilter

    # restore -> product
    def restore(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_archived = False
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class TipViewSet(ModelViewSet):
    queryset = product_models.Product.objects.all()
    serializer_class = product_ser.ProductTipSerializer
    lookup_field = 'pk'
