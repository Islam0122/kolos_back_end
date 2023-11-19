import django_filters
from product import models as prod_mod

from django_filters import rest_framework as filters
from product.models import Product, Category
from rest_framework.filters import SearchFilter


class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = ['category', 'state']
