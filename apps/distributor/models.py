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
        blank=False,
        null=False,
        verbose_name='Фотография'
    )
    full_name = models.CharField(
        max_length=100,
        verbose_name='ФИО',
    )
    region = models.CharField(
        choices=REGION_CHOICES,
        max_length=50,
        blank=False,
        null=False,
        verbose_name='Регион'
    )
    inn = models.IntegerField(
        unique=True,
        verbose_name='ИНН'
    )
    address = models.CharField(
        max_length=250,
        verbose_name='Адрес по прописке'
    )
    actual_address = models.CharField(
        max_length=250,
        verbose_name='Фактическое место жительства'
    )
    passport_series = models.CharField(
        max_length=2,
        verbose_name='Серия паспорта'
    )
    passport_id = models.IntegerField(
        unique=True,
        verbose_name='Номер паспорта'
    )
    issued_by = models.CharField(
        max_length=50,
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
        verbose_name='Срок действия' #надо сделать выбор даты
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

    def __str__(self):
        return self.full_name
