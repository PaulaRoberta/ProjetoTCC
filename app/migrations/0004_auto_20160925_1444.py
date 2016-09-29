# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160922_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='texto',
            name='entity',
        ),
        migrations.AddField(
            model_name='entity',
            name='description',
            field=models.CharField(null=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 25, 14, 44, 37, 859754, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='entity',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 25, 14, 44, 37, 857877, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 25, 14, 44, 37, 858641, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='faq',
            name='asked_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 25, 14, 44, 37, 860321, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='Texto',
        ),
    ]
