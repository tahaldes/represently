# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 09:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rep_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ZipCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='rep',
            name='zipcode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zip_to_rep.ZipCode'),
        ),
    ]