# Generated by Django 3.2.9 on 2021-12-16 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='subject',
        ),
        migrations.AddField(
            model_name='question',
            name='subject',
            field=models.ManyToManyField(to='blog.Subject'),
        ),
    ]
