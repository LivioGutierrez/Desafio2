# Generated by Django 5.0.6 on 2024-06-19 23:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desafioadl', '0002_rename_tarea_id_subtarea_tarea'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtarea',
            name='tarea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='desafioadl.tarea'),
        ),
    ]