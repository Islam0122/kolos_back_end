# Generated by Django 4.2.6 on 2023-11-15 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_loginattempt_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LoginAttempt',
        ),
    ]
