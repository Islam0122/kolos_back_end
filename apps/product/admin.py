from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from . import models as m
from common.mixins import ChangeHistoryMixin

admin.site.register(m.Category)
# admin.site.register(m.Warehouse)


@admin.register(m.ProductNormal)
class ProductNormalAdmin(SimpleHistoryAdmin, ChangeHistoryMixin):
    list_filter = ["is_archived", "state", "category"]

    # Запрещаем добавление и удаление объектов
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

@admin.register(m.ProductDefect)
class ProductDefectAdmin(SimpleHistoryAdmin, ChangeHistoryMixin):
    list_display = ['product', ]

    # Запрещаем добавление и удаление объектов
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
