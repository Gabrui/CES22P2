# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 23:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FichaUsuario', '0003_auto_20170602_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=250)),
                ('username', models.CharField(default='myusername', max_length=250, unique=True)),
                ('email_account', models.EmailField(default='myaccount@emaildomain.com', max_length=250, unique=True)),
                ('gender', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=250)),
                ('home_state_address', models.CharField(max_length=250)),
                ('religion', models.CharField(max_length=250)),
                ('music_like', models.CharField(max_length=250)),
                ('civil_status', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=100)),
                ('album_picture', models.CharField(max_length=10000)),
                ('age', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.AlterField(
            model_name='album',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FichaUsuario.UserInfo'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
