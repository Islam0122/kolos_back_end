# Generated by Django 4.2.4 on 2023-10-11 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_archiveproduct'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='archiveproduct',
            options={'verbose_name': 'Архивированный Товар', 'verbose_name_plural': 'Архивированные Товары'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категория'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterField(
            model_name='archiveproduct',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='archiveproduct',
            name='identification_number',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Идентификационный номер'),
        ),
        migrations.AlterField(
            model_name='archiveproduct',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='archiveproduct',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='archiveproduct',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='archiveproduct',
            name='unit_of_measurement',
            field=models.CharField(default='литр', max_length=10, verbose_name='Единица измерения'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='identification_number',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Идентификационный номер'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_of_measurement',
            field=models.CharField(default='литр', max_length=10, verbose_name='Единица измерения'),
        ),
    ]
