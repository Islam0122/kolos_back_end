# Generated by Django 4.2.6 on 2023-11-30 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0006_remove_returninvoice_original_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='returninvoice',
            name='return_date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата создания накладной возврата'),
        ),
    ]
