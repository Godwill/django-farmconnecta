# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-11 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20160926_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default='None', max_length=255),
        ),
    ]