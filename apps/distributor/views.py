from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Distributor
from .serializers import DistributorSerializer



# Create your views here.
class DistributorView(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):

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


