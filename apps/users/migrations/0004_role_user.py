

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, unique=True)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.role')),
            ],
        ),
    ]
