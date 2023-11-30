# Generated by Django 4.2.6 on 2023-11-30 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('title', models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категория товаров',
            },
        ),
        migrations.CreateModel(
            name='ProductNormal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='создано в: ')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='обновленно в: ')),
                ('name', models.CharField(max_length=250, verbose_name='Наименование')),
                ('identification_number', models.CharField(max_length=200, unique=True, verbose_name='ID')),
                ('unit', models.CharField(choices=[('item', 'шт'), ('kilogram', 'кг'), ('liter', 'литр')], default='item', max_length=8, verbose_name='Ед.измерения')),
                ('quantity', models.IntegerField(default=1, verbose_name='Кол-во')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('sum', models.IntegerField(default=0, verbose_name='Сумма')),
                ('state', models.CharField(choices=[('normal', 'норма'), ('defect', 'брак')], default='normal', max_length=20, verbose_name='Состояние')),
                ('is_archived', models.BooleanField(default=False, verbose_name='Архив? ')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProductNormal', to='product.category')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Склад-Норм-Товаров',
            },
        ),
        migrations.CreateModel(
            name='ProductDefect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='создано в: ')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='обновленно в: ')),
                ('name', models.CharField(max_length=250, verbose_name='Наименование')),
                ('identification_number', models.CharField(max_length=200, unique=True, verbose_name='ID')),
                ('unit', models.CharField(choices=[('item', 'шт'), ('kilogram', 'кг'), ('liter', 'литр')], default='item', max_length=8, verbose_name='Ед.измерения')),
                ('quantity', models.IntegerField(default=1, verbose_name='Кол-во')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('sum', models.IntegerField(default=0, verbose_name='Сумма')),
                ('state', models.CharField(choices=[('normal', 'норма'), ('defect', 'брак')], default='normal', max_length=20, verbose_name='Состояние')),
                ('is_archived', models.BooleanField(default=False, verbose_name='Архив? ')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProductDefect', to='product.category')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Склад-Брак-Товаров',
            },
        ),
    ]
