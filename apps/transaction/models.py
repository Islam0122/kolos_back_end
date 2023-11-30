from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from product import choices
from product.models import ProductNormal, ProductDefect


class Invoice(models.Model):
    identification_number_invoice = models.CharField(
        max_length=128,
        null=False, blank=False,
        verbose_name='Номер накладной продажи')
    distributor = models.ForeignKey(
        'distributor.Distributor',
        on_delete=models.CASCADE,
        related_name='distrib_invoice',
        verbose_name='дистрибьютор'
    )
    sale_date = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания накладной продажи")

    def __str__(self):
        return f"Продажа {self.id} "

    class Meta:
        verbose_name = _('Продажа')
        verbose_name_plural = _('Продажи')


class InvoiceItems(models.Model):
    product = models.ForeignKey(
        'product.ProductNormal',
        max_length=200,
        verbose_name='Товар из накладной',
        on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1)],
        verbose_name='Количество')
    invoice = models.ForeignKey(
        'transaction.Invoice',
        related_name='order_product',
        on_delete=models.CASCADE,
        verbose_name='Накладная')

    def save(self, *args, **kwargs):
        if self.product and self.quantity > 0:
            if self.product.quantity >= self.quantity:
                self.product.quantity -= self.quantity
                self.product.save()
            else:
                raise ValueError(f"Недостаточно товара {self.product.name} на складе.")

            super().save(*args, **kwargs)
        else:
            raise ValueError("Неверные данные для создания позиции заказа.")

    def total_price(self):
        return self.product.price * self.quantity


    def __str__(self):
        return f"позиция: {self.product.name} "
    class Meta:
        verbose_name = _('Проданная позиция')
        verbose_name_plural = _('Проданные позиции')


class ReturnInvoice(models.Model):
    identification_number_return = models.CharField(
        max_length=128,
        null=False, blank=False,
        verbose_name='Номер накладной возврата')
    distributor = models.ForeignKey(
        'distributor.Distributor',
        on_delete=models.CASCADE,
        related_name='distrib_return_invoice',
        verbose_name='Дистрибьютор'
    )
    return_date = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания накладной возврата")

    def __str__(self):
        return f"Возврат {self.id} "


class ReturnInvoiceItems(models.Model):
    product = models.ForeignKey(
        'product.ProductNormal',
        max_length=200,
        verbose_name='Товар из накладной возврата',
        on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        verbose_name='Количество')
    state = models.CharField(
        _('Состояние'),
        max_length=20,
        choices=choices.State.choices,
        default=choices.State.NORMAL
    )
    return_invoice = models.ForeignKey(
        ReturnInvoice,
        related_name='return_product',
        on_delete=models.CASCADE,
        verbose_name='Накладная возврата')

    def save(self, *args, **kwargs):
        # Получаем ProductNormal, к которому относится возвращаемый товар
        product_normal = self.product

        if self.state == choices.State.DEFECT:
            print('zzzz')
            # Бракованный склад
            defect_items = ProductDefect.objects.filter(identification_number=product_normal.identification_number)

            if defect_items.exists():
                defect_item = defect_items.first()
                defect_item.quantity += self.quantity
                defect_item.save()
            else:
                # Если товара нет на бракованном складе, создаем новый
                ProductDefect.objects.create(
                    name=product_normal.name,
                    category=product_normal.category,
                    identification_number=product_normal.identification_number,
                    unit=product_normal.unit,
                    quantity=self.quantity,
                    price=product_normal.price,
                    state=self.state
                )
        else:
            # Нормальный склад
            normal_items = ProductNormal.objects.filter(identification_number=product_normal.identification_number)

            if normal_items.exists():
                normal_item = normal_items.first()
                normal_item.quantity += self.quantity
                normal_item.save()
            else:
                # Если товара нет на нормальном складе, создаем новый
                ProductNormal.objects.create(
                    name=product_normal.name,
                    category=product_normal.category,
                    identification_number=product_normal.identification_number,
                    unit=product_normal.unit,
                    quantity=self.quantity,
                    price=product_normal.price,
                    state=self.state
                )

        super().save(*args, **kwargs)
    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"Возвращенная позиция: {self.product.name} "
    class Meta:
        verbose_name = _('Возвращенная  позиция')
        verbose_name_plural = _('Возвращенные позиции')