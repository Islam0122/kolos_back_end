from rest_framework import serializers
from product.models import AbstractProduct, ProductItem



class ProductItemSerializer(serializers.ModelSerializer):
    # product = AbstractProductSerializer()
    class Meta:
        model = ProductItem
        fields = '__all__'

    # def create(self, validated_data):
    #     # Extract the nested product data
    #     product_data = validated_data.pop('product')
    #     product_item = ProductItem.objects.create(**validated_data)
    #     product, created = AbstractProduct.objects.get_or_create(**product_data)
    #     product_item.product = product
    #     product_item.save()
    #     return product_item

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = prod_mod.ProductItem
#         fields = ['id', 'name', 'identification_number', 'unit', 'quantity', 'price',
#                   'sum', 'category', 'state', 'created_at', 'is_archived']
