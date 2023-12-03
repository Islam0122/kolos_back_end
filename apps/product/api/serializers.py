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
        model = m.ProductNormal
        fields = ['id', 'name', 'category', 'identification_number', 'unit', 'quantity', 'price',
                  'sum', 'state', 'warehouse']


class ProductDefectItemSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', queryset=m.Category.objects.all())

    # category_id = serializers.PrimaryKeyRelatedField(source='category', read_only=True)
    sum = serializers.ReadOnlyField()

    class Meta:
        model = m.ProductDefect
        fields = ['id', 'name', 'category', 'identification_number', 'unit', 'quantity', 'price',
                  'sum', 'state']


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.ProductNormal
        fields = ('id', 'name')


class SearchSer(serializers.Serializer):
    name = serializers.CharField()
    category = serializers.CharField()

    class Meta:
        fields = ['name', 'category']


class ProductDefectSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.ProductDefect
        fields = '__all__'


class ProductNormalSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.ProductNormal
        fields = '__all__'