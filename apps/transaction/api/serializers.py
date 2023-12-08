from rest_framework import serializers
from ..models import Invoice, InvoiceItems, ReturnInvoiceItems, ReturnInvoice


class InvoiceItemsSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    identification_number = serializers.SerializerMethodField()
    unit = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()
    sale_date = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = InvoiceItems
        fields = ['id', 'name', 'identification_number', 'unit', 'price', 'quantity',
                  'sale_date', 'total_price', 'category']

    def get_identification_number(self, obj):
        return obj.product.identification_number

    def get_name(self, obj):
        return obj.product.name

    def get_unit(self, obj):
        return obj.product.unit

    def get_price(self, obj):
        return obj.product.price

    def get_sale_date(self, obj):
        return obj.invoice.sale_date

    def get_category(self, obj):  # Добавляем метод для получения категории
        return obj.product.category.title

    def get_total_price(self, obj):
        return obj.total_price()


class InvoiceSerializer(serializers.ModelSerializer):
    read_only_fields = ['id', 'sale_date']
    products_invoice = InvoiceItemsSerializer(many=True, read_only=True)

    class Meta:
        model = Invoice
        fields = ['id', 'distributor', 'sale_date', 'products_invoice', 'identification_number_invoice']


class ReturnInvoiceItemsSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    identification_number = serializers.SerializerMethodField()
    unit = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()
    return_date = serializers.SerializerMethodField()
    sale_date = serializers.SerializerMethodField()

    class Meta:
        model = ReturnInvoiceItems
        fields = ['id', 'name', 'identification_number', 'unit', 'quantity', 'price',
                   'total_price', 'return_date', 'sale_date', 'state']

    def get_identification_number(self, obj):
        return obj.invoice_item.product.identification_number

    def get_name(self, obj):
        return obj.invoice_item.product.name

    def get_unit(self, obj):
        return obj.invoice_item.product.unit

    def get_price(self, obj):
        return obj.invoice_item.product.price

    def get_return_date(self, obj):
        return obj.return_invoice.return_date

    def get_sale_date(self, obj):
        try:
            sale_date = obj.invoice_item.invoice.sale_date
            return sale_date
        except AttributeError:
            return None


    def get_total_price(self, obj):
        return obj.total_price()



class ReturnInvoiceItemsSerializerPDF(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    identification_number = serializers.SerializerMethodField()
    unit = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()
    return_date = serializers.SerializerMethodField()
    sale_date = serializers.SerializerMethodField()

    class Meta:
        model = ReturnInvoiceItems
        fields = ['id', 'name', 'identification_number', 'unit', 'quantity', 'price',
                   'total_price', 'return_date', 'sale_date', 'state']


    def get_identification_number(self, obj):
        return obj.invoice_item.product.identification_number

    def get_name(self, obj):
        return obj.invoice_item.product.name

    def get_unit(self, obj):
        return obj.invoice_item.product.unit

    def get_price(self, obj):
        return obj.invoice_item.product.price

    def get_return_date(self, obj):
        return obj.return_invoice.return_date

    def get_sale_date(self, obj):
        try:
            sale_date = obj.invoice_item.invoice.sale_date
            return sale_date
        except AttributeError:
            return None


    def get_total_price(self, obj):
        return obj.total_price()



class ReturnInvoiceSerializer(serializers.ModelSerializer):
    products_return_invoice = InvoiceItemsSerializer(many=True, read_only=True)


    class Meta:
        model = ReturnInvoice
        fields = ['id', 'distributor', 'return_date', 'products_return_invoice']



class SearchSerSeles(serializers.Serializer):
    name = serializers.CharField()
    category = serializers.CharField()



class ClueSearchSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = ReturnInvoiceItems
        fields = ['id', 'name', 'category']

    def get_name(self, obj):
        return obj.invoice_item.product.name

    def get_category(self, obj):  # Метод для получения категории
        return obj.invoice_item.product.category.title