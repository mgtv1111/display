# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-06 06:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0002_tables'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='modules',
            table='display_Modules',
        ),
        migrations.AlterModelTable(
            name='tables',
            table='display_Tables',
        ),
    ]
