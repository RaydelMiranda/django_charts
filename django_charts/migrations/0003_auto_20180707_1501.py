# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-07-07 19:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_charts', '0002_auto_20180707_1500'),
    ]

    operations = [
        migrations.RenameField(
            model_name='splinechart',
            old_name='data_url',
            new_name='data_url_name',
        ),
    ]
