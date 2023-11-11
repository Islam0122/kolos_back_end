from django.contrib import admin

from . import models as m



admin.site.register(m.Category)
admin.site.register(m.AbstarctProduct)
admin.site.register(m.Product)

# @admin.register(m.Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_filter = ["is_archived", "state"]
