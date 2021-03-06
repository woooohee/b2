# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-11-27 02:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import photo.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='앨범 이름')),
                ('description', models.CharField(blank=True, max_length=100, verbose_name='앨범 설명')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='사진 제목')),
                ('image', photo.fields.ThumbnailImageField(upload_to='photo/%Y/%m')),
                ('description', models.TextField(blank=True, verbose_name='사진 설명')),
                ('upload_date', models.DateTimeField(auto_now_add=True, verbose_name='등록 일시')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photo.Album')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
