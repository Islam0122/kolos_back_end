from django.contrib import admin

from . import models as m

admin.site.register(m.Category)
admin.site.register(m.ProductDefect)


@admin.register(m.ProductNormal)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ["is_archived", "state", "category"]

