# Generated by Django 3.2.9 on 2021-12-12 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_orderdetail_package'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderDetail',
        ),
    ]