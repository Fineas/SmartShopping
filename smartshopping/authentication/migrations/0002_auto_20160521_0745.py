# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-21 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='cod',
        ),
        migrations.AlterField(
            model_name='account',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
