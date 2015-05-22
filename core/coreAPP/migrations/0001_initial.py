# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('busName', models.CharField(verbose_name='Business Name', unique=True, max_length=200)),
                ('repairBus', models.NullBooleanField()),
                ('address1', models.CharField(verbose_name='Address', max_length=200, blank=True)),
                ('address2', models.CharField(verbose_name='Address', max_length=200, blank=True)),
                ('city', models.CharField(max_length=200, blank=True)),
                ('state', models.CharField(max_length=200, blank=True)),
                ('zipcode', models.IntegerField(null=True, blank=True)),
                ('phone1', models.CharField(max_length=200, blank=True)),
                ('phone2', models.CharField(max_length=200, blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('web', models.URLField(blank=True)),
                ('geolocal', models.CharField(max_length=200, blank=True)),
                ('hours', models.CharField(max_length=200, blank=True)),
                ('lastUpdate', models.DateTimeField(verbose_name='last updated', null=True, auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BusItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('lastUpdate', models.DateTimeField(verbose_name='last updated', auto_now=True)),
                ('businesses', models.ForeignKey(to='coreAPP.Business')),
            ],
            options={
                'verbose_name': 'Reuse Business Item',
                'verbose_name_plural': 'Reuse Business Items',
            },
        ),
        migrations.CreateModel(
            name='BusRepairItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('business', models.ForeignKey(to='coreAPP.Business')),
            ],
            options={
                'verbose_name': 'Repair Business Item',
                'verbose_name_plural': 'Repair Business Items',
            },
        ),
        migrations.CreateModel(
            name='RepairItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('RepItemName', models.CharField(unique=True, max_length=200)),
                ('lastUpdate', models.DateTimeField(verbose_name='last update', auto_now=True)),
            ],
            options={
                'verbose_name': 'Repair Item',
                'verbose_name_plural': 'Repair Items',
            },
        ),
        migrations.CreateModel(
            name='RepCat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('repName', models.CharField(unique=True, max_length=200)),
                ('lastUpdate', models.DateTimeField(verbose_name='last update', auto_now=True)),
            ],
            options={
                'verbose_name': 'Repair Category',
                'verbose_name_plural': 'Repair Categories',
            },
        ),
        migrations.CreateModel(
            name='ReuseItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('itemName', models.CharField(verbose_name='item name', unique=True, max_length=200)),
                ('lastUpdate', models.DateTimeField(verbose_name='last updated', auto_now=True)),
            ],
            options={
                'verbose_name': 'Reuse Item',
                'verbose_name_plural': 'Reuse Items',
            },
        ),
        migrations.CreateModel(
            name='UseCat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('catName', models.CharField(verbose_name='Category Name', unique=True, max_length=200)),
                ('lastUpdate', models.DateTimeField(verbose_name='date updated', auto_now=True)),
            ],
            options={
                'verbose_name': 'Reuse Category',
                'verbose_name_plural': 'Reuse Categories',
            },
        ),
        migrations.AddField(
            model_name='reuseitem',
            name='itemCat',
            field=models.ForeignKey(to='coreAPP.UseCat'),
        ),
        migrations.AddField(
            model_name='repairitem',
            name='RepCat',
            field=models.ForeignKey(to='coreAPP.RepCat'),
        ),
        migrations.AddField(
            model_name='busrepairitem',
            name='repairItem',
            field=models.ForeignKey(to='coreAPP.RepairItem'),
        ),
        migrations.AddField(
            model_name='busitem',
            name='items',
            field=models.ForeignKey(to='coreAPP.ReuseItem'),
        ),
    ]
