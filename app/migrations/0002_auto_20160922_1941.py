# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 22, 19, 41, 32, 561360, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='entity',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 22, 19, 41, 32, 559456, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 22, 19, 41, 32, 560208, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='faq',
            name='asked_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 22, 19, 41, 32, 561932, tzinfo=utc)),
        ),
    ]
