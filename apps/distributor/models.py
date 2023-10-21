from django.db import models

from django.utils.translation import gettext_lazy as _

# Choices должны быть в отдельном модуле 'choices.py' или по крайне мере в одном классе
REGION_CHOICES = (
    ('Баткен', 'Баткен'),
    ('Джалал-Абад', 'Джалал-Абад'),
    ('Иссык-Куль', 'Иссык-Куль'),
    ('Нарын', 'Нарын'),
    ('Ош', 'Ош'),
    ('Талас', 'Талас'),
    ('Чуй', 'Чуй'),
)


# Создал модель контакт для примера
# class Contact(models.Model):
#     distributor = models.ForeignKey('Distributor', on_delete=models.CASCADE)


class Distributor(models.Model):
    """В verbose_name желательно использовать from django.utils.translation import gettext_lazy, для многоязычности и
    для масштабируемости проекта в дальнейшем """
    photo = models.ImageField(
        upload_to='media/distributor_images/',
        blank=False,
        null=False,
        verbose_name=_('Фотография')
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
    # адрес, фактическое место жит., серия, номер паспорта
    # и в целом все что связанно с приватными данными
    # должно храниться в отдельной модельке и иметь связь(OneToOneField)
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

    # необходимо создать отдельную модель контакта со связью ForeignKey к модели Distributor

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Дистрибьютор"
        verbose_name_plural = "Дистрибьюторы"


# Это пример получения списка контактов дистрибутора



# поля одинаковы с моделькой дистрибутор поэтому можно просто наследоваться от него
class ArchiveDistributor(models.Model):
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
        # default='Unknown',
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

    # actual_place_of_residence = models.CharField(
    #     max_length=255,
    #     default='Unknown'
    # )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Архивированный Дистрибьютор"
        verbose_name_plural = "Архивированные Дистрибьюторы"

# class ArchivedObject(models.Model):
#     original_object = models.ForeignKey(Distributor, on_delete=models.CASCADE)
#     archived_at = models.DateTimeField(auto_now_add=True)
