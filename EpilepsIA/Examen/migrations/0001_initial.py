# Generated by Django 5.1.7 on 2025-03-13 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('estado', models.TextField()),
            ],
        ),
    ]
