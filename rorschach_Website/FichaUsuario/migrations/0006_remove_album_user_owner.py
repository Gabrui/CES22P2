# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 13:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FichaUsuario', '0005_auto_20170603_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='user_owner',
        ),
    ]