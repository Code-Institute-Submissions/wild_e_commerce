# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 12:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0002_auto_20170428_1329'),
        ('products', '0018_auto_20170428_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='statusname',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='status.Status'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=254),
        ),
    ]
