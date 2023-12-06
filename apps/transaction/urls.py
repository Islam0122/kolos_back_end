from django.urls import path
from .api import views as _
from .api.pdf_view import GeneratePdf, GenerateReturnPdf

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

    # генерация pdf конкретной продажи по id накладной
    path('generate_pdf/<int:pk>/', GeneratePdf.as_view(), name='generate_pdf'),

    # список всех продуктов проданных дистрибутору по его id
    path('distributor/<int:distributor_id>/', _.DistributorInvoiceItemsView.as_view(),
         name='distributor_invoice_items'),

#ВОЗВРАТ


    # возврат товара и список всех продаж
    path('return_invoices/', _.ReturnInvoiceViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='return-invoices'),

    # детальный обзор продажи
    path('return_invoices/<int:pk>/', _.ReturnInvoiceViewSet.as_view({
        'get': 'retrieve'
    }), name='invoices'),

    # список всех возвратных продуктов дистрибутору по его id
    path('return/distributor/<int:distributor_id>/', _.ReturnInvoiceListByDistributor.as_view(),
         name='distributor_return_invoice_items'),

    # генерация pdf конкретного возврата по id накладной
    path('generate_return_pdf/<int:pk>/', GenerateReturnPdf.as_view(), name='generate_return_pdf'),

    # path('search_sale/', _.SearchSale.as_view(), name='search_sale'),

    path('clue-products-sold/<int:distributor_id>/', _.SearchSold.as_view()),
    path('clue-products-returned/<int:distributor_id>/', _.SearchReturned.as_view()),


    # path('invoice_items/', InvoiceItemsViewSet.as_view(), name='invoice-items-list'),
    # path('invoice_items/<int:pk>/', InvoiceItemsViewSetDet.as_view(), name='invoice-items-detail'),
     ]