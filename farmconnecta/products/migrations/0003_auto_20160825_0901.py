# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.FileField(blank=True, upload_to='products'),
        ),
    ]