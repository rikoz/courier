# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 14:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20170830_1355'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statusdetail',
            old_name='id',
            new_name='det_id',
        ),
    ]
