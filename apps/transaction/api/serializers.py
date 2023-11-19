from rest_framework import serializers
from transaction import models as m


class InvoiceSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = m.Invoice
        fields = '__all__'

    def get_total_price(self, obj):
        return obj.total_price()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        product = instance.product
        representation['product'] = {
            'id': product.id,
            'name': product.name,
            'unit': product.unit,
            'identification_number': product.identification_number,
            'price': product.price,

        }
        distributor = instance.distributor
        representation['distributor'] = {
            'id': distributor.id,
            'name': distributor.name,
            'photo': distributor.photo.url if distributor.photo else None,
            'inn': distributor.inn,
            'region': distributor.region,
            'contact': distributor.contact,
            'contact2': distributor.contact2 if distributor.contact2 else None,

        }
        return representation