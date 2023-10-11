from django.urls import path

from . import views

<<<<<<< HEAD
router = DefaultRouter()
router.register('distributor', views.DistributorView, 'api_distributor')

urlpatterns = router.urls
=======
urlpatterns = [
    # Маршруты для DistributorView
    path('distributor/', views.DistributorView.as_view({'get': 'list', 'post': 'create'}), name='distributor-list'),
    path('distributor/<int:pk>/', views.DistributorView.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='distributor-detail'),
    path('distributor/<int:pk>/archive/', views.DistributorView.as_view({'post': 'archive'}), name='distributor-archive'),
    path('distributor/<int:pk>/restore/', views.DistributorView.as_view({'post': 'restore'}), name='distributor-restore'),
    
    # Маршруты для ArchivedDistributorListView
    path('archived-distributors/', views.ArchivedDistributorListView.as_view(), name='archived-distributor-list'),
]
>>>>>>> 96926b2519640b01f8190961ecc35c88dd3b12c5
