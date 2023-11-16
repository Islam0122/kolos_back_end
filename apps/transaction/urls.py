from django.urls import path
from .api import views

urlpatterns = [
    #order
    path('', views.OrderViewSet.as_view({'get': 'list'})),
    path('<int:pk>/', views.OrderViewSet.as_view({'get': 'retrieve',
                                                    'post': 'create'})),


    # path('archive/', views.ArchivedOrderView.as_view({'get': 'list'})),
    # path('archive/<int:pk>/', views.ArchivedOrderView.as_view({'get': 'retrieve',
    #                                                              'put': 'update',
    #                                                              'delete': 'restore'})),

]


