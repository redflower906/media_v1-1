# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20170616_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='container',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]