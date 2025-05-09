# Generated by Django 5.2 on 2025-05-02 02:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Alerta', '0002_remove_alertaresultado_alerta_ptr_and_more'),
        ('AlertaDiagnostico', '0001_initial'),
        ('Resultado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlertaResultado',
            fields=[
                ('alerta_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Alerta.alerta')),
                ('alerta_precedente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alertas_resultado', to='AlertaDiagnostico.alertadiagnostico')),
                ('resultado', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Resultado.resultado')),
            ],
            bases=('Alerta.alerta',),
        ),
    ]
