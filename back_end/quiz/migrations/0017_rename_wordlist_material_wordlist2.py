# Generated by Django 4.2 on 2023-04-14 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0016_alter_wordlist_visibility'),
    ]

    operations = [
        migrations.RenameField(
            model_name='material',
            old_name='wordlist',
            new_name='wordlist2',
        ),
    ]
