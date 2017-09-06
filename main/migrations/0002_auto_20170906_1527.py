# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 15:27
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('district', models.CharField(max_length=255)),
                ('gid', models.IntegerField(primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('city', models.CharField(max_length=255, null=True)),
                ('party', models.CharField(max_length=255, null=True)),
                ('chamber', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unionvote', models.BooleanField()),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hvote', to='main.Bill')),
            ],
        ),
        migrations.RemoveField(
            model_name='housedistrict',
            name='incumbent',
        ),
        migrations.RemoveField(
            model_name='housemember',
            name='incumbent',
        ),
        migrations.RemoveField(
            model_name='housevote',
            name='bill',
        ),
        migrations.RemoveField(
            model_name='housevote',
            name='housemember',
        ),
        migrations.RemoveField(
            model_name='senatedistrict',
            name='incumbent',
        ),
        migrations.RemoveField(
            model_name='senatevote',
            name='bill',
        ),
        migrations.RemoveField(
            model_name='senatevote',
            name='senatemember',
        ),
        migrations.AddField(
            model_name='politician',
            name='chamber',
            field=models.CharField(default='h', max_length=255),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='HouseDistrict',
        ),
        migrations.DeleteModel(
            name='HouseMember',
        ),
        migrations.DeleteModel(
            name='HouseVote',
        ),
        migrations.DeleteModel(
            name='SenateDistrict',
        ),
        migrations.DeleteModel(
            name='SenateVote',
        ),
        migrations.AddField(
            model_name='vote',
            name='politician',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Politician'),
        ),
        migrations.AddField(
            model_name='district',
            name='incumbent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='district', to='main.Politician'),
        ),
    ]