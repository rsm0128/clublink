# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-22 02:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0049_auto_20170818_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubevent',
            name='online_registration',
            field=models.BooleanField(default=False),
        ),
    ]
