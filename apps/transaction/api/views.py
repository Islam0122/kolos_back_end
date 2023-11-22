from rest_framework import viewsets, status
from ..models import Invoice, InvoiceItems
from .serializers import InvoiceSerializer, InvoiceItemsSerializer
from rest_framework.response import Response
from rest_framework import generics


class InvoiceItemsViewSet(generics.ListCreateAPIView):
    queryset = InvoiceItems.objects.all()
    serializer_class = InvoiceItemsSerializer


class InvoiceItemsViewSetDet(generics.RetrieveUpdateDestroyAPIView):
    queryset = InvoiceItems.objects.all()
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

    def create(self, request, *args, **kwargs):
        products_invoice_data = request.data.pop('products_invoice', None)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = serializer.save()
        if products_invoice_data:
            for product_data in products_invoice_data:
                InvoiceItems.objects.create(invoice=instance, **product_data)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DistributorInvoiceItemsView(generics.ListAPIView):
    serializer_class = InvoiceItemsSerializer

    def get_queryset(self):
        distributor_id = self.kwargs['distributor_id']
        return InvoiceItems.objects.filter(invoice__distributor__id=distributor_id)