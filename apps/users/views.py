from django.utils import timezone
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth import authenticate, login
from .models import CustomUser, LoginAttempt
from .serializers import UserSerializer, UserCreateSerializer
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from core.settings.base import MAX_LOGIN_ATTEMPTS, LOCKOUT_DURATION

class TestEndpoint(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({'message': f'Добро пожаловать, {user.username}!'})

class LoginAPIView(APIView):
    @swagger_auto_schema(request_body=UserSerializer, responses={200: 'OK', 400: 'Bad Request'},)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = authenticate(request, **serializer.validated_data)
            login_attempt, created = LoginAttempt.objects.get_or_create(user=user)

            if login_attempt.is_blocked():
                return Response(
                    {'detail': 'Превышено максимальное количество попыток, пользователь временно заблокирован'},
                    status=status.HTTP_423_LOCKED)

            if user is None:
                login_attempt.increase_failed_attempts()
                if login_attempt.failed_attempts >= MAX_LOGIN_ATTEMPTS:
                    login_attempt.block_user(LOCKOUT_DURATION)

                return Response({'detail': 'Неверные данные, попробуйте ещё раз!'}, status=status.HTTP_400_BAD_REQUEST)

            # Успешная аутентификация
            login_attempt.unblock_user()  # Снимаем блокировку, если она была
            login(request, user)

            return Response(data={"message": "Вход в систему выполнен успешно",
                                  "access": str(AccessToken.for_user(user)),
                                  "refresh": str(RefreshToken.for_user(user)),
                                  "role": "Директор" if user.is_superuser else "Завсклад"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

