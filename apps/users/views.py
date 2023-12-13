from axes.decorators import axes_dispatch
from django.core.management import call_command
from django.utils.decorators import method_decorator
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth import authenticate, login
from .models import CustomUser
from .serializers import UserSerializer, UserCreateSerializer
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema


class TestEndpoint(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({'message': f'Добро пожаловать, {user.username}!'})


class LoginAPIView(APIView):
    @method_decorator(axes_dispatch)
    @swagger_auto_schema(request_body=UserSerializer, responses={200: 'OK', 400: 'Bad Request'},)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(request, **serializer.validated_data)

        if user:
            login(request, user)
            return Response(data={"message": "Вход в систему выполнен успешно",
                                  "access": str(AccessToken.for_user(user)),
                                  "refresh": str(RefreshToken.for_user(user)),
                                  "role": user.role}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Неверные данные, попробуйте ещё раз!'}, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        auth_token = request.data.get('access')
        if auth_token and auth_token.user == request.user:
            auth_token.delete()
        return Response({"message": "Вы успешно вышли из системы."}, status=status.HTTP_200_OK)


class RegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = request.data.get('username')
        password = request.data.get('password')
        CustomUser.objects.create_user(username=username, password=password)
        return Response({"message": "Пользователь успешно создан"}, status=status.HTTP_201_CREATED)