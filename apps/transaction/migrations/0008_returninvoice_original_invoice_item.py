# Generated by Django 4.2.6 on 2023-12-02 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0007_alter_returninvoice_return_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='returninvoice',
            name='original_invoice_item',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='return_item', to='transaction.invoiceitems', verbose_name='Проданная позиция'),
        ),
    ]