# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReuseCategories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('lastUpdate', models.DateTimeField(verbose_name=b'date updated')),
            ],
        ),
        migrations.CreateModel(
            name='ReuseItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('itemName', models.CharField(max_length=255)),
                ('lastUpdate', models.DateTimeField(verbose_name=b'last updated')),
                ('itemCategory', models.ForeignKey(to='coreAPP.ReuseCategories')),
            ],
        ),
    ]
