# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-28 18:59
from __future__ import unicode_literals

from django.db import migrations, models
import house.models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0004_auto_20160728_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houseinfo',
            name='pic',
            field=models.CharField(blank=True, default=house.models.upload_location, max_length=1000, null=True),
        ),
    ]
