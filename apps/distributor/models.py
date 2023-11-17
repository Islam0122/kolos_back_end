from django.db import models
from django.utils.translation import gettext_lazy as _
import phonenumbers

from . import choices


# Создал модель контакт для примера
# class Contact(models.Model):
#     distributor = models.ForeignKey('Distributor', on_delete=models.CASCADE)
#     phone_number = models.CharField(
#         max_length=15,
#         blank=True,
#         null=True,
#         verbose_name=_("Contact Phone")
#     )



class Distributor(models.Model):
    """В verbose_name желательно использовать from django.utils.translation import gettext_lazy, для многоязычности и
    для масштабируемости проекта в дальнейшем """
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
        verbose_name='ФИО',
    )
    region = models.CharField(
        choices=choices.REGION_CHOICES,
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
    passport_series = models.CharField(
        default='id',
        max_length=4,
        blank=False,
        null=False,
        # unique=True,
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
    contact = models.IntegerField(blank=False,
                                  null=False,
                                  verbose_name='Контактный номер'
                                  )
    contact2 = models.IntegerField(blank=True,
                                  null=True,
                                  verbose_name='Второй контактный номер'
                                  )

    def save(self, *args, **kwargs):
        # Проверка и форматирование основного номера телефона
        if self.contact:
            parsed_number = phonenumbers.parse(str(self.contact), "KG")
            if phonenumbers.is_valid_number(parsed_number):
                self.contact = int(phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164))

        # Проверка и сохранение другого номера телефона
        if self.contact2:
            parsed_other_number = phonenumbers.parse(str(self.contact2), "KG")
            if phonenumbers.is_valid_number(parsed_other_number):
                self.contact2 = int(
                    phonenumbers.format_number(parsed_other_number, phonenumbers.PhoneNumberFormat.E164))

        super(Distributor, self).save(*args, **kwargs)
    # )
    # contact2 = models.IntegerField(
    #     null=True,
    #     blank=True,
    #     verbose_name='Контактный номер два'
    # )

    is_archived = models.BooleanField(
        default=False,
        verbose_name='В АРХИВ'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Дистрибьютор"
        verbose_name_plural = "Дистрибьюторы"
