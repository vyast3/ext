# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-31 21:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ext_app', '0003_auto_20170831_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='end_date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='travel',
            name='start_date',
            field=models.CharField(max_length=100),
        ),
    ]
