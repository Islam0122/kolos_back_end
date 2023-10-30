from rest_framework import serializers

from product import models as prod_mod


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = prod_mod.ProductItem
        fields = ['id', 'name', 'identification_number', 'unit', 'quantity', 'price',
                  'sum', 'category', 'state', 'created_at', 'is_archived']

