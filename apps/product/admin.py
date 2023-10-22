from django.contrib import admin

from . import models as m

# Register your models here.
admin.site.register(m.Category)


@admin.register(m.Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ["is_archived"]
