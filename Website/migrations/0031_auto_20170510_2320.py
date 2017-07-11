# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-10 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0030_appinfo_s_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='co',
            old_name='dongDingMenNei',
            new_name='miYun',
        ),
        migrations.RenameField(
            model_name='co',
            old_name='wanShouGongXi',
            new_name='shunYi',
        ),
        migrations.RenameField(
            model_name='no2',
            old_name='dongDingMenNei',
            new_name='miYun',
        ),
        migrations.RenameField(
            model_name='no2',
            old_name='wanShouGongXi',
            new_name='shunYi',
        ),
        migrations.RenameField(
            model_name='o3',
            old_name='dongDingMenNei',
            new_name='miYun',
        ),
        migrations.RenameField(
            model_name='o3',
            old_name='wanShouGongXi',
            new_name='shunYi',
        ),
        migrations.RenameField(
            model_name='pm10',
            old_name='dongDingMenNei',
            new_name='miYun',
        ),
        migrations.RenameField(
            model_name='pm10',
            old_name='wanShouGongXi',
            new_name='shunYi',
        ),
        migrations.RenameField(
            model_name='pm25',
            old_name='dongDingMenNei',
            new_name='miYun',
        ),
        migrations.RenameField(
            model_name='pm25',
            old_name='wanShouGongXi',
            new_name='shunYi',
        ),
        migrations.RenameField(
            model_name='so2',
            old_name='dongDingMenNei',
            new_name='miYun',
        ),
        migrations.RenameField(
            model_name='so2',
            old_name='wanShouGongXi',
            new_name='shunYi',
        ),
        migrations.AddField(
            model_name='co',
            name='wanShouXiGong',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='co',
            name='yongDingMenNei',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='co',
            name='yuFa',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='no2',
            name='wanShouXiGong',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='no2',
            name='yongDingMenNei',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='no2',
            name='yuFa',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='o3',
            name='wanShouXiGong',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='o3',
            name='yongDingMenNei',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='o3',
            name='yuFa',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pm10',
            name='wanShouXiGong',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pm10',
            name='yongDingMenNei',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pm10',
            name='yuFa',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pm25',
            name='wanShouXiGong',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pm25',
            name='yongDingMenNei',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pm25',
            name='yuFa',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='so2',
            name='wanShouXiGong',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='so2',
            name='yongDingMenNei',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='so2',
            name='yuFa',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]