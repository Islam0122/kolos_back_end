# Generated by Django 4.2.6 on 2023-11-26 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributor', '0009_alter_distributor_passport_series_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='distributor',
            name='passport_id',
        ),
        migrations.RemoveField(
            model_name='distributor',
            name='passport_series',
        ),
        migrations.AddField(
            model_name='distributor',
            name='passport_series_number',
            field=models.CharField(default=1, max_length=100, unique=True, verbose_name='Серия, номер паспорта'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='distributor',
            name='address',
            field=models.CharField(max_length=250, verbose_name='Адрес по прописке'),
        ),
        migrations.AlterField(
            model_name='distributor',
            name='contact',
            field=models.CharField(max_length=100, verbose_name='Контактный номер'),
        ),
        migrations.AlterField(
            model_name='distributor',
            name='contact2',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Второй контактный номер'),
        ),
        migrations.AlterField(
            model_name='distributor',
            name='inn',
            field=models.CharField(max_length=20, unique=True, verbose_name='ИНН'),
        ),
    ]
