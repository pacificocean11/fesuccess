# Generated by Django 3.2.9 on 2021-12-21 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_thoughtdata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thoughtdata',
            old_name='thought_data',
            new_name='quote',
        ),
    ]
