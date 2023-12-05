from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from distributor import models as dis_m

from distributor.api import serializers as ser


class DistributorViewSet(ModelViewSet):
    queryset = dis_m.Distributor.objects.filter(is_archived=False)
    serializer_class = ser.DistributorSerializer
    lookup_field = 'pk'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # instance.is_archived = True
        instance.archived()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ArchivedDistributorView(ModelViewSet):
    queryset = dis_m.Distributor.objects.filter(is_archived=True)
    serializer_class = ser.DistributorSerializer
    lookup_field = 'pk'

    def restore(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.restore()

        return Response(status=status.HTTP_200_OK)
