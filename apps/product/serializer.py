from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from product.models import Product, Category ,ArchiveProduct


# Те же самые ошибки что и в Distributor
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# метод split занимает много места и при интерпретировании много времени, так что рекомендую засунуть все это в
# tuple(кортеж)
class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'title category_title identification_number unit_of_measurement quantity price status total_price ' \
                 'create_data '.split()


class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, min_length=1, max_length=100)
    category_id = serializers.IntegerField()
    unit_of_measurement = serializers.CharField(max_length=10, default="литр")
    quantity = serializers.IntegerField(default=1)
    price = serializers.IntegerField()
    status = serializers.CharField(max_length=10)

    def validate_category_id(self, category_id):  # 10
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError('Category does not exists!')
        return category_id


# народ GPT это конечно, очень хорошо и радует глаз то,
# что технологии развиваюься с такой большой скоростью,
# но немного перебарщиваете с его использованием
class ArchivedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchiveProduct  # Replace 'A' with the correct model name
        fields = '__all__'