from django.contrib import admin
from rest_framework.authtoken.models import TokenProxy

from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


admin.site.unregister(TokenProxy)

@admin.register(CustomUser)
class UserAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'last_name']
    list_filter = ("is_superuser", "is_active")
    search_fields = ('username', 'first_name', 'last_name', 'role')

    fieldsets = (
        (_('Данные для входа'), {'fields': ('username', 'password')}),
        (_('Пользователь'), {'fields': ('first_name', 'last_name')}),
        (_('Настройки пользователя'), {'fields': ('role', 'is_active')}),
    )

    add_fieldsets = (
        (_('Данные для входа'), {'fields': ('username', 'password1', 'password2')}),
        (_('Пользователь'), {'fields': ('first_name', 'last_name')}),
        (_('Настройки пользователя'), {'fields': ('role', 'is_active')}),
    )