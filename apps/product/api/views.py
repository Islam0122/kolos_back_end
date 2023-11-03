from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from product import models as prod_mod
from product.api import serializers as prod_ser

# search
from django_filters import rest_framework as rest_filter
from rest_framework import filters


class ProductViewSet(ModelViewSet):
    queryset = prod_mod.ProductItem.objects.filter(is_archived=False)
    serializer_class = prod_ser.ProductItemSerializer
    lookup_field = 'pk'
    ## filter,search
    filter_backends = [rest_filter.DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title']

    # /api/v1/product/archive?search=
    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.query_params.get('search', None)
        if keyword:
            queryset = queryset.filter(title__icontains=keyword)
        return queryset

    # delete -> archived
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_archived = True
        instance.save()

        return Response(status=status.c_NO_CONTENT)


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


