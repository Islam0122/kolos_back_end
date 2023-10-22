from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Product, Category
from rest_framework import serializers

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title', 'category','category_title', 'identification_number', 'unit_of_measurement',
                  'quantity', 'price', 'status', 'total_price', 'create_date','is_archived']

# # народ GPT это конечно, очень хорошо и радует глаз то,
# # что технологии развиваюься с такой большой скоростью,
# # но немного перебарщиваете с его использованием
# class ArchivedProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ArchiveProduct  # Replace 'A' with the correct model name
#         fields = '__all__'