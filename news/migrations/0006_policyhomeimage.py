# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-01 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_slideimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='policyhomeImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255, verbose_name='图片标题')),
                ('homepic', models.ImageField(default='uploads/top_images/default.jpg', upload_to='uploads/top_images/', verbose_name='首页政策图片')),
            ],
            options={
                'verbose_name': '首页管理政策图片',
            },
        ),
    ]
