# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 13:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0004_auto_20170421_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='brands.Brand'),
        ),
    ]
