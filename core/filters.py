from django_filters import rest_framework as filters
from apps.product.models import Product

class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class ProductFilter(filters.FilterSet):
    category = CharFilterInFilter(field_name='category__title', lookup_expr='in')

    class Meta:
        model = Product
        fields = ['category']

