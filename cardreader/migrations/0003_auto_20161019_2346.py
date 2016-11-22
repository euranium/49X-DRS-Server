# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 23:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cardreader', '0002_auto_20160421_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='w_num',
            field=models.CharField(max_length=8),
        ),
    ]