# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-08-22 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_userpermissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpermissions',
            name='can_impersonate_user',
            field=models.BooleanField(default=False),
        ),
    ]
