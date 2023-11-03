from django_filters import rest_framework as filters
from product import models as prod_mod


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class ProductFilter(filters.FilterSet):
    category = CharFilterInFilter(field_name='category', lookup_expr='in')
    create_data__gte = filters.DateFilter(field_name="created_at", lookup_expr="gte")
    create_data__lte = filters.DateFilter(field_name="created_at", lookup_expr="lte")

    class Meta:
        model = prod_mod.ProductItem
        fields = ['category', 'create_date']
