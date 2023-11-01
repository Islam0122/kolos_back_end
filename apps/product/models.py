from django.db import models
from django.utils.translation import gettext_lazy as _

from . import choices
from common.models import BaseModel


class AbstractProduct(BaseModel):
    name = models.CharField(
        _('Наименование'),
        max_length=120
    )
    category = models.CharField(
        _('Категория'),
        max_length=40,
        choices=choices.Category.choices,
        default=choices.Category.ALCOHOL
    )
    unit = models.CharField(
        _('Ед.измерения'),
        max_length=8,
        choices=choices.Unit.choices,
        default=choices.Unit.ITEM
    )

    def __str__(self):
        return f'наименование товара: {self.name}, категория: {self.category}'


class ProductItem(BaseModel):
    product = models.ForeignKey(
        AbstractProduct,
        on_delete=models.CASCADE,
        related_name='product',
        verbose_name='Продукт'
    )
    identification_number = models.CharField(
        _('ID'),
        max_length=100,
        unique=True
    )
    quantity = models.IntegerField(
        _('Кол-во'),
        default=1
    )
    price = models.IntegerField(
        _('Цена'),
    )  # сделайте IntegerField price
    sum = models.IntegerField(
        _('Сумма'),
        default=0
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

    def __str__(self):
        return f'наименование: {self.product}, кол-во: {self.quantity}'

    def save(self, *args, **kwargs):
        self.sum = self.quantity * self.price
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')
