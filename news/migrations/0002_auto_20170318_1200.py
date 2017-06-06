# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-18 04:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='focusarticle',
            name='pic',
            field=models.ImageField(default='images/default.jpg', upload_to='uploads/top_images/%(basename)s_%(datetime)s.%(extname)s', verbose_name='头条图片436*200'),
        ),
        migrations.AlterField(
            model_name='lawarticle',
            name='pic',
            field=models.ImageField(default='images/default.jpg', upload_to='uploads/top_images/%(basename)s_%(datetime)s.%(extname)s', verbose_name='头条图片436*200'),
        ),
        migrations.AlterField(
            model_name='policyarticle',
            name='pic',
            field=models.ImageField(default='images/default.jpg', upload_to='uploads/top_images/%(basename)s_%(datetime)s.%(extname)s', verbose_name='头条图片436*200'),
        ),
        migrations.AlterField(
            model_name='popularscience',
            name='pic',
            field=models.ImageField(default='images/default.jpg', upload_to='uploads/top_images/%(basename)s_%(datetime)s.%(extname)s', verbose_name='头条图片436*200'),
        ),
        migrations.AlterField(
            model_name='talentsarticle',
            name='pic',
            field=models.ImageField(default='images/default.jpg', upload_to='uploads/top_images/%(basename)s_%(datetime)s.%(extname)s', verbose_name='头条图片436*200'),
        ),
        migrations.AlterField(
            model_name='techarticle',
            name='pic',
            field=models.ImageField(default='images/default.jpg', upload_to='uploads/top_images/%(basename)s_%(datetime)s.%(extname)s', verbose_name='头条图片436*200'),
        ),
    ]