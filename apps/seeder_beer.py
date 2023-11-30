# import django
# import random
# import datetime
# import faker
# from distributor.models import Distributor
# from product.models import ProductNormal, Category
#
# django.setup()
# fake = faker.Faker()
#
# distributors = ['Артур', 'Влад', 'Alex', 'Jhon', 'David']
#
# regions = ['kg', 'eu', 'ru']
#
# _category = ['Алкашка', 'винишко']
#
#
# def create_category():
#     Category.objects.all().delete()
#     for category in _category:
#         Category.objects.create(
#             title=category
#         )
#
#
#
# def create_distributor():
#     Distributor.objects.all().delete()
#     for distributor in distributors:
#         Distributor.objects.create(
#             name=distributor,
#             region=regions,
#             inn=random.randint(1, 9999999),
#             address='MKK',
#             actual_place_of_residence='Bishkek',
#             passport_series=random.randint(1, 20000000),
#             passport_id=random.randint(46464, 200000),
#             issued_by='SDDS',
#             issue_date=datetime.datetime.now(),
#             validity=datetime.datetime.now(),
#             contact1=996771478853,
#             contact2=996771478852,
#             is_archived=random.choice([True, False])
#
#         ),
#
#
# products = ['Пиво', 'Соки', 'Вино', 'водка', 'безалкогольное пиво '] * 10
#
#
# def create_product():
#     ProductNormal.objects.all().delete()
#     for product in products:
#         ProductNormal.objects.create(
#             name=product,
#             identification_number="321",
#             unit=random.choice(['шт', 'кг', 'литр']),
#             quantity=123,
#             price=23243,
#             sum=43434,
#             category=Category.objects.create(
#                 title=_category
#             ),
#             state='норма',
#             is_archived=random.choice([True, False])
#
#         )
#
#
# def seed():
#     create_product()
#     create_distributor()
