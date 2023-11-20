from django.urls import path
from .api import views as _
from .api.pdf_view import GeneratePdf

urlpatterns = [

    path('generate_pdf/<int:pk>/', GeneratePdf.as_view(), name='generate_pdf'),
    path('invoices/', _.InvoiceViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('invoices/<int:pk>/', _.InvoiceViewSet.as_view({'get': 'retrieve'})),
    path('distributor/<int:distributor_id>/', _.DistributorInvoiceItemsView.as_view(),
         name='distributor_invoice_items'),

    # path('archive/', views.ArchivedOrderView.as_view({'get': 'list'})),
    # path('archive/<int:pk>/', views.ArchivedOrderView.as_view({'get': 'retrieve',
    #                                                              'put': 'update',
    #                                                              'delete': 'restore'})),

]


