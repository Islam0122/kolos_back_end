from django.urls import path
from .api import views, pdf_view as _


urlpatterns = [
    #order
    path('', views.InvoiceViewSet.as_view({'get': 'list',
                                        'post': 'create'})),
    path('<int:pk>/', views.InvoiceViewSet.as_view({'get': 'retrieve'})),
    path('generate_pdf/<int:pk>/', _.GeneratePdf.as_view(), name='generate_pdf'),


    # path('archive/', views.ArchivedOrderView.as_view({'get': 'list'})),
    # path('archive/<int:pk>/', views.ArchivedOrderView.as_view({'get': 'retrieve',
    #                                                              'put': 'update',
    #                                                              'delete': 'restore'})),

]


