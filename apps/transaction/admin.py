from django.contrib import admin

from . import models as m

admin.site.register(m.InvoiceItems)
admin.site.register(m.ReturnInvoiceItems)

@admin.register(m.Invoice)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ["id"]
