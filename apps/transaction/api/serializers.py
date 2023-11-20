from rest_framework import serializers
from ..models import Invoice, InvoiceItems
from product.api.serializers import ProductItemSerializer
from distributor.api.serializers import DistributorSerializer


class InvoiceItemsSerializer(serializers.ModelSerializer):
    product = ProductItemSerializer()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = InvoiceItems
        fields = ['id', 'product', 'quantity', 'total_price']

    def get_total_price(self, obj):
        return obj.total_price()


class InvoiceSerializer(serializers.ModelSerializer):
    distributor = DistributorSerializer()
    read_only_fields = ['id', 'created_at']
    products_invoice = InvoiceItemsSerializer(many=True, read_only=True)

    class Meta:
        model = Invoice
        fields = ['id', 'distributor', 'created_at', 'products_invoice']
