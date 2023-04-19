# Generated by Django 4.2 on 2023-04-13 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_rename_added_material_date_added_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name='material',
            name='translation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='materials', to='quiz.translation'),
        ),
        migrations.AlterField(
            model_name='word',
            name='language',
            field=models.ForeignKey(help_text='The language of this word', null=True, on_delete=django.db.models.deletion.RESTRICT, to='quiz.language'),
        ),
    ]