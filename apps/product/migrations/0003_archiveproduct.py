

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchiveProduct',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('identification_number', models.AutoField(primary_key=True, serialize=False)),
                ('unit_of_measurement', models.CharField(default='литр', max_length=10)),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('НОРМА', 'НОРМА'), ('брак', 'Брак'), ('просроченный', 'Просроченный')], default='НОРМА', max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
        ),
    ]