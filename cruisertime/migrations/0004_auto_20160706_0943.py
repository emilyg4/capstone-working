# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cruisertime', '0003_worldborder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worldborder',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]