from django.core.validators import MinValueValidator
from django.db import models
from distributor.models import Distributor
from product.models import Product


class Invoice(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product_invoice',
    )
    distributor = models.ForeignKey(
        Distributor,
        on_delete=models.CASCADE,
        related_name='distrib_invoice',
    )
    quantity = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        verbose_name='Колличество'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата добавления")

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f'Накладная №: {self.product.name}'

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
