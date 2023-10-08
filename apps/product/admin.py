from django.contrib import admin

# Register your models here.

from apps.product import  models

# Register your models here.
admin.site.register(models.Product)
admin.site.register(models.Category)