from rest_framework import serializers
from .models import Distributor


class DistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distributor
        fields = ['id', 'photo', 'name', 'region', 'inn', 'address',
                  'actual_place_of_residence', 'passport_series', 'passport_id',
                  'issued_by', 'issue_date', 'validity', 'is_archived', 'contact1', 'contact2']
