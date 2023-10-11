from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .models import Distributor, ArchiveDistributor
from .serializers import DistributorSerializer, ArchivedDistributorSerializer



# Create your views here.
class DistributorView(viewsets.ModelViewSet):

    queryset = Distributor.objects.filter(is_archived=False)
    serializer_class = DistributorSerializer

    # @action(detail=True, methods=['post'])
    # def archive(self, request, pk=None):
    #     distributor = self.get_object()
    #     distributor.is_archived = True
    #     distributor.save()
    #     return Response({'status': 'archived'})

    @action(detail=True, methods=['post'])
    def restore(self, request, pk=None):
        distributor = self.get_object()
        distributor.is_archived = False
        distributor.save()
        return Response({'status': 'restored'})
    
    
    def destroy(self):
        archive_distributor = ArchiveDistributor(
            photo=self.photo,
            name=self.name,
            region=self.region,
            inn=self.inn,
            address=self.address,
            actual_place_of_residence=self.actual_place_of_residence,
            # Другие поля...
        )
        archive_distributor.save()

        self.is_archived = True
        self.save()

    def delete(self, *args, **kwargs):
        self.move_to_archive()


class ArchivedDistributorListView(ListAPIView):
    queryset = Distributor.objects.filter(is_archived=True)
    serializer_class = ArchivedDistributorSerializer
