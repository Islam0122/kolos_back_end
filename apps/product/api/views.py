from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse as json_resp
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from product.models import Category, Product
from .serializers import CategorySerializer, ProductItemSerializer, ProductTipSerializer

import seeder_beer as sd


def seeder_start(request):
    sd.seed()
    return json_resp({'status': 'success'})


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'


class ProductItemViewSet(ModelViewSet):
    queryset = Product.objects.filter(is_archived=False)
    serializer_class = ProductItemSerializer
    lookup_field = 'pk'
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'identification_number']
    filterset_fields = ['category', 'state']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_archived = True
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ArchivedProductView(ModelViewSet):
    queryset = Product.objects.filter(is_archived=True)
    serializer_class = ProductItemSerializer
    lookup_field = 'pk'

    # restore -> product
    def restore(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_archived = False
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class TipViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductTipSerializer
    lookup_field = 'pk'
