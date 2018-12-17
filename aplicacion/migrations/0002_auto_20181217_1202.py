# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-17 12:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receta',
            name='nombreM',
        ),
        migrations.AddField(
            model_name='receta',
            name='medId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacion.medico'),
        ),
        migrations.AddField(
            model_name='receta',
            name='pacId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacion.paciente'),
        ),
    ]