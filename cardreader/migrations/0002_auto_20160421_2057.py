# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-22 03:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardreader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='out_time',
            field=models.TimeField(null=True),
        ),
    ]