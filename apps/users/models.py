from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from users.managers import UserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):

    ROLE = {
        ('Гость', 'Гость'),
        ('Завсклад', 'Завсклад'),
        ('Директор', 'Директор'),
    }

    username = models.CharField(_('Логин'), max_length=200, unique=True, db_index=True)
    is_superuser = models.BooleanField(_('Доступ к админке'), default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(_('Активный пользователь'), default=True)
    role = models.CharField(_('Роль'), choices=ROLE, default='Гость', max_length=100)
    first_name = models.CharField(_('Имя'), max_length=200)
    last_name = models.CharField(_('Фамилия'), max_length=200)
    objects = UserManager()

    USERNAME_FIELD = 'username'

    def save(self, *args, **kwargs):
        if self.role == 'Директор':
            self.is_superuser = True
            self.is_staff = True
        else:
            self.is_superuser = False
            self.is_staff = False

        super().save(*args, **kwargs)

    class Meta:
        db_table = 'users'
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"