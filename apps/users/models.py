from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('Поле Имя пользователя должно быть задано')
        user = self.model(username=username, **extra_fields)
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must have is_staff = True")

        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser = True")
        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=254, unique=True)
    password = models.CharField(max_length=128, null=True)
    email = models.EmailField(unique=True, null=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password']

    objects = UserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class LoginAttempt(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.PROTECT, db_constraint=False, null=True)
    failed_attempts = models.IntegerField(default=0)
    last_failed_attempt = models.DateTimeField(null=True)
    blocked = models.BooleanField(default=False)
    block_duration = models.DateTimeField(null=True, blank=True)

    def increase_failed_attempts(self):
        self.failed_attempts += 1
        self.last_failed_attempt = timezone.now()
        self.save()

    def is_blocked(self):
        return self.blocked and self.block_duration is not None and self.block_duration > timezone.now()

    def block_user(self, duration=None):
        self.blocked = True
        if duration:
            self.block_duration = timezone.now() + duration
        else:
            self.block_duration = timezone.now() + timezone.timedelta(minutes=30)
        self.failed_attempts = 0  # Сброс количества неудачных попыток
        self.save()

    def unblock_user(self):
        self.blocked = False
        self.block_duration = None
        self.save()

    def __str__(self):
        return f"LoginAttempt for {self.user.username if self.user else 'anonymous'} - Failed attempts: {self.failed_attempts}"

    class Meta:
        verbose_name = "Заблокированный пользователь"
        verbose_name_plural = "Заблокированные пользователи"
