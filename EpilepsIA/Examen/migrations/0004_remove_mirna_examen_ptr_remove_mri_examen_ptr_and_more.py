# Generated by Django 5.1.7 on 2025-03-14 08:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Examen', '0003_alter_examen_id'),
        ('Paciente', '0001_initial'),
        ('Solicitud', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mirna',
            name='examen_ptr',
        ),
        migrations.RemoveField(
            model_name='mri',
            name='examen_ptr',
        ),
        migrations.AddField(
            model_name='examen',
            name='paciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Paciente.paciente'),
        ),
        migrations.AddField(
            model_name='examen',
            name='solicitud',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Solicitud.solicitud'),
        ),
        migrations.DeleteModel(
            name='EEG',
        ),
        migrations.DeleteModel(
            name='miRNA',
        ),
        migrations.DeleteModel(
            name='MRI',
        ),
    ]
