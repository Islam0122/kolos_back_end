import rest_framework.serializers
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.product.serializer import ProductSerializers, ProductValidateSerializer
from apps.product.models import Product


# Create your views here.
class ProductViewSet(ModelViewSet):  # GET/PUT/DELETE/CREATE/POST
    queryset = Product.objects.all().select_related('category')
    serializer_class = ProductSerializers
    lookup_field = 'pk'

    def create(self, request, *args, **kwargs):
        serializer = ProductValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product = Product.objects.create(
            title=serializer.validated_data.get('title'),
            category_id=serializer.validated_data.get('category_id'),
            unit_of_measurement=serializer.validated_data.get('unit_of_measurement'),
            quantity=serializer.validated_data.get('quantity'),
            price=serializer.validated_data.get('price'),
            status=serializer.validated_data.get('status'),
        )

        return Response(data=self.serializer_class(product, many=False).data, status=status.HTTP_201_CREATED)