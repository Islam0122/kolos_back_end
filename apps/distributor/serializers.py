from rest_framework import serializers
from .models import Distributor

class DistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distributor
        fields = '__all__'


class DistributorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distributor
        fields = ('id', 'name', 'region')


