# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-02 05:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0011_auto_20200202_0517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerktpmodel',
            name='document',
            field=models.FileField(null=b'True', upload_to=b'Data_Pemohon', verbose_name=b'Upload Document'),
        ),
    ]
