from django.contrib import admin

from product import models as m

# Register your models here.
admin.site.register(m.Product)
admin.site.register(m.Category)
admin.site.register(m.ArchiveProduct)