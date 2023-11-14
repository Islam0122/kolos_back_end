from django.db import models
from django.utils.translation import gettext_lazy as _

from . import choices
from common.models import BaseModel


class Category(models.Model):
    title = models.CharField(
        _('Категория'),
         max_length=40,
         primary_key=True
                             )
    def __str__(self):
        return f' {self.title}'



class Product(BaseModel):
    name = models.CharField(
        _('Наименование'),
        max_length=120
    )
    category= models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',

    )
    identification_number = models.CharField(
        _('ID'),
        max_length=100,

    )
    unit = models.CharField(
        _('Ед.измерения'),
        max_length=8,
        choices=choices.Unit.choices,
        default=choices.Unit.ITEM
    )

    quantity = models.IntegerField(
        _('Кол-во'),
        default=1
    )
    price =models.IntegerField(
        _('Цена'),
    )
    sum = models.IntegerField(
        _('Сумма'),
        default= 0
    )
    state = models.CharField(
        _('Состояние'),
        max_length=20,
        choices=choices.State.choices,
        default=choices.State.NORMAL
    )

    is_archived = models.BooleanField(
        _('Архив? '),
        default=False
    )

    def __str__(self):
        return f'наименование: {self.name}, кол-во: {self.quantity}'


    def save(self, *args, **kwargs):
        self.sum = self.quantity * self.price
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')
