# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-16 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]