# Generated by Django 4.2.6 on 2023-10-27 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_is_archived'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='создано в: ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='обновленно в: ')),
                ('name', models.CharField(max_length=120, verbose_name='Наименование')),
                ('identification_number', models.CharField(max_length=100, unique=True, verbose_name='ID')),
                ('unit', models.CharField(choices=[('item', 'шт'), ('kilogram', 'кг'), ('liter', 'литр'), ('m', 'м')], default='item', max_length=8, verbose_name='Ед.измерения')),
                ('quantity', models.IntegerField(default=1, verbose_name='Кол-во')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('sum', models.IntegerField(default=0, verbose_name='Сумма')),
                ('category', models.CharField(choices=[('alcohol', 'Алгокольный'), ('Безалкогольный', 'Безалкогольный')], default='alcohol', max_length=40, verbose_name='Категория')),
                ('state', models.CharField(choices=[('Normal', 'Норма'), ('Invalid', 'Брак')], max_length=20, verbose_name='Состояния')),
                ('is_archived', models.BooleanField(default=False, verbose_name='Архив? ')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
