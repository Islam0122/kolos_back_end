from django.urls import path
from .views import *


urlpatterns = [
    path('', DistributorViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/',
         DistributorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('<int:pk>/restore/', DistributorViewSet.as_view({'put': 'restore'})),
    path('archived-distributors/', ArchivedDistributorListView.as_view(), name='archived-distributor-list'),
]
