from rest_framework import serializers
from apps.distributor.models import Distributor, ArchiveDistributor


# Ребят плз, умоляю, прошу, молю используйте ChatGPT по назначению или хотя бы не палитесь
# Че по коду: не используйте
# в переменных fields значение __all__ такая практика может вызвать непредвиденные ошибки в коде

class DistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distributor  # Replace 'A' with the correct model name
        fields = '__all__'


# не нужно создавать проблему с переизбыточностью кода, создайте масштабируемый ModelSerializer
class DistributorValidateSerializer(serializers.Serializer):
    photo = serializers.ImageField()
    name = serializers.CharField()
    region = serializers.CharField()
    inn = serializers.IntegerField()
    address = serializers.CharField()
    actual_place_of_residence = serializers.CharField()
    passport_series = serializers.CharField()
    passport_id = serializers.IntegerField()
    issued_by = serializers.CharField()
    issue_date = serializers.DateField()
    validity = serializers.DateField()
    contact1 = serializers.IntegerField()
    contact2 = serializers.IntegerField(required=False)


# в переменных fields значение __all__ такая практика может вызвать непредвиденные ошибки в коде
class ArchivedDistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchiveDistributor  # Replace 'A' with the correct model name
        fields = '__all__'
