from rest_framework.viewsets import ModelViewSet

from apps.distributor import models as dis_m

from apps.distributor import serializers as ser


class DistributorViewSet(ModelViewSet):  # GET/PUT/DELETE/CREATE/POST
    queryset = dis_m.Distributor.objects.filter(is_archived=False)
    serializer_class = ser.DistributorSerializer
    lookup_field = 'pk'


class ArchivedDistributorView(ModelViewSet):
    queryset = dis_m.Distributor.objects.filter(is_archived=True)
    serializer_class = ser.DistributorSerializer
    lookup_field = 'pk'
