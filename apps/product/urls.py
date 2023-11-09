from django.urls import path
from .api import views

urlpatterns = [
    #product
    path('', views.ProductItemViewSet.as_view({'get': 'list','post': 'create'})),

    path('<int:pk>/', views.ProductItemViewSet.as_view({'get': 'retrieve',
                                                    'put': 'update',
                                                    'delete': 'destroy'})),
    #product -> archive
    path('db_seed/', views.seeder_start),

    path('archive/', views.ArchivedProductView.as_view({'get': 'list'})),
    path('archive/<int:pk>/', views.ArchivedProductView.as_view({'get': 'retrieve',
                                                                 'put': 'update',
                                                                 'delete': 'restore'})),
    #category
    path('category/', views.CategoryViewSet.as_view({'get': 'list',
                                                     'post': 'create'})),
    path('category/<int:pk>/', views.CategoryViewSet.as_view({'get': 'retrieve',
                                                                 'put': 'update',
                                                                 'delete': 'restore'})),
    path('tip/', views.TipViewSet.as_view({'get': 'list'}))
]

