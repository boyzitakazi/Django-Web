# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-02 05:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0006_auto_20200202_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerktpmodel',
            name='document',
            field=models.FileField(default=None, null=True, upload_to=b'media/Data_Pemohon'),
        ),
    ]
