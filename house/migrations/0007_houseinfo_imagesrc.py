# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-28 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0006_remove_houseinfo_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='houseinfo',
            name='imagesrc',
            field=models.CharField(blank=True, default='../media/media/None/Dva.png', max_length=1000, null=True),
        ),
    ]