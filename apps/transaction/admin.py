from django.contrib import admin

from . import models as m


admin.site.register(m.Order)


# @admin.register(m.Order)
# class ProductAdmin(admin.ModelOrder):
#     list_filter = ["is_archived", "state"]
