# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-29 10:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0005_auto_20171011_0816'),
        ('sensors', '0007_auto_20171011_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='actuator',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='plants.Plant'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='sensor_type',
            field=models.CharField(choices=[('WL', 'Water Level'), ('Temp', 'Temperature'), ('SM', 'Soil Moisture'), ('HDT', 'Humidity'), ('RS', 'RainSensor')], default='Temp', max_length=20),
        ),
    ]
