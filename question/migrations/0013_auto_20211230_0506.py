# Generated by Django 3.2.9 on 2021-12-30 05:06

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0012_auto_20211229_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='option_a',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option_b',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option_c',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option_d',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
