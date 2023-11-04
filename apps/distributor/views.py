from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from . import models as dis_m
from . import serializers as ser

class DistributorViewSet(ModelViewSet):
    queryset = dis_m.Distributor.objects.filter(is_archived=False)
    serializer_class = ser.DistributorSerializer
    lookup_field = 'pk'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_archived = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ArchivedDistributorView(ModelViewSet):
    queryset = dis_m.Distributor.objects.filter(is_archived=True)
    serializer_class = ser.DistributorSerializer
    lookup_field = 'pk'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_archived = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)






