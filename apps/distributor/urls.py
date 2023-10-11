from django.urls import path

from . import views


urlpatterns = [
    path('', views.DistributorViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/',
         views.DistributorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('<int:pk>/restore/', views.DistributorViewSet.as_view({'put': 'restore'})),
    path('archived-distributors/', views.ArchivedDistributorListView.as_view(), name='archived-distributor-list'),
]
