# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 15:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170906_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='politician',
            name='chamber',
        ),
    ]