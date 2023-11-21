from rest_framework import viewsets
from ..models import Invoice, InvoiceItems
from .serializers import InvoiceSerializer, InvoiceItemsSerializer
from rest_framework.response import Response
from rest_framework import generics


class InvoiceItemsViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceItemsSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        products = InvoiceItems.objects.filter(invoice=instance)
        products_serializer = InvoiceItemsSerializer(products, many=True)
        response_data = serializer.data
        response_data['products_invoice'] = products_serializer.data
        return Response(response_data)


class DistributorInvoiceItemsView(generics.ListAPIView):
    serializer_class = InvoiceItemsSerializer

    def get_queryset(self):
        distributor_id = self.kwargs['distributor_id']
        invoices = Invoice.objects.filter(distributor__id=distributor_id)
        items = InvoiceItems.objects.filter(invoice__in=invoices)
        return items