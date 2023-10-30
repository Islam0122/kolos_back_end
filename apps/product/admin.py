from django.contrib import admin

from . import models as m


@admin.register(m.ProductItem)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ["is_archived"]
