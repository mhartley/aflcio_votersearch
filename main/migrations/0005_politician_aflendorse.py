# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-06 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20171101_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='politician',
            name='endorse',
            field=models.NullBooleanField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]