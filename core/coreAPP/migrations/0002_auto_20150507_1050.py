# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coreAPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('userName', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('permissions', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('busName', models.CharField(max_length=255)),
                ('repairBus', models.NullBooleanField()),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200, blank=True, null=True)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zipcode', models.IntegerField(max_length=15)),
                ('phone1', models.CharField(max_length=255)),
                ('phone2', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('web', models.URLField(max_length=255)),
                ('geolocal', models.CharField(max_length=255)),
                ('hours', models.CharField(max_length=255)),
                ('lastUpdate', models.DateTimeField(verbose_name='last updated')),
                ('adminID', models.ForeignKey(to='coreAPP.Admin')),
            ],
        ),
        migrations.CreateModel(
            name='BusItem',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('businesses', models.ForeignKey(to='coreAPP.Business')),
            ],
        ),
        migrations.CreateModel(
            name='RepCat',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('repName', models.CharField(max_length=255)),
                ('adminID', models.ForeignKey(to='coreAPP.Admin')),
            ],
        ),
        migrations.CreateModel(
            name='UseCat',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('catName', models.CharField(max_length=255)),
                ('lastUpdate', models.DateTimeField(verbose_name='date updated')),
                ('adminID', models.ForeignKey(to='coreAPP.Admin')),
            ],
        ),
        migrations.CreateModel(
            name='UseItems',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('itemName', models.CharField(max_length=255)),
                ('lastUpdate', models.DateTimeField(verbose_name='last updated')),
                ('adminID', models.ForeignKey(to='coreAPP.Admin')),
                ('itemCat', models.ForeignKey(to='coreAPP.UseCat')),
            ],
        ),
        migrations.RemoveField(
            model_name='reuseitem',
            name='itemCategory',
        ),
        migrations.DeleteModel(
            name='ReuseCategories',
        ),
        migrations.DeleteModel(
            name='ReuseItem',
        ),
        migrations.AddField(
            model_name='busitem',
            name='items',
            field=models.ForeignKey(to='coreAPP.UseItems'),
        ),
    ]
