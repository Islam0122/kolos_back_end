# filters.py
import django_filters
from product.models import Product

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['exact', 'icontains'],
            'identification_number': ['exact', 'icontains'],
            # Добавьте другие поля, если необходимо
        }