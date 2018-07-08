# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-07-07 20:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_charts', '0004_auto_20180707_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='splinechart',
            name='x_axis_extra_options',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='X axis extra_options'),
        ),
        migrations.AddField(
            model_name='splinechart',
            name='x_axis_format',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='X axis format'),
        ),
        migrations.AddField(
            model_name='splinechart',
            name='x_axis_preix',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='X axis preix'),
        ),
        migrations.AddField(
            model_name='splinechart',
            name='x_axis_suffix',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='X axis suffix'),
        ),
        migrations.AddField(
            model_name='splinechart',
            name='x_axis_title',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='X axis title'),
        ),
        migrations.AddField(
            model_name='splinechart',
            name='x_data_format',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='X data format'),
        ),
        migrations.AddField(
            model_name='splinechart',
            name='y_axis_extra_options',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Y axis extra_options'),
        ),
        migrations.AddField(
            model_name='splinechart',
            name='y_axis_format',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Y axis format'),
        ),
        migrations.AddField(
            model_name='splinechart',
            name='y_axis_preix',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Y axis preix'),
        ),
        migrations.AddField(
            model_name='splinechart',
            name='y_axis_suffix',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Y axis suffix'),
        ),
        migrations.AddField(
            model_name='splinechart',
            name='y_axis_title',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Y axis title'),
        ),
        migrations.AddField(
            model_name='splinechart',
            name='y_data_format',
            field=models.CharField(blank=True, max_length=16, null=True, verbose_name='Y data format'),
        ),
    ]