from rest_framework import serializers
from product import models as m


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Category
        fields = '__all__'


class ProductItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = m.Product
        fields = '__all__'