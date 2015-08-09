# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_us',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=75)),
                ('content', models.TextField(default=None, blank=True)),
                ('weibo', models.CharField(max_length=30)),
                ('telephone', models.IntegerField(max_length=11)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
                ('content', models.TextField(default=None, blank=True)),
                ('tag', models.TextField(default=None, blank=True)),
                ('create_by', models.CharField(max_length=256, blank=True)),
                ('create_time', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=75)),
                ('content', models.TextField(default=None, blank=True)),
                ('weibo', models.CharField(max_length=30)),
                ('telephone', models.IntegerField(max_length=11)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
