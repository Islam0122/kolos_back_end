# Generated by Django 4.2.7 on 2023-11-07 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_category_container_productitem_container_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=40, verbose_name='Категория'),
        ),
    ]
