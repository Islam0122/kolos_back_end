from django.urls import path
from .api import views

urlpatterns = [

    path('', views.ProductViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/', views.ProductViewSet.as_view({'get': 'retrieve',
                                                    'put': 'update'})),
    path('archive/', views.ArchivedProductView.as_view({'get': 'list'})),
    path('archive/<int:pk>/', views.ArchivedProductView.as_view({'get': 'retrieve',
                                                                 'put': 'update'})),
    path('db_seed/',views.seeder_start, name='seeder')
]
