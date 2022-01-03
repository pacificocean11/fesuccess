# Generated by Django 3.2.9 on 2021-12-15 15:58

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_orderdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', ckeditor.fields.RichTextField()),
                ('correct_choice', models.IntegerField()),
                ('solution', ckeditor.fields.RichTextField()),
                ('video_solution_url', models.CharField(blank=True, max_length=1000)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.subject')),
            ],
        ),
    ]