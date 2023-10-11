


from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Distributor, ArchiveDistributor

from .serializers import DistributorValidateSerializer, ArchivedDistributorSerializer, DistributorSerializer


class DistributorViewSet(ModelViewSet):  # GET/PUT/DELETE/CREATE/POST
    queryset = Distributor.objects.all()
    serializer_class =DistributorSerializer
    lookup_field = 'pk'

    def create(self, request, *args, **kwargs):
        serializer = DistributorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        distributor = Distributor.objects.create(
            photo=serializer.validated_data.get('photo'),
            name=serializer.validated_data.get('name'),
            region=serializer.validated_data.get('region'),
            inn=serializer.validated_data.get('inn'),
            address=serializer.validated_data.get('address'),
            actual_place_of_residence=serializer.validated_data.get('actual_place_of_residence'),
            passport_series=serializer.validated_data.get('passport_series'),
            passport_id=serializer.validated_data.get('passport_id'),
            issued_by=serializer.validated_data.get('issued_by'),
            issue_date=serializer.validated_data.get('issue_date'),
            validity=serializer.validated_data.get('validity'),
            contact1=serializer.validated_data.get('contact1'),
            contact2=serializer.validated_data.get('contact2'),

        )

        return Response(data=DistributorValidateSerializer(distributor, many=False).data,
                        status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        archive_distributor = ArchiveDistributor(
            photo=instance.photo,
            name=instance.name,
            region=instance.region,
            inn=instance.inn,
            address=instance.address,
            actual_place_of_residence=instance.actual_place_of_residence,  # Corrected field name
            passport_series=instance.passport_series,  # Corrected field name
            passport_id=instance.passport_id,  # Corrected field name
            issued_by=instance.issued_by,
            issue_date=instance.issue_date,  # Corrected field name
            validity=instance.validity,
            contact1=instance.contact1,
            contact2=instance.contact2
        )
        archive_distributor.save()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def restore(self, request, pk):
        archive_distributor = ArchiveDistributor.objects.get(pk=pk)

        new_distributor = Distributor(
            photo=archive_distributor.photo,
            name=archive_distributor.name,
            region=archive_distributor.region,
            inn=archive_distributor.inn,
            address=archive_distributor.address,
            actual_place_of_residence=archive_distributor.actual_place_of_residence,  # Corrected field name
            passport_series=archive_distributor.passport_series,  # Corrected field name
            passport_id=archive_distributor.passport_id,  # Corrected field name
            issued_by=archive_distributor.issued_by,
            issue_date=archive_distributor.issue_date,  # Corrected field name
            validity=archive_distributor.validity,
            contact1=archive_distributor.contact1,
            contact2=archive_distributor.contact2
        )
        new_distributor.save()
        archive_distributor.delete()
        return Response(data=DistributorSerializer(new_distributor).data, status=status.HTTP_201_CREATED)





class ArchivedDistributorListView(ListAPIView):
    queryset = Distributor.objects.filter(is_archived=True)
    serializer_class = ArchivedDistributorSerializer


