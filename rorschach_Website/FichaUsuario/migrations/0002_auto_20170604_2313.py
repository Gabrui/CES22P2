# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 23:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FichaUsuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenreModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_score', models.IntegerField()),
                ('picture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FichaUsuario.Picture')),
            ],
        ),
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FichaUsuario.GenreModel'),
        ),
    ]
