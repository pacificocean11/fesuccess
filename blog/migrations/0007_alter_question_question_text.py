# Generated by Django 3.2.9 on 2021-12-15 18:04

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_question_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
