# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-21 00:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('w_num', models.CharField(max_length=9)),
                ('in_time', models.TimeField()),
                ('out_time', models.TimeField()),
            ],
        ),
    ]
