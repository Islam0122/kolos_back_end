from django.core.validators import MinValueValidator
from django.db import models, transaction
from django.utils.translation import gettext_lazy as _
from product import choices
from product.models import ProductNormal, ProductDefect
from django.db.models import F


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
        return f"Прод-я позиция: -> {self.product.name} "


    class Meta:
        verbose_name = _('Проданная позиция')
        verbose_name_plural = _('Проданные позиции')


class ReturnInvoice(models.Model):
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

    invoice_item = models.ForeignKey(
        'transaction.InvoiceItems',
        on_delete=models.CASCADE,
        verbose_name='Товар из накладной продажи'
    )

    def save(self, *args, **kwargs):
        product_normal = self.invoice_item.product

        with transaction.atomic():
            try:
                invoice_item = self.invoice_item
            except InvoiceItems.DoesNotExist:
                raise ValueError("Товар не найден в истории продаж.")

            if self.state == choices.State.DEFECT:
                defect_item, created = ProductDefect.objects.get_or_create(
                    product=product_normal,
                    defaults={'quantity': self.quantity}
                )

                if not created:
                    defect_item.quantity += self.quantity
                    defect_item.save()
                product_normal.state = choices.State.DEFECT
                product_normal.save()

            else:
                # Увеличиваем количество на основном складе
                ProductNormal.objects.filter(
                    identification_number=product_normal.identification_number
                ).update(
                    quantity=F('quantity') + self.quantity
                )

                # Уменьшаем количество в истории продаж
                invoice_item = self.invoice_item
                invoice_item.quantity -= self.quantity

                # Используем F-объект для избежания race condition при обновлении поля
            InvoiceItems.objects.filter(pk=invoice_item.pk).update(
                quantity=F('quantity') - self.quantity
            )

        super().save(*args, **kwargs)

    def total_price(self):
        return self.invoice_item.product.price * self.quantity

    def __str__(self):
        return f"Возв-я позиция: -> {self.invoice_item.product.name} "

    class Meta:
        verbose_name = _('Возвращенная  позиция')
        verbose_name_plural = _('Возвращенные позиции')