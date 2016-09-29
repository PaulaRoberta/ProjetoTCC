# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('Comment', models.CharField(null=True, max_length=200)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2016, 9, 3, 20, 42, 5, 685132, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('serie_number', models.CharField(null=True, max_length=120, unique=True)),
                ('maker', models.CharField(null=True, max_length=120)),
                ('model', models.CharField(null=True, max_length=120)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2016, 9, 3, 20, 42, 5, 683281, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('description', models.CharField(null=True, max_length=200)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2016, 9, 3, 20, 42, 5, 683886, tzinfo=utc))),
                ('resolved_at', models.DateTimeField(null=True, blank=True)),
                ('entity', models.ForeignKey(null=True, to='app.Entity')),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('ask', models.CharField(null=True, max_length=200)),
                ('answer', models.CharField(null=True, max_length=200)),
                ('asked_at', models.DateTimeField(default=datetime.datetime(2016, 9, 3, 20, 42, 5, 685711, tzinfo=utc))),
                ('answered_at', models.DateTimeField(auto_now=True)),
                ('entity', models.ForeignKey(null=True, to='app.Entity')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(null=True, max_length=120)),
                ('description', models.CharField(null=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Midias',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('file', models.CharField(null=True, max_length=120)),
                ('link', models.CharField(null=True, max_length=120)),
                ('entity', models.ForeignKey(null=True, to='app.Entity')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(null=True, max_length=120)),
                ('email', models.CharField(null=True, max_length=120)),
                ('identify', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('type_user', models.CharField(max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.ForeignKey(to='app.UserType'),
        ),
        migrations.AddField(
            model_name='location',
            name='user',
            field=models.ForeignKey(null=True, to='app.User'),
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(null=True, to='app.User'),
        ),
        migrations.AddField(
            model_name='entity',
            name='location',
            field=models.ForeignKey(to='app.Location'),
        ),
        migrations.AddField(
            model_name='comment',
            name='event',
            field=models.ForeignKey(null=True, to='app.Event'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, to='app.User'),
        ),
    ]
