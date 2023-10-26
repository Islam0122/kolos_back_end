from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.core.validators import RegexValidator
from .models import CustomUser


def create_custom_validator(field_name, min_length, max_length, message):
    return serializers.CharField(
        min_length=min_length,
        max_length=max_length,
        allow_blank=False,
        allow_null=False,
        validators=[RegexValidator(regex='^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]*$', message=message)])


class UserSerializer(serializers.Serializer):
    username = create_custom_validator('username', 4, 8, 'Логин должен состоять только из букв и цифр.')
    password = create_custom_validator('password', 8, 12,
                                       'Пароль должен содержать как минимум одну букву и одну цифру.')


class UserCreateSerializer(UserSerializer):
    def validate(self, data):
        username = data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError('Пользователь с таким именем уже существует')
        return data
