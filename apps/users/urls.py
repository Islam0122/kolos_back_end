from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegistrationUserViewSet.as_view({'post': 'create'})),
    path('login/', views.login_userViewSet.as_view({'post': 'post'})),
]