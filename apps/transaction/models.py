from django.db import models

from distributor.models import Distributor
from product.models import Product


class Order(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='order_product',
    )
    distributor = models.ForeignKey(
        Distributor,
        on_delete=models.CASCADE,
        related_name='order_distributor',
    )
    quantity = models.IntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f'Накладная №: {self.product.product.name}'

    def save(self, *args, **kwargs):
        if self.product and self.quantity > 0:
            if self.product.quantity >= self.quantity:
                self.product.quantity -= self.quantity
                self.product.save()
                super().save(*args, **kwargs)
            else:
                raise ValueError(f"Недостаточно товара {self.product.product.name} на складе.")
        else:
            raise ValueError("Неверные данные для создания позиции заказа.")
