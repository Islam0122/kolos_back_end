from rest_framework import serializers
from ..models import Invoice, InvoiceItems


class InvoiceItemsSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    identification_number = serializers.SerializerMethodField()
    unit = serializers.SerializerMethodField()
    product_price = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = InvoiceItems
        fields = ['id', 'product_name', 'identification_number', 'unit', 'product_price',  'quantity', 'created_at', 'total_price']

    def get_identification_number(self, obj):
        return obj.product.identification_number

    def get_product_name(self, obj):
        return obj.product.name

    def get_unit(self, obj):
        return obj.product.unit

    def get_product_price(self, obj):
        return obj.product.price

    def get_created_at(self, obj):
        return obj.invoice.created_at

    def get_total_price(self, obj):
        return obj.total_price()


class InvoiceSerializer(serializers.ModelSerializer):
    read_only_fields = ['id', 'created_at']
    products_invoice = InvoiceItemsSerializer(many=True, read_only=True)

    class Meta:
        model = Invoice
        fields = ['id', 'distributor', 'created_at', 'products_invoice', 'identification_number_invoice']