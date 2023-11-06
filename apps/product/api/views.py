from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse as json_resp

from product import models as prod_mod
from product.api import serializers as prod_ser
import seeder_beer as sd


def seeder_start(request):
    sd.seed()
    return json_resp({'status': 'success'})




class ProductPagination(PageNumberPagination):
    page_size = 10



class ProductViewSet(ModelViewSet):
    queryset = prod_mod.ProductItem.objects.filter(is_archived=False)
    serializer_class = prod_ser.ProductSerializer
    lookup_field = 'pk'
    pagination_class = ProductPagination


class ArchivedProductView(ModelViewSet):
    queryset = prod_mod.ProductItem.objects.filter(is_archived=True)
    serializer_class = prod_ser.ProductSerializer
    lookup_field = 'pk'


