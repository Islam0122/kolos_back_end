from django.db import models


class Unit(models.TextChoices):
    """Ед.измерения"""
    ITEM = 'item', 'шт'
    KILOGRAM = 'kilogram', 'кг'
    LITER = 'liter', 'литр'



class State(models.TextChoices):
    """Состояние товара"""
    normalL = 'normal', 'норма'
    defect = 'defect', 'брак'


