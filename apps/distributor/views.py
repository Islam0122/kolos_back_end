<<<<<<< HEAD
from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

=======
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
>>>>>>> 96926b2519640b01f8190961ecc35c88dd3b12c5
from .models import Distributor
from .serializers import DistributorSerializer, ArchivedDistributorSerializer



# Create your views here.
class DistributorView(viewsets.ModelViewSet):

    queryset = Distributor.objects.filter(is_archived=False)
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


<<<<<<< HEAD
=======
class ArchivedDistributorListView(ListAPIView):
    queryset = Distributor.objects.filter(is_archived=True)
    serializer_class = ArchivedDistributorSerializer
>>>>>>> 96926b2519640b01f8190961ecc35c88dd3b12c5
