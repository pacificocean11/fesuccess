# Generated by Django 3.2.9 on 2021-12-16 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_question_question_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=200)),
                ('related_subjects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.subject')),
            ],
        ),
    ]
