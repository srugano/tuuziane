# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 08:44
from __future__ import unicode_literals

import oscar.models.fields.slugfield
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0008_auto_20160304_1652"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="slug",
            field=oscar.models.fields.slugfield.SlugField(
                max_length=255, verbose_name="Slug"
            ),
        ),
    ]
