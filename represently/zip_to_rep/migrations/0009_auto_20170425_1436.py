# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 19:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zip_to_rep', '0008_auto_20170425_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rep',
            name='zip_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zip_to_rep.Zipcode'),
        ),
    ]
