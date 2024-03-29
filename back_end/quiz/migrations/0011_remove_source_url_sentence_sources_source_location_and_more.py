# Generated by Django 4.2 on 2023-04-13 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0010_remove_sentence_source_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='source',
            name='url',
        ),
        migrations.AddField(
            model_name='sentence',
            name='sources',
            field=models.ManyToManyField(to='quiz.source'),
        ),
        migrations.AddField(
            model_name='source',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='translation',
            name='source',
            field=models.ManyToManyField(to='quiz.source'),
        ),
        migrations.AddField(
            model_name='wordlist',
            name='materials',
            field=models.ManyToManyField(through='quiz.Material', to='quiz.translation'),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(help_text='The name of the language', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='translation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='quiz.translation'),
        ),
        migrations.AlterField(
            model_name='material',
            name='wordlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.wordlist'),
        ),
        migrations.AlterField(
            model_name='source',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='sentence',
            unique_together={('sentence', 'language')},
        ),
    ]
