from django.db import models
from django.utils import timezone
from . import choices


class Category(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Категория'
    )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категория"


class Product(models.Model):

    title = models.CharField(
        max_length=200,
        verbose_name='Наименование'
    )
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 verbose_name='Категория'
                                 )  # Категория
    identification_number = models.CharField(
        max_length=100,
        verbose_name='Идентификационный номер'
    )
    unit_of_measurement = models.CharField(
        max_length=10,
        default="литр",
        verbose_name='Единица измерения'
    )
    quantity = models.IntegerField(
        default=1,
        verbose_name='Количество'
    )
    price = models.IntegerField(
        verbose_name='Цена'
    )
    status = models.CharField(
        max_length=20,
        choices=choices.STATUS_CHOICES,
        default='НОРМА'
    )
    create_date = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(
        default=False,
        verbose_name='В АРХИВ'
    )
    def total_price(self):
        # Рассчитываем сумму между ценой и количеством
        return self.price * self.quantity

    @property
    def category_title(self):
        try:
            return self.category.title
        except:
            return None

    def delete(self, using=None, keep_parents=False):
        self.is_archived = True

    def unarchive(self):
        self.is_archived = False

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"




# class ArchiveProduct(models.Model):
#     title = models.CharField(
#         max_length=200,
#         verbose_name='Наименование',
#     )
#     category = models.ForeignKey(
#         Category,
#         on_delete=models.CASCADE,
#         verbose_name='Категория',
#     )
#     identification_number = models.AutoField(
#         primary_key=True,
#         verbose_name='Идентификационный номер'
#     )
#     unit_of_measurement = models.CharField(
#         max_length=10,
#         default="литр",
#         verbose_name='Единица измерения'
#     )
#     quantity = models.IntegerField(
#         default=1,
#         verbose_name='Количество'
#     )
#     price = models.IntegerField(
#         verbose_name='Цена',
#     )
#     status = models.CharField(
#         max_length=20,
#         choices=choices.STATUS_CHOICES,
#         default='НОРМА'
#     )
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = "Архивированный Товар"
#         verbose_name_plural = "Архивированные Товары"
#
# ### Проблема такая же как в Distributor
# # 1. нагромождение моделек
# # 2. ненужное заполнение бд
# # 3. и конечно же choices
