from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        user = self.model(
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'Директор')

        return self.create_user(username, password, **extra_fields)
