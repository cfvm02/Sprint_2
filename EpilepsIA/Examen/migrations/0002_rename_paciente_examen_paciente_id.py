# Generated by Django 5.2.1 on 2025-05-09 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Examen', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='examen',
            old_name='paciente',
            new_name='paciente_id',
        ),
    ]
