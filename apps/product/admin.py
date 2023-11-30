from django.contrib import admin

from . import models as m

admin.site.register(m.Category)


@admin.register(m.ProductNormal)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ["is_archived", "state", "category"]


@admin.register(m.ProductDefect)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ["is_archived", "state", "category"]