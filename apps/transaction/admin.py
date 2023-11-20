from django.contrib import admin

from . import models as m

admin.site.register(m.InvoiceItems)

@admin.register(m.Invoice)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ["id"]
