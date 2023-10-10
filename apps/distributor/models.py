from django.db import models


REGION_CHOICES = (
    ('Баткен', 'Баткен'),
    ('Джалал-Абад', 'Джалал-Абад'),
    ('Иссык-Куль', 'Иссык-Куль'),
    ('Нарын', 'Нарын'),
    ('Ош', 'Ош'),
    ('Талас', 'Талас'),
    ('Чуй', 'Чуй'),
)

class Distributor(models.Model):
    photo = models.ImageField(
        upload_to='media/distributor_images/',
        blank=False,
        null=False,
        verbose_name='Фотография'
    )
    name = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        verbose_name='ФИО',
    )
    region = models.CharField(
        choices=REGION_CHOICES,

        max_length=150,

        blank=False,
        null=False,
        verbose_name='Регион'
    )
    inn = models.IntegerField(
        blank=False,
        unique=True,
        null=False,
        verbose_name='ИНН'
    )
    address = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        verbose_name='Адрес по прописке'
    )
    actual_place_of_residence = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        verbose_name='Фактическое место жительства'
    )
    passport_series = models.IntegerField(
        blank=False,
        null=False,
        unique=True,
        verbose_name='Серия паспорта'
    )
    passport_id = models.IntegerField(
        blank=False,
        null=False,
        verbose_name='Номер паспорта'
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
    contact1 = models.IntegerField(
        null=False,
        blank=False,
        verbose_name='Контактный номер один'
    )
    contact2 = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Контактный номер два'
    )
    is_archived = models.BooleanField(
        default=False,
        verbose_name='В архив'
    )
