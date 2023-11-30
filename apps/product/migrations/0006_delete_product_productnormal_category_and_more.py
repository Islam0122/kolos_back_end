# Generated by Django 4.2.6 on 2023-11-29 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_productdefect_productnormal_remove_product_category'),
        ('transaction', '0012_alter_invoiceitems_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='productnormal',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProductNormal', to='product.category'),
        ),
        migrations.AddField(
            model_name='productdefect',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ProductDefect', to='product.category'),
        ),
    ]
