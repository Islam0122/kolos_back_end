# Generated by Django 4.2.6 on 2023-11-30 15:24

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('distributor', '0010_remove_distributor_passport_id_and_more'),
        ('product', '0001_initial'),
        ('transaction', '0002_remove_invoiceitems_returned'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReturnInvoiceItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Количество')),
                ('state', models.CharField(choices=[('normal', 'норма'), ('defect', 'брак')], default='normal', max_length=20, verbose_name='Состояние')),
                ('product', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='product.productnormal', verbose_name='Товар из накладной возврата')),
            ],
            options={
                'verbose_name': 'Возвращенная  позиция',
                'verbose_name_plural': 'Возвращенные позиции',
            },
        ),
        migrations.AlterModelOptions(
            name='returninvoice',
            options={},
        ),
        migrations.RenameField(
            model_name='returninvoice',
            old_name='identification_number_invoice',
            new_name='identification_number_return',
        ),
        migrations.RenameField(
            model_name='returninvoice',
            old_name='created_at',
            new_name='return_date',
        ),
        migrations.AddField(
            model_name='returninvoice',
            name='original_invoice',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='transaction.invoice', verbose_name='Оригинальная накладная продажи'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='returninvoice',
            name='distributor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='distrib_return_invoice', to='distributor.distributor', verbose_name='Дистрибьютор'),
        ),
        migrations.DeleteModel(
            name='InvoiceItemsReturn',
        ),
        migrations.AddField(
            model_name='returninvoiceitems',
            name='return_invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='return_product', to='transaction.returninvoice', verbose_name='Накладная возврата'),
        ),
    ]
