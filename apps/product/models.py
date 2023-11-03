from django.db import models
from django.utils.translation import gettext_lazy as _

from . import choices
from common.models import BaseModel


class ProductItem(BaseModel):
    name = models.CharField(
        _('Наименование'),
        max_length=120
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
    price = models.IntegerField(
        _('Цена'),
        blank=True,
        null=True
    )
    sum = models.IntegerField(
        _('Сумма'),
        default=0
    )
    category = models.CharField(
        _('Категория'),
        max_length=40,
        choices=choices.Category.choices,
        default=choices.Category.ALCOHOL
    )
    state = models.CharField(
        _('Состояние'),
        max_length=20,
        choices=choices.State.choices,
    )
    is_archived = models.BooleanField(
        _('Архив? '),
        default=False
    )

    def save(self, *args, **kwargs) -> str:
        self.sum = self.quantity * self.price
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'товар: {self.name} {self.sum}'

    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')


