from rest_framework import viewsets
from ..models import Invoice, InvoiceItems
from .serializers import InvoiceSerializer, InvoiceItemsSerializer
from rest_framework.response import Response


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

