# Generated by Django 3.2.9 on 2021-12-16 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_alter_member_order_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='package_expiration_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='purchase_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
