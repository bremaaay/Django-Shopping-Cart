# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-10 00:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank='true', max_length=200)),
                ('password', models.CharField(blank='true', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(blank='true', max_length=200)),
                ('itemquantity', models.CharField(blank='true', max_length=200)),
                ('itemimage', models.FileField(blank='true', upload_to='images')),
            ],
            options={
                'db_table': 'home_items',
            },
        ),
    ]
