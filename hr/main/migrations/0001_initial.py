# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-28 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default='N/A', max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, default='N/A', max_length=10, null=True)),
                ('status', models.CharField(blank=True, default='N/A', max_length=10, null=True)),
            ],
        ),
    ]
