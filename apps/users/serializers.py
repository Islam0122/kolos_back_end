from rest_framework import serializers
from django.contrib.auth.models import User


# Ребята используем менеджеры и AbstractBaseUser для его переопределения(это удалить и переделать)
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already taken")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
