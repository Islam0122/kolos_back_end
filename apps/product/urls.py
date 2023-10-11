from django.urls import path
from . import views

urlpatterns = [

    path('', views.ProductViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('product/<int:pk>/',
         views.ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('product/<int:pk>/restore/', views.ProductViewSet.as_view({'put': 'restore'}))

]
