# Generated by Django 3.2.9 on 2022-01-01 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0026_question_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='tags',
            new_name='comma_saperated_tags',
        ),
    ]