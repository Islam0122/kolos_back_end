import random

from product import models as prod_mod, choices

products = ['Пиво', 'Кега', 'Вино', 'квас', 'Хер его какой напиток'] * 100


def product_seeder():
    prod_mod.ProductItem.objects.all().delete()
    for product in products:
        prod_mod.ProductItem.objects.create(
            name=product,
            identification_number=random.randint(1, 1000),
            unit=choices.Unit.LITER,
            quantity=15,
            price=random.randint(1, 10),
            category=choices.Category.ALCOHOL,
            state=choices.State.NORMAL,
            is_archived=False,
        )




def seed():
    print('Сидер запущен епта')
    product_seeder()
