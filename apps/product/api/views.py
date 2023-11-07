import django_filters
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse as json_resp

from product import models as prod_mod
from product.api import serializers as prod_ser
import seeder_beer as sd


def seeder_start(request):
    sd.seed()
    return json_resp({'status': 'success'})

# search
from rest_framework import filters

from product.api.filters import ProductFilter


# filter


class ProductViewSet(ModelViewSet):
    queryset = prod_mod.ProductItem.objects.filter(is_archived=False, state='Normal')
    serializer_class = prod_ser.ProductItemSerializer
    lookup_field = 'pk'
    filter_backends = [filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['name']
    filterset_class  = ProductFilter

    # delete -> archived
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_archived = True
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class InvalidProductViewSet(ModelViewSet):
    queryset = prod_mod.ProductItem.objects.filter(state='Invalid')
    serializer_class = prod_ser.ProductItemSerializer
    lookup_field = 'pk'
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    # delete -> archived
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_archived = True
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ArchivedProductView(ModelViewSet):
    queryset = prod_mod.ProductItem.objects.filter(is_archived=True)
    serializer_class = prod_ser.ProductItemSerializer
    lookup_field = 'pk'

    # restore -> product
    def restore(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_archived = False
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
