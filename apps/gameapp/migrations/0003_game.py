# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 17:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginreg', '0005_auto_20160820_1706'),
        ('gameapp', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('players', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('game_joiner', models.ManyToManyField(related_name='jointrip', to='loginreg.User')),
                ('game_starter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usersstarts', to='loginreg.User')),
            ],
        ),
    ]
