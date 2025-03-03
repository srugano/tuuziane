# Generated by Django 4.2.6 on 2023-12-20 17:10

import oscar.models.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("catalogue", "0026_predefined_product_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="attributeoption",
            name="code",
            field=oscar.models.fields.NullCharField(max_length=255, unique=True, verbose_name="Unique identifier"),
        ),
        migrations.AddField(
            model_name="attributeoptiongroup",
            name="code",
            field=oscar.models.fields.NullCharField(max_length=255, unique=True, verbose_name="Unique identifier"),
        ),
        migrations.AddField(
            model_name="category",
            name="code",
            field=oscar.models.fields.NullCharField(max_length=255, unique=True, verbose_name="Code"),
        ),
        migrations.AddField(
            model_name="productimage",
            name="code",
            field=oscar.models.fields.NullCharField(max_length=255, unique=True, verbose_name="Code"),
        ),
    ]
