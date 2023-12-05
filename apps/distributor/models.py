from common.models import BaseModel
from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords
from django.utils.translation import gettext_lazy as _


class Distributor(BaseModel):
    photo = models.ImageField(
        upload_to='media/distributor_images/',
        blank=True,
        null=True,
        verbose_name=_('Фотография')
    )
    name = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        verbose_name=_('ФИО'),
    )
    region = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        verbose_name=_('Регион')
    )
    inn = models.CharField(
        max_length=20,
        blank=False,
        unique=True,
        null=False,
        verbose_name=_('ИНН')
    )
    address = models.CharField(
        max_length=250,
        blank=False,
        null=False,
        verbose_name=_('Адрес по прописке')
    )
    actual_place_of_residence = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name=_('Фактическое место жительства')
    )
    passport_series_number = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        unique=True,
        verbose_name='Серия, номер паспорта'
    )
    issued_by = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Кем выдан'
    )
    issue_date = models.DateField(
        null=False,
        blank=False,
        verbose_name='Дата выдачи'
    )
    validity = models.DateField(
        null=False,
        blank=False,
        verbose_name='Срок действия'
    )
    contact = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name='Контактный номер'
    )
    contact2 = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Второй контактный номер'
    )
    is_archived = models.BooleanField(
        default=False,
        verbose_name='В АРХИВ'
    )

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Дистрибьютор"
        verbose_name_plural = "Дистрибьюторы"

    def archived(self):
        self.is_archived = True
        self.delete_at = timezone.now()
        self.save()

    def restore(self):
        self.is_archived = False
        self.delete_at = None
        self.save()