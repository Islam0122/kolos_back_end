from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from . import models as dis_m

from . import serializers as ser


class DistributorViewSet(ModelViewSet):  # GET/PUT/DELETE/CREATE/POST
    queryset = dis_m.Distributor.objects.filter(is_archived=False)
    serializer_class = ser.DistributorSerializer
    lookup_field = 'pk'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_archived = True
        instance.save()
        Response(status=status.HTTP_200_OK)


class ArchivedDistributorView(ModelViewSet):
    queryset = dis_m.Distributor.objects.filter(is_archived=True)
    serializer_class = ser.DistributorSerializer
    lookup_field = 'pk'

    def restore(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_archived = False
        instance.save()

        return Response(status=status.HTTP_200_OK)


