# Generated by Django 5.0.4 on 2024-04-06 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("faltas", "0002_dadosexcel_menssagem_faltas_aluno_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="dadosexcel", name="processado_recentemente",
        ),
    ]
