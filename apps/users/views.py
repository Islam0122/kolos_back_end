# Import necessary modules
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from django.contrib.auth import authenticate

# Import serializers (assuming you have created them)
from .serializers import UserRegistrationSerializer, UserLoginSerializer


# Registration User ViewSet
class RegistrationUserViewSet(ModelViewSet):
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Login User ViewSet
# название класса с БОЛЬШОЙ БУКВЫ
class login_userViewSet(ModelViewSet):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user:
            token, created = Token.objects.get_or_create(user=user)
        # можно вместо else ничего не писать
            return Response({'token': token.key})
        else:
            return Response(status=401, data={'error': 'Invalid credentials'})
