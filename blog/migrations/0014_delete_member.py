# Generated by Django 3.2.9 on 2021-12-16 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_member'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Member',
        ),
    ]