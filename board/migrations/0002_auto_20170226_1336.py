# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-26 13:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board',
            options={'ordering': ('-date',), 'verbose_name': 'board'},
        ),
        migrations.AddField(
            model_name='board',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date(2017, 2, 26)),
            preserve_default=False,
        ),
    ]
