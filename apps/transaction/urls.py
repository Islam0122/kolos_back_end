from django.urls import path
from .api import views

urlpatterns = [
    #order
    path('', views.InvoiceViewSet.as_view({'get': 'list',
                                        'post': 'create'})),
    path('<int:pk>/', views.InvoiceViewSet.as_view({'get': 'retrieve'})),


    # path('archive/', views.ArchivedOrderView.as_view({'get': 'list'})),
    # path('archive/<int:pk>/', views.ArchivedOrderView.as_view({'get': 'retrieve',
    #                                                              'put': 'update',
    #                                                              'delete': 'restore'})),

]


