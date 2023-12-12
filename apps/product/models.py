from django.db import models, transaction
from django.utils.translation import gettext_lazy as _
from . import choices
from common.models import BaseModel
from django.utils import timezone
from simple_history.models import HistoricalRecords
from django.db.models.signals import post_migrate
from django.dispatch import receiver



class Warehouse(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_('Название склада'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Склад')
        verbose_name_plural = _('Склад')

    @receiver(post_migrate)
    def create_initial_warehouses(sender, **kwargs):
        if sender.name == 'product':
            # Создание двух складов
            Warehouse.objects.get_or_create(id=1, name='normal')
            Warehouse.objects.get_or_create(id=2, name='defect')


class Category(models.Model):
    title = models.CharField(
        _('Категория'),
        max_length=40,
        primary_key=True
    )

    def __str__(self):
        return f' {self.title}'

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категория товаров')


class ProductNormal(BaseModel):
    name = models.CharField(
        _('Наименование'),
        max_length=250
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='ProductNormal',

    )
    identification_number = models.CharField(
        _('ID'),
        unique=True,
        max_length=200,

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
    )
    sum = models.IntegerField(
        _('Сумма'),
        default=0
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
    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE,
        default='1',
        related_name='normal_products',
        verbose_name=_('Склад (нормальный товар)')
    )

    history = HistoricalRecords()

    def __str__(self):
        return f'наименование: {self.name}, кол-во: {self.quantity}'

    def save(self, *args, **kwargs):
        self.sum = self.quantity * self.price
        return super().save(*args, **kwargs)

    def archived(self):
        self.is_archived = True
        self.delete_at = timezone.now()
        self.save()

    def restore(self):
        self.is_archived = False
        self.delete_at = None
        self.save()

    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Склад-Норм-Товаров')


class ProductDefect(BaseModel):
    product = models.ForeignKey(ProductNormal, on_delete=models.CASCADE, related_name='defective_products', verbose_name='Бракованный товар')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Колличество')
    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE,
        related_name='defect_products',
        default='2',
        verbose_name=_('Склад (бракованный товар)')

    )
    is_archived = models.BooleanField(
        _('Архив? '),
        default=False
    )

    history = HistoricalRecords()

    def __str__(self):
        return f"DefectiveProduct {self.product.name} (Quantity: {self.quantity}, Warehouse: {self.warehouse})"

    class Meta:
        verbose_name = _('Бракованные товары')
        verbose_name_plural = _('Бракованные товары')

    def archived(self):
        self.is_archived = True
        self.delete_at = timezone.now()
        self.save()

    def restore(self):
        self.is_archived = False
        self.delete_at = None
        self.save()