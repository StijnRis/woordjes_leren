# Generated by Django 4.2 on 2023-04-13 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_sentence_source_translation_source'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sentence',
            name='source',
        ),
        migrations.AlterUniqueTogether(
            name='translation',
            unique_together={('word', 'translation')},
        ),
        migrations.AlterUniqueTogether(
            name='word',
            unique_together={('name', 'language')},
        ),
        migrations.RemoveField(
            model_name='translation',
            name='source',
        ),
    ]
