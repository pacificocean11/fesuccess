# Generated by Django 3.2.9 on 2021-12-30 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0014_auto_20211230_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.CharField(default='', max_length=1000, unique=True),
        ),
    ]
