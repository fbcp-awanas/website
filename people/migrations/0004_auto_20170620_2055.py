# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 01:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20170617_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
