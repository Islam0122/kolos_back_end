from django.urls import path
from .api import views

urlpatterns = [

    path('', views.ProductViewSet.as_view({'get': 'list'})),
    path('create/', views.ProductViewSet.as_view({'post': 'create'})),
    path('<int:pk>/', views.ProductViewSet.as_view({'get': 'retrieve',
                                                    'put': 'update',
                                                    'delete': 'destroy'})),


    path('Invalid/', views.InvalidProductViewSet.as_view({'get': 'list'})),
    path('Invalid/<int:pk>/', views.InvalidProductViewSet.as_view({
                                                    'get': 'retrieve',
                                                    'put': 'update',
                                                    'delete': 'destroy'})),
    path('db_seed/', views.seeder_start),

    path('archive/', views.ArchivedProductView.as_view({'get': 'list'})),
    path('archive/<int:pk>/', views.ArchivedProductView.as_view({'get': 'retrieve',
                                                                 'put': 'update',
                                                                 'delete': 'restore'}))
]
