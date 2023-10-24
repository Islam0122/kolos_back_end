from django_filters import rest_framework as filters
from .product.models import Product

class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class ProductFilter(filters.FilterSet):
    category = CharFilterInFilter(field_name='category__title', lookup_expr='in')
    create_data__gte = filters.DateFilter(field_name="create_date", lookup_expr="gte")
    create_data__lte = filters.DateFilter(field_name="create_date", lookup_expr="lte")

    class Meta:
        model = Product
        fields = ['category', 'create_date']

