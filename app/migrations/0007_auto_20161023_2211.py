# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 22:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20161023_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 23, 22, 11, 19, 470013, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='entity',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 23, 22, 11, 19, 466958, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='entity',
            name='image',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 23, 22, 11, 19, 467735, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='faq',
            name='asked_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 23, 22, 11, 19, 470726, tzinfo=utc)),
        ),
    ]
