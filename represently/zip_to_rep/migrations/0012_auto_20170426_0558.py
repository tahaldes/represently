# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 10:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zip_to_rep', '0011_auto_20170426_0555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rep',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='rep',
            name='dist',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='zip_to_rep.District'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='district',
            name='zip_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zip_to_rep.Zipcode'),
        ),
    ]
