from django.contrib import admin
from .models import LoginAttempt, CustomUser

admin.site.register(LoginAttempt)
admin.site.register(CustomUser)
