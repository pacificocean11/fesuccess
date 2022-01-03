# Generated by Django 3.2.9 on 2021-12-21 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20211219_0521'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberSolvedQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solving_time', models.DateTimeField(auto_now_add=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.member')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.question')),
            ],
        ),
    ]
