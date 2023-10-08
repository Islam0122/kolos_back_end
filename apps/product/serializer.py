from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.product.models import Product, Category



class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'




class ProductSerializers(serializers.ModelSerializer):
  class Meta:
        model = Product
        fields = 'title  category_title identification_number unit_of_measurement quantity price status'.split()

class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, min_length=1, max_length=100)
    category_id = serializers.IntegerField()
    unit_of_measurement = serializers.CharField(max_length=10 , default="литр")
    quantity = serializers.IntegerField(default=1)
    price = serializers.IntegerField()
    status = serializers.CharField(max_length=10)


    def validate_category_id(self, category_id):  # 10
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError('Category does not exists!')
        return category_id