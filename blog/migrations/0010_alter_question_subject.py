# Generated by Django 3.2.9 on 2021-12-16 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20211216_0546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='subject',
            field=models.ManyToManyField(blank=True, to='blog.Subject'),
        ),
    ]
