# Generated by Django 4.2.4 on 2023-10-12 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distributor', '0004_delete_archivedobject'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archivedistributor',
            name='archived_date',
        ),
        migrations.RemoveField(
            model_name='archivedistributor',
            name='is_archived',
        ),
        migrations.RemoveField(
            model_name='distributor',
            name='archived_date',
        ),
        migrations.RemoveField(
            model_name='distributor',
            name='is_archived',
        ),
    ]
