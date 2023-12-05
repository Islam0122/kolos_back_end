from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from . import models as m
from common.mixins import ChangeHistoryMixin

admin.site.register(m.Category)
admin.site.register(m.Warehouse)


@admin.register(m.ProductNormal)
class ProductNormalAdmin(SimpleHistoryAdmin, ChangeHistoryMixin):
    list_filter = ["is_archived", "state", "category"]


@admin.register(m.ProductDefect)
class ProductDefectAdmin(SimpleHistoryAdmin, ChangeHistoryMixin):
    list_display = ['product', ]
