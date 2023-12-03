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

class ProductDefectItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='product.name')
    identification_number = serializers.CharField(source='product.identification_number')
    unit = serializers.CharField(source='product.unit')
    price = serializers.IntegerField(source='product.price')
    sum = serializers.IntegerField(source='product.sum')
    state = serializers.CharField(source='product.state')
    is_archived = serializers.BooleanField(source='product.is_archived')
    category = serializers.CharField(source='product.category.title')

    class Meta:
        model = m.ProductDefect
        fields = ['id', 'name', 'identification_number', 'unit', 'price', 'sum', 'state', 'is_archived', 'category', 'quantity', 'warehouse']