# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-28 19:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0005_auto_20160728_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='houseinfo',
            name='pic',
        ),
    ]