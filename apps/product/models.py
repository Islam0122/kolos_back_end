from django.db import models
from django.utils.translation import gettext_lazy as _

from . import choices
from common.models import BaseModel

class Category(models.Model):
    title = models.CharField(
        _('Категория'),
        max_length=40
        )
    def __str__(self):
        return f' {self.title}'





class AbstarctProduct(BaseModel):
    name = models.CharField(
        _('Наименование'),
        max_length=120
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',

    )
    identification_number = models.CharField(
        _('ID'),
        max_length=100,

    )

    def __str__(self):
        return f' {self.name}'



class Product(models.Model):
    product = models.ForeignKey(
        AbstarctProduct,
        on_delete=models.CASCADE,
        related_name='products',

    )
    quantity = models.IntegerField(
        _('Кол-во'),
        default=1
    )
    unit = models.CharField(
        _('Ед.измерения'),
        max_length=8,
        choices=choices.Unit.choices,
        default=choices.Unit.ITEM
    )
    price =models.IntegerField(
        _('Цена'),
    )
    state = models.CharField(
        _('Состояние'),
        max_length=20,
        choices=choices.State.choices,
        default=choices.State.normalL
    )

    is_archived = models.BooleanField(
        _('Архив? '),
        default=False
    )
    sum = models.IntegerField(
        _('Сумма'),
        default=0
    )
    def save(self, *args, **kwargs):
        self.sum = self.quantity * self.price
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'наименование: {self.product.name}, кол-во: {self.quantity}'



    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')
