# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 12:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='status',
            old_name='status',
            new_name='name',
        ),
    ]
