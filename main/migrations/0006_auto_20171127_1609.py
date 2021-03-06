# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-27 16:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_politician_aflendorse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='capture',
            name='name',
        ),
        migrations.AddField(
            model_name='capture',
            name='address',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='capture',
            name='cellphone',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='capture',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='capture',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='capture',
            name='zipcode',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]
