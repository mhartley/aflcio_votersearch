# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-27 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20171127_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='capture',
            name='georeturn',
            field=models.NullBooleanField(),
        ),
        migrations.AlterField(
            model_name='capture',
            name='zipcode',
            field=models.CharField(max_length=10),
        ),
    ]
