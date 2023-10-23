from django.contrib import admin
from .models import Distributor



# Register your models here.
# admin.site.register(Distributor)
# admin.site.register(Contact)


@admin.register(Distributor)
class DistriAdmin(admin.ModelAdmin):
    list_filter = ["is_archived"]