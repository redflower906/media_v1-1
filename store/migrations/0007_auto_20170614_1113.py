# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-14 15:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20170613_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='service',
        ),
        migrations.RemoveField(
            model_name='servicesubtype',
            name='service',
        ),
        migrations.DeleteModel(
            name='Job',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.DeleteModel(
            name='ServiceSubType',
        ),
    ]