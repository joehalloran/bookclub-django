# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 22:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
    ]