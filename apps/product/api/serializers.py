from rest_framework import serializers
from product import models as m


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Category
        fields = ['title', ]


class ProductItemSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', queryset=m.Category.objects.all())

    # category_id = serializers.PrimaryKeyRelatedField(source='category', read_only=True)
    sum = serializers.ReadOnlyField()

    class Meta:
        model = m.Product
        fields = ['id', 'name', 'category', 'identification_number', 'unit', 'quantity', 'price',
                  'sum', 'state']


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Product
        fields = ('id', 'name')