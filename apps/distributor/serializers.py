from rest_framework import serializers
from .models import Distributor, ArchiveDistributor

class DistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distributor  # Replace 'A' with the correct model name
        fields = '__all__'
class DistributorValidateSerializer(serializers.Serializer):
    photo = serializers.ImageField()
    name = serializers.CharField()
    region = serializers.CharField()
    inn = serializers.IntegerField()
    address = serializers.CharField()
    actual_place_of_residence = serializers.CharField()
    passport_series = serializers.CharField()
    passport_id = serializers.IntegerField()
    issued_by = serializers.CharField()
    issue_date = serializers.DateField()
    validity = serializers.DateField()
    contact1 = serializers.IntegerField()
    contact2 = serializers.IntegerField(required=False)

class ArchivedDistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchiveDistributor  # Replace 'A' with the correct model name
        fields = '__all__'