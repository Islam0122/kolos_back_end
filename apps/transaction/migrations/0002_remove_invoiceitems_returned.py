# Generated by Django 4.2.6 on 2023-11-30 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoiceitems',
            name='returned',
        ),
    ]