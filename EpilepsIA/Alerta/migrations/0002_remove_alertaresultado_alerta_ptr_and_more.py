# Generated by Django 5.1.7 on 2025-03-14 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Alerta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alertaresultado',
            name='alerta_ptr',
        ),
        migrations.DeleteModel(
            name='alertaDiagnostico',
        ),
        migrations.DeleteModel(
            name='alertaResultado',
        ),
    ]
