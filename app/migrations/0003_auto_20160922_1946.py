# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160922_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Texto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 22, 19, 46, 45, 272948, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='entity',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 22, 19, 46, 45, 270602, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 22, 19, 46, 45, 271330, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='faq',
            name='asked_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 22, 19, 46, 45, 273525, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='texto',
            name='entity',
            field=models.ForeignKey(null=True, to='app.Entity'),
        ),
    ]
