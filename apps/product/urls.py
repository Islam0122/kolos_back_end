from django.urls import path
from .api import views

urlpatterns = [
    path('db_seed/', views.seeder_start),
    #product


    path('', views.ProductItemViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/', views.ProductItemViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    #product -> archive


    path('archive/', views.ArchivedProductView.as_view({'get': 'list'})),
    path('archive/<int:pk>/', views.ArchivedProductView.as_view({'get': 'retrieve',
                                                                 'put': 'update',
                                                                 'delete': 'restore'})),

    path('type/', views.TypeViewSet.as_view({'get': 'list'}))
]

