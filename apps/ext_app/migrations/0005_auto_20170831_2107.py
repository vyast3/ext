# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-31 21:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ext_app', '0004_auto_20170831_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='end_date',
            field=models.DateTimeField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='travel',
            name='start_date',
            field=models.DateTimeField(blank=True, default='', null=True),
        ),
    ]
