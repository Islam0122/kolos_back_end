from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth import authenticate, login
from .models import CustomUser, LoginAttempt
from .serializers import UserSerializer, UserCreateSerializer
from rest_framework.views import APIView
from django.utils import timezone

MAX_LOGIN_ATTEMPTS = 4
LOCKOUT_DURATION = timezone.timedelta(minutes=5)  # Время блокировки (24 часа)

class LoginAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(request, **serializer.validated_data)
        if user is not None:
            LoginAttempt.objects.filter(user=user).delete()
                # Далее выполнить вход пользователя
            token = {"access": str(AccessToken.for_user(user)),
            "refresh": str(RefreshToken.for_user(user)),}
            login(request, user)
            return Response(data={"message": "Вход в систему выполнен успешно", "token": token}, status=status.HTTP_200_OK)

        else:
            try:
                user = CustomUser.objects.get(username=serializer.validated_data['username'])
                login_attempt, created = LoginAttempt.objects.get_or_create(user=user)
                login_attempt.failed_attempts += 1
                login_attempt.last_failed_attempt = timezone.now()
                login_attempt.save()
                if login_attempt.failed_attempts >= MAX_LOGIN_ATTEMPTS:
                        # Заблокировать доступ на LOCKOUT_DURATION
                    login_attempt.blocked_until = timezone.now() + LOCKOUT_DURATION
                    login_attempt.save()
                    return Response({'message': 'Программа временно не работает. Обратитесь к администратору!'},
                                status=status.HTTP_401_UNAUTHORIZED)
                else:
                    return Response({'message': 'Не правильные данные! Попробуйте еще раз!'}, status=status.HTTP_401_UNAUTHORIZED)
            except ObjectDoesNotExist:
                return Response({"message": "Пользователь не существует!"}, status=status.HTTP_404_NOT_FOUND)

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
