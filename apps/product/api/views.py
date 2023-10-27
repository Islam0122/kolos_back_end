from rest_framework.viewsets import ModelViewSet

from product import models as prod_mod
from product.api import serializers as prod_ser


class ProductViewSet(ModelViewSet):
    queryset = prod_mod.ProductItem.objects.filter(is_archived=False)
    serializer_class = prod_ser.ProductSerializer
    lookup_field = 'pk'


class ArchivedProductView(ModelViewSet):
    queryset = prod_mod.ProductItem.objects.filter(is_archived=True)
    serializer_class = prod_ser.ProductSerializer
    lookup_field = 'pk'


