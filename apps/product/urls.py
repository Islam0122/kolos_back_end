from django.urls import path
from . import views

urlpatterns = [

    path('', views.ProductViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/',
         views.ProductViewSet.as_view({'get': 'retrieve', 'patch': 'update', 'delete': 'destroy'})),
    path('<int:pk>/restore/', views.ProductViewSet.as_view({'put': 'restore'}))

]
