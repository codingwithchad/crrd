# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coreAPP', '0002_auto_20150507_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='password',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='admin',
            name='permissions',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='admin',
            name='userName',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='business',
            name='busName',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='business',
            name='city',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='business',
            name='geolocal',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='business',
            name='hours',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='business',
            name='phone1',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='business',
            name='phone2',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='business',
            name='state',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='business',
            name='web',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='business',
            name='zipcode',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='repcat',
            name='repName',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='usecat',
            name='catName',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='useitems',
            name='itemName',
            field=models.CharField(max_length=200),
        ),
    ]
