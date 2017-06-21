# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 05:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20170616_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='pickup',
            field=models.TextField(blank=True, help_text='Enter names of people other than parents approved for pick-up, one per line', verbose_name='Approved for pickup'),
        ),
        migrations.AlterField(
            model_name='leader',
            name='position',
            field=models.CharField(blank=True, choices=[('Com', 'Commander'), ('Sec', 'Secretary'), ('Admin', 'Admin Helper'), ('Lead', 'Leader'), ('AL', 'Assistant Leader'), ('Student', 'Student Helper'), ('Direct', 'Director'), ('GameLead', 'Game Leader'), ('GameAs', 'Game Assistant'), ('GameStu', 'Game Student Helper'), ('Listener', 'Listener'), ('StoreShop', 'Store Shopper'), ('StoreCoor', 'Store Coordinator'), ('StoreHelp', 'Store Helper'), ('StoreWrap', 'Store Wrapper'), ('Float', 'Floater'), ('Web', 'Webmaster')], max_length=9, null=True),
        ),
    ]