from django.contrib import admin
from .models import Distributor
from simple_history.admin import SimpleHistoryAdmin
from common.mixins import ChangeHistoryMixin

# Register your models here.
# admin.site.register(Distributor)
# admin.site.register(Contact)


@admin.register(Distributor)
class DistriAdmin(SimpleHistoryAdmin, ChangeHistoryMixin):
    list_filter = ["is_archived"]
