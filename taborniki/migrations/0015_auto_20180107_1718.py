# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-07 16:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taborniki', '0014_auto_20180107_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='akcija',
            name='organizator',
        ),
        migrations.RemoveField(
            model_name='akcija',
            name='udelezenci',
        ),
    ]