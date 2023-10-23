from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.viewsets import ModelViewSet

from distributor import models as dis_m

from distributor.api import serializers as ser


class DistributorViewSet(ModelViewSet):  # GET/PUT/DELETE/CREATE/POST
    queryset = dis_m.Distributor.objects.all()
    serializer_class = ser.DistributorSerializer
    lookup_field = 'pk'
    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = ser.DistributorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Ребят это очень плохая практика, создайте ModelSerializer и
        # укажите здесь вместо этого нагромождения кода
        # seralizer.save() и не ломайте себе мозги
        distributor = dis_m.Distributor.objects.create(
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

        return Response(data=ser.DistributorValidateSerializer(distributor, many=False).data,
                        status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # Модель ArchiveDistributor не имеет смысла,
        # добавьте просто в обычный Distributor поле 'is_archive'
        # которое
        # будет по умолчанию false а при destroy true
        archive_distributor = dis_m.ArchiveDistributor(
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


class ArchivedDistributorView(ModelViewSet):
    queryset = dis_m.ArchiveDistributor.objects.all()
    serializer_class = ser.ArchivedDistributorSerializer
    lookup_field = 'pk'

    def restore(self, request, pk):
        archive_distributor = dis_m.ArchiveDistributor.objects.get(pk=pk)
        # Модель ArchiveDistributor не имеет смысла,
        # добавьте просто в обычный Distributor поле 'is_archive'
        # которое
        # будет True а при restore false

        new_distributor = dis_m.Distributor(
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
        return Response(data=ser.DistributorSerializer(new_distributor).data, status=status.HTTP_201_CREATED)
