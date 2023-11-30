from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class InvoiceItems(models.Model):
    product = models.ForeignKey('product.ProductNormal', max_length=200, verbose_name='Товар из накладной', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)], verbose_name='Количество')
    invoice = models.ForeignKey('transaction.Invoice', related_name='order_product', on_delete=models.CASCADE, verbose_name='Накладная')
    returned = models.BooleanField(default=False, verbose_name='Продана')
    sale_date = models.DateField(auto_now_add=True, verbose_name='Дата продажи')

    def save(self, *args, **kwargs):
        if self.product and self.quantity > 0:
            if self.returned:
                self.product.quantity += self.quantity  # Увеличиваем количество товара на складе при возврате
                self.product.save()
            elif self.product.quantity >= self.quantity:
                self.product.quantity -= self.quantity   # уменьшаем при отпуске
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



class Invoice(models.Model):

    identification_number_invoice = models.CharField(max_length=128, null=False, blank=False, verbose_name='Номер накладной продажи')
    distributor = models.ForeignKey(
        'distributor.Distributor',
        on_delete=models.CASCADE,
        related_name='distrib_invoice',
        verbose_name='дистрибьютор'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания накладной продажи")

    def __str__(self):
        return f"Продажа {self.id} "

    class Meta:
        verbose_name = _('Продажа')
        verbose_name_plural = _('Продажи')

class ReturnInvoice(models.Model):
    identification_number_invoice = models.CharField(max_length=128, null=False, blank=False,
                                                     verbose_name='Номер накладной возврата')
    distributor = models.ForeignKey(
        'distributor.Distributor',
        on_delete=models.CASCADE,
        related_name='distrib_invoice_return',
        verbose_name='дистрибьютор'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания накладной возврата")

    def __str__(self):
        return f"Возврат {self.id} "

    class Meta:
        verbose_name = _('Возврат')
        verbose_name_plural = _('Возвраты')


class InvoiceItemsReturn(models.Model):
    product = models.ForeignKey('transaction.InvoiceItems', max_length=200, verbose_name='Товар из накладной', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)], verbose_name='Количество')
    invoice = models.ForeignKey('transaction.Invoice', related_name='order_product_return', on_delete=models.CASCADE, verbose_name='Накладная')
    returned = models.BooleanField(default=False, verbose_name='Возвращено')
    returned_date = models.DateField(auto_now_add=True, verbose_name='Дата возврата')

    def save(self, *args, **kwargs):
        if self.product and self.quantity > 0:
            if self.returned:
                self.product.quantity += self.quantity  # Увеличиваем количество товара на складе при возврате
                self.product.save()
            elif self.product.quantity >= self.quantity:
                self.product.quantity -= self.quantity   # уменьшаем при отпуске
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
        verbose_name = _('Возвращенная  позиция')
        verbose_name_plural = _('Возвращенные позиции')