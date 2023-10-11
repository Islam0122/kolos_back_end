from django.db import models

# Create your models here.
STATUS_CHOICES = (

    ('НОРМА', 'НОРМА'),
    ('брак', 'Брак'),
    ('просроченный', 'Просроченный'),
)


class Category(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Категория'
    )
    #create_data = models.DateTimeField(auto_now_add=True)

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
    ) #Категория
    identification_number = models.AutoField(
        primary_key=True, 
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
        choices=STATUS_CHOICES, 
        default='НОРМА'
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


    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class ArchiveProduct(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Наименование',
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,
        verbose_name='Категория',
    ) # Категория
    identification_number = models.AutoField(
        primary_key=True,
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
        verbose_name='Цена',
    )
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='НОРМА'
    )

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Архивированный Товар"
        verbose_name_plural = "Архивированные Товары"