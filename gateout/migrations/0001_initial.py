# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-12 10:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import gateout.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking', models.CharField(max_length=50)),
                ('line', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='container',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=15)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('terminal', models.CharField(max_length=10)),
                ('order_date', models.DateTimeField(blank=True, null=True)),
                ('imo1', models.CharField(max_length=20)),
                ('imo2', models.CharField(max_length=20)),
                ('move', models.CharField(max_length=50)),
                ('temperature', models.CharField(max_length=20)),
                ('pod', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=20)),
                ('iso', models.CharField(max_length=10)),
                ('plate_id', models.CharField(max_length=20)),
                ('truck_company', models.CharField(max_length=100)),
                ('consignee', models.CharField(max_length=100)),
                ('seal1', models.CharField(max_length=50)),
                ('seal2', models.CharField(max_length=50)),
                ('weight', models.FloatField(default=0)),
                ('exception', models.CharField(max_length=100)),
                ('genset', models.CharField(max_length=100)),
                ('damage', models.CharField(max_length=200)),
                ('remark', models.CharField(max_length=200)),
                ('checker', models.CharField(max_length=100)),
                ('check_date', models.DateTimeField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gateout.booking')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='container_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=gateout.models.image_directory_path)),
                ('thumbnails_image', models.ImageField(upload_to=gateout.models.thumbnails_directory_path)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('container', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gateout.container')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='vessel',
            fields=[
                ('code', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='voy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voy', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vessel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gateout.vessel')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='voy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gateout.voy'),
        ),
        migrations.AlterUniqueTogether(
            name='container',
            unique_together=set([('number', 'booking')]),
        ),
    ]
