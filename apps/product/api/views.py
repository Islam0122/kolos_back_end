from django.db.models import Q
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse as json_resp
from django_filters.rest_framework import DjangoFilterBackend

from product import models as m
from .filters import ProductFilter
from . import  serializers as ser
import seeder_beer as sd


def seeder_start(request):
    sd.seed()
    return json_resp({'status': 'success'})



class CategoryViewSet(ModelViewSet):
    queryset = m.Category.objects.all()
    serializer_class = ser.CategorySerializer
    lookup_field = 'pk'






class ProductItemViewSet(ModelViewSet):
    queryset = m.Product.objects.filter(is_archived=False)
    serializer_class = ser.ProductItemSerializer
    lookup_field = 'pk'
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['product__name','product__identification_number']
    filterset_class = ProductFilter


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_archived = True
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)








class ArchivedProductView(ModelViewSet):
    queryset = m.Product.objects.filter(is_archived=True)
    serializer_class = ser.ProductItemSerializer
    lookup_field = 'pk'

    # restore -> product
    def restore(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_archived = False
        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)




class TipViewSet(ModelViewSet):
    queryset = m.Product.objects.all()
    serializer_class = ser.ProductTipSerializer
    lookup_field = 'pk'
