# Generated by Django 3.2.9 on 2021-12-16 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discipline_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]
