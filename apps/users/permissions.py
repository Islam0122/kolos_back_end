from rest_framework import permissions


class IsStockPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'Завсклад' or 'Директор')


class IsGuestPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'Гость')
