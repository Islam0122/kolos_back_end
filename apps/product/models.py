from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    #create_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class Product(models.Model):
    STATUS_CHOICES = (

    ('НОРМА', 'НОРМА'),
    ('брак', 'Брак'),
    ('просроченный', 'Просроченный'),
    )


    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #Категория
    identification_number = models.AutoField(primary_key=True)
    unit_of_measurement = models.CharField(max_length=10 , default="литр")
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='НОРМА')
    @property
    def category_title(self):
        try:
            return self.category.title
        except:
            return None
    def __str__(self):
        return self.title