from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Distributor
from .serializers import DistributorSerializer

class DistributorViewSet(viewsets.ModelViewSet):
    queryset = Distributor.objects.all()
    serializer_class = DistributorSerializer

    @action(detail=True, methods=['post'])
    def archive(self, request, pk=None):
        distributor = self.get_object()
        distributor.is_archived = True
        distributor.save()
        return Response({'status': 'archived'})

    @action(detail=True, methods=['post'])
    def restore(self, request, pk=None):
        distributor = self.get_object()
        distributor.is_archived = False
        distributor.save()
        return Response({'status': 'restored'})
