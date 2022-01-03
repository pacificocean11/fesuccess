# Generated by Django 3.2.9 on 2021-12-23 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0027_rename_thought_data_thoughtdata_quote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membersolvedquestion',
            name='member',
        ),
        migrations.RemoveField(
            model_name='membersolvedquestion',
            name='question',
        ),
        migrations.RemoveField(
            model_name='question',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='question',
            name='subtopic',
        ),
        migrations.RemoveField(
            model_name='question',
            name='topic',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='realted_disciplines',
        ),
        migrations.RemoveField(
            model_name='subtopic',
            name='related_subject',
        ),
        migrations.RemoveField(
            model_name='subtopic',
            name='topic',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='related_disciplines',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='related_subjects',
        ),
        migrations.DeleteModel(
            name='MemberCompletedTopic',
        ),
        migrations.DeleteModel(
            name='MemberSolvedQuestion',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.DeleteModel(
            name='SubTopic',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]
