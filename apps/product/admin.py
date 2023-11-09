from django.contrib import admin

from . import models as m



admin.site.register(m.Category)
@admin.register(m.Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ["is_archived", "state"]
