from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import TestEndpoint

urlpatterns = [
    path('login/', views.LoginAPIView.as_view(), name='login'),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),
    # path('register/', views.RegistrationView.as_view(), name='register'),
    # path('test/', TestEndpoint.as_view(), name='test_endpoint'),
]
