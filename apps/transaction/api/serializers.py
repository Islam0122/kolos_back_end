from rest_framework import serializers
from transaction import models as m


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Order
        fields = '__all__'

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
