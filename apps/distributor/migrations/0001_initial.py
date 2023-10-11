

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArchiveDistributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='media/distributor_images/', verbose_name='Фотография')),
                ('name', models.CharField(max_length=50, verbose_name='ФИО')),
                ('region', models.CharField(choices=[('Баткен', 'Баткен'), ('Джалал-Абад', 'Джалал-Абад'), ('Иссык-Куль', 'Иссык-Куль'), ('Нарын', 'Нарын'), ('Ош', 'Ош'), ('Талас', 'Талас'), ('Чуй', 'Чуй')], max_length=150, verbose_name='Регион')),
                ('inn', models.IntegerField(unique=True, verbose_name='ИНН')),
                ('address', models.CharField(max_length=150, verbose_name='Адрес по прописке')),
                ('passport_series', models.IntegerField(unique=True, verbose_name='Серия паспорта')),
                ('passport_id', models.IntegerField(verbose_name='Номер паспорта')),
                ('issued_by', models.CharField(max_length=255, verbose_name='Кем выдан')),
                ('issue_date', models.DateField(verbose_name='Дата выдачи')),
                ('validity', models.DateField(verbose_name='Срок действия')),
                ('contact1', models.IntegerField(verbose_name='Контактный номер один')),
                ('contact2', models.IntegerField(blank=True, null=True, verbose_name='Контактный номер два')),
                ('is_archived', models.BooleanField(default=False, verbose_name='В архив')),
                ('archived_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата архивации')),
                ('actual_place_of_residence', models.CharField(default='Unknown', max_length=255)),
            ],
            options={
                'verbose_name': 'Архивированный Дистрибьютор',
                'verbose_name_plural': 'Архивированные Дистрибьюторы',
            },
        ),
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
                ('contact1', models.IntegerField(verbose_name='Контактный номер один')),
                ('contact2', models.IntegerField(blank=True, null=True, verbose_name='Контактный номер два')),
                ('is_archived', models.BooleanField(default=False, verbose_name='В архив')),
                ('archived_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата архивации')),
            ],
            options={
                'verbose_name': 'Дистрибьютор',
                'verbose_name_plural': 'Дистрибьюторы',
            },
        ),
    ]