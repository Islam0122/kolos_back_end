# Generated by Django 4.2.6 on 2023-10-23 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='media/distributor_images/', verbose_name='Фотография')),
                ('name', models.CharField(max_length=50, verbose_name='ФИО')),
                ('region', models.CharField(choices=[('Баткен', 'Баткен'), ('Джалал-Абад', 'Джалал-Абад'), ('Иссык-Куль', 'Иссык-Куль'), ('Нарын', 'Нарын'), ('Ош', 'Ош'), ('Талас', 'Талас'), ('Чуй', 'Чуй')], max_length=150, verbose_name='Регион')),
                ('inn', models.IntegerField(unique=True, verbose_name='ИНН')),
                ('address', models.CharField(max_length=150, verbose_name='Адрес по прописке')),
                ('actual_place_of_residence', models.CharField(max_length=255, verbose_name='Фактическое место жительства')),
                ('passport_series', models.IntegerField(unique=True, verbose_name='Серия паспорта')),
                ('passport_id', models.IntegerField(verbose_name='Номер паспорта')),
                ('issued_by', models.CharField(max_length=255, verbose_name='Кем выдан')),
                ('issue_date', models.DateField(verbose_name='Дата выдачи')),
                ('validity', models.DateField(verbose_name='Срок действия')),
                ('is_archived', models.BooleanField(default=False, verbose_name='В АРХИВ')),
            ],
            options={
                'verbose_name': 'Дистрибьютор',
                'verbose_name_plural': 'Дистрибьюторы',
            },
        ),
    ]
