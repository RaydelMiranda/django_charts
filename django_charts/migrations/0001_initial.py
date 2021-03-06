# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-07-07 18:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SPLineChart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('code', models.CharField(max_length=100, unique=True, verbose_name='Code')),
                ('type', models.IntegerField(choices=[(1, 'pie'), (2, 'spline')], verbose_name='Type')),
                ('data_url', models.URLField(help_text='Url from we will get data.', verbose_name='Data URL')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
