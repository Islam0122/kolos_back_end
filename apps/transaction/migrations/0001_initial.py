# Generated by Django 4.2.6 on 2023-11-10 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('distributor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfer_date', models.DateTimeField(auto_now_add=True)),
                ('returned', models.BooleanField(default=False)),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distributor.distributor')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='DistributorProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfer_date', models.DateTimeField(auto_now_add=True)),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distributor.distributor')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
