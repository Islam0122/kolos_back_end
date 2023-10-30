from django.db import models


class Unit(models.TextChoices):
    """Ед.измерения"""
    ITEM = 'item', 'шт'
    KILOGRAM = 'kilogram', 'кг'
    LITER = 'liter', 'литр'
    M = 'm', 'м'  # узнать что такое ед.измеренения 'м' и при надобности заменить переменную.


class Category(models.TextChoices):
    """Категории"""
    ALCOHOL = 'alcohol', 'Алгокольный'
    NOT_ALCOHOL = 'Безалкогольный', 'Безалкогольный'


class State(models.TextChoices):
    """Состояние товара"""
    NORMAL = 'Normal', 'Норма'
    INVALID = 'Invalid', 'Брак'
