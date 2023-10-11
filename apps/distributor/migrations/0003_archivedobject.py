

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('distributor', '0002_alter_archivedistributor_actual_place_of_residence'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivedObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archived_at', models.DateTimeField(auto_now_add=True)),
                ('original_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distributor.distributor')),
            ],
        ),
    ]
