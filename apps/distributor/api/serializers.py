from rest_framework import serializers
from distributor.models import Distributor


class DistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distributor
        fields = ['id', 'photo', 'name', 'region', 'inn', 'address',
                  'actual_place_of_residence', 'passport_series_number',
                  'issued_by', 'issue_date', 'validity', 'contact', 'contact2', 'delete_at']
