# Generated by Django 4.2 on 2023-04-15 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0017_rename_wordlist_material_wordlist2'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='translation',
            unique_together=set(),
        ),
        migrations.RenameField(
            model_name='translation',
            old_name='word',
            new_name='from_word',
        ),
        migrations.RenameField(
            model_name='translation',
            old_name='translation',
            new_name='to_word',
        ),
        migrations.AlterUniqueTogether(
            name='translation',
            unique_together={('from_word', 'to_word')},
        ),
    ]
