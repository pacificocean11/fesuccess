# Generated by Django 3.2.9 on 2021-12-30 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0021_remove_question_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.CharField(default='', max_length=1000),
        ),
    ]