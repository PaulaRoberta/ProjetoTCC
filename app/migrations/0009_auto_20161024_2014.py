# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 20:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20161023_2229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 24, 20, 14, 6, 29350, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='entity',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 24, 20, 14, 6, 25802, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 24, 20, 14, 6, 26555, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='faq',
            name='asked_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 24, 20, 14, 6, 30008, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='imagem',
            name='entity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Entity'),
        ),
    ]
