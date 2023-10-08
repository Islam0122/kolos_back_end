from django.urls import path
from . import views
urlpatterns = [

    path('product/', views.ProductViewSet.as_view({'get': 'list', 'post':'create'})),
    path('product/<int:pk>/',
         views.ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
