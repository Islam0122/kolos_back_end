from datetime import timezone
from django.shortcuts import get_object_or_404
from rest_framework.generics import mixins
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
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


    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_archived = True
        instance.save()
        return super().update(request, *args, **kwargs)



class DistributorViewSet(viewsets.ModelViewSet):
    queryset = Distributor.objects.filter(is_archived=False)
    serializer_class = DistributorSerializer


class DistributorArchiveView(APIView):
    def post(self, request, distributor_id):
        distributor = get_object_or_404(Distributor, id=distributor_id)
        distributor.is_archived = True
        distributor.archived_date = timezone.now()
        distributor.save()
        return Response({'message': 'Distributor archived successfully'})

    def delete(self, request, distributor_id):
        distributor = get_object_or_404(Distributor, id=distributor_id)
        distributor.is_archived = False
        distributor.archived_date = None
        distributor.save()
        return Response({'message': 'Distributor unarchived successfully'})
