# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-30 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0022_patientgroup_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientgroup',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
