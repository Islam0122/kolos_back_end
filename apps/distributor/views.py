from rest_framework.generics import mixins
from rest_framework import generics
from rest_framework.viewsets import GenericViewSet
from .models import Distributor
from .serializers import DistributorSerializer, DistributorDetailSerializer


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
