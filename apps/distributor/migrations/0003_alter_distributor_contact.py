# Generated by Django 4.2.6 on 2023-11-13 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributor', '0002_remove_distributor_contact1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distributor',
            name='contact',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Контактный номер'),
        ),
    ]
