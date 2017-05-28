# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 12:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_owner', models.CharField(max_length=250)),
                ('algum_title', models.CharField(max_length=250)),
                ('genre', models.CharField(max_length=100)),
                ('algum_logo', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(max_length=10)),
                ('picture_title', models.CharField(max_length=250)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FichaUsuario.Album')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email_account', models.CharField(max_length=250)),
                ('gender', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=250)),
                ('home_state_address', models.CharField(max_length=250)),
                ('religion', models.CharField(max_length=250)),
                ('music_like', models.CharField(max_length=250)),
                ('civil_status', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=100)),
                ('album_picture', models.CharField(max_length=10000)),
                ('age', models.IntegerField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FichaUsuario.UserInfo'),
        ),
    ]