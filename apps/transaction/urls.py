from django.urls import path
from .api import views as _
from .api.pdf_view import GeneratePdf


urlpatterns = [
    # продажа товара и список всех продаж
    path('invoices/', _.InvoiceViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),

    # детальный обзор продажи
    path('invoices/<int:pk>/', _.InvoiceViewSet.as_view({
        'get': 'retrieve'
    }), name='invoices'),

    # генерация pdf конкретной продажи по id продажи
    path('generate_pdf/<int:pk>/', GeneratePdf.as_view(), name='generate_pdf'),

    # список всех продуктов проданных дистрибутору по его id
    path('distributor/<int:distributor_id>/', _.DistributorInvoiceItemsView.as_view(),
         name='distributor_invoice_items'),



    # path('invoice/', InvoiceViewSet.as_view(), name='invoice-list'),
    # path('invoice_items/', InvoiceItemsViewSet.as_view(), name='invoice-items-list'),
    # path('invoice_items/<int:pk>/', InvoiceItemsViewSetDet.as_view(), name='invoice-items-detail'),
     ]