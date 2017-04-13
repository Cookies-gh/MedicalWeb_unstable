# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-06 06:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0002_auto_20170331_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessoryexamination',
            name='doc',
            field=models.ImageField(default='', upload_to='AE/', verbose_name='Image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attachinfo',
            name='doc',
            field=models.ImageField(default='', upload_to='Attachment/', verbose_name='Image'),
            preserve_default=False,
        ),
    ]