# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-21 11:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='test',
        ),
    ]
