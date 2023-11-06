import django_filters
from product import models as prod_mod


class CharFilterInFilter(django_filters.rest_framework.BaseInFilter, django_filters.rest_framework.CharFilter):
    pass


class ProductFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = prod_mod.ProductItem
        fields = ['category',"state"]
