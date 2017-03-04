# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-03 18:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emission',
            name='description',
            field=models.TextField(default='Enter description here'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enregistrement',
            name='description',
            field=models.TextField(default='Enter description here'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enregistrement',
            name='edition_id',
            field=models.SmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]