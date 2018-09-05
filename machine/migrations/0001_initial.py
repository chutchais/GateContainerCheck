# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-08-19 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='machine',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_loggin_date', models.DateTimeField(auto_now=True, null=True)),
                ('ip', models.GenericIPAddressField()),
            ],
        ),
    ]
