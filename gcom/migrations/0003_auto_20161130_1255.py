# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 07:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gcom', '0002_auto_20161129_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ImageField(upload_to=b'siteimages/'),
        ),
    ]