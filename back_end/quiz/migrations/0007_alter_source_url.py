# Generated by Django 4.2 on 2023-04-13 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_source_alter_material_translation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
