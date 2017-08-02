# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MMSMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=30)),
                ('mime_type', models.CharField(max_length=30)),
                ('media_sid', models.CharField(max_length=35)),
                ('message_sid', models.CharField(max_length=35)),
                ('media_url', models.CharField(max_length=150)),
                ('content', models.TextField()),
            ],
        ),
    ]
