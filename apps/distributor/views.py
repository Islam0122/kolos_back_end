from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from . import models as dis_m

from . import serializers as ser


class DistributorViewSet(ModelViewSet):  # GET/PUT/DELETE/CREATE/POST
    queryset = dis_m.Distributor.objects.filter(is_archived=False)
    serializer_class = ser.DistributorSerializers
    lookup_field = 'pk'


class ArchivedDistributorView(ModelViewSet):
    queryset = dis_m.Distributor.objects.filter(is_archived=True)
    serializer_class = ser.DistributorSerializers
    lookup_field = 'pk'
