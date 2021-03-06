# Generated by Django 3.2.9 on 2021-12-29 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0007_alter_topic_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subject_name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='subtopic',
            name='subtopic_name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='topic_name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
