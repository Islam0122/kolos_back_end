from django.urls import path
from .views import *


urlpatterns = [
    path('', DistributorViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/',
         DistributorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('archive/', ArchivedDistributorView.as_view({'get': 'list'})),
    path('archive/<int:pk>/', ArchivedDistributorView.as_view({'get': 'retrieve', 'put': 'restore'}))
]
