# Generated by Django 4.0.5 on 2023-01-06 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='id_sensor',
            new_name='sensor',
        ),
    ]