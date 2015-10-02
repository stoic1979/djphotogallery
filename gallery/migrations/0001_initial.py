# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(default=datetime.datetime.now)),
                ('title', models.CharField(unique=True, max_length=64)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True)),
                ('is_public', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(default=datetime.datetime.now)),
                ('title', models.CharField(max_length=64)),
                ('slug', models.SlugField(unique=True)),
                ('caption', models.TextField(blank=True)),
                ('is_public', models.BooleanField(default=True)),
                ('gallery', models.ForeignKey(to='gallery.Gallery')),
            ],
        ),
    ]
