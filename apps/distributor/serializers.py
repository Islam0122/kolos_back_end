from rest_framework import serializers
from .models import Distributor

class DistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distributor
        fields = '__all__'
class DistributorValidateSerializer(serializers.Serializer):
    photo = serializers.ImageField()
    full_name = serializers.CharField()
    region = serializers.CharField()
    inn = serializers.IntegerField()
    address = serializers.CharField()
    actual_address = serializers.CharField()
    passport_series = serializers.CharField()
    passport_id = serializers.IntegerField()
    issued_by = serializers.CharField()
    issue_date = serializers.DateField()
    validity = serializers.DateField()
    contact1 = serializers.IntegerField()
    contact2 = serializers.IntegerField(required=False)
    is_archived = serializers.BooleanField()

class DistributorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distributor
        fields = ('id', 'name', 'region')


