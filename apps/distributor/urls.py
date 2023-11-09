from django.urls import path
from .api import views

urlpatterns = [
    path('', views.DistributorViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/', views.DistributorViewSet.as_view({'get': 'retrieve',
                                                        'put': 'update',
                                                        'delete': 'destroy'})),
    path('archive/', views.ArchivedDistributorView.as_view({'get': 'list'})),
    path('archive/<int:pk>/', views.ArchivedDistributorView.as_view({'get': 'retrieve',
                                                                     'put': 'update',
                                                                     'delete': 'restore'}))
]
