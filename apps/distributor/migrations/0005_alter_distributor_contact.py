# Generated by Django 4.2.6 on 2023-11-13 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributor', '0004_alter_distributor_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distributor',
            name='contact',
            field=models.IntegerField(blank=True, null=True, verbose_name='Контактный номер'),
        ),
    ]
