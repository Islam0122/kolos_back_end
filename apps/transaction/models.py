from django.core.validators import MinValueValidator
from django.db import models


class InvoiceItems(models.Model):

    product = models.ForeignKey('product.Product',
                                max_length=200,
                                verbose_name='Товар из накладной',
                                on_delete=models.CASCADE,
                                )
    quantity = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        verbose_name='Количество'
    )
    invoice = models.ForeignKey('transaction.Invoice', related_name='order_product', on_delete=models.CASCADE,
                                verbose_name='Накладная')

    def save(self, *args, **kwargs):
        if self.product and self.quantity > 0:
            if self.product.quantity >= self.quantity:
                self.product.quantity -= self.quantity
                self.product.save()
                super().save(*args, **kwargs)
            else:
                raise ValueError(f"Недостаточно товара {self.product.name} на складе.")
        else:
            raise ValueError("Неверные данные для создания позиции заказа.")

    def total_price(self):
        return self.product.price * self.quantity


class Invoice(models.Model):

    identification_number_invoice = models.CharField(max_length=128, null=False, blank=False, verbose_name='Номер накладной')
    distributor = models.ForeignKey(
        'distributor.Distributor',
        on_delete=models.CASCADE,
        related_name='distrib_invoice',
        verbose_name='дистрибьютор'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания накладной")

    def __str__(self):
        return f"Invoice {self.id} "





