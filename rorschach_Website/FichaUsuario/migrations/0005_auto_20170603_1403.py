# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FichaUsuario', '0004_auto_20170602_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='file_type',
        ),
        migrations.AddField(
            model_name='picture',
            name='picture_file',
            field=models.ImageField(default=None, max_length=1000, upload_to=''),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='avatar',
            field=models.ImageField(default='avatar.png', max_length=250, upload_to=''),
        ),
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.ImageField(max_length=1000, upload_to=''),
        ),
    ]
