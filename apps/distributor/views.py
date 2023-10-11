


from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

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



class ArchivedDistributorListView(ListAPIView):
    queryset = Distributor.objects.filter(is_archived=True)
    serializer_class = ArchivedDistributorSerializer

