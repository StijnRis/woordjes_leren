from django.core.management.base import BaseCommand, CommandError
import argparse
import os
import sys
from quiz.models import Word, Language, Translation
# python back_end/manage.py import_scv_file C:\Users\stijn\Downloads\nl-en_words.xml English Nederlands


def dir_path(string):
    if os.path.isfile(string):
        return string
    else:
        sys.exit()


class Command(BaseCommand):
    help = "Import tranlations from scv file"

    def add_arguments(self, parser):
        parser.add_argument('path', type=dir_path)
        parser.add_argument('from_language', type=str)
        parser.add_argument('to_language', type=str)

    def handle(self, *args, **options):
        path = options['path']
        language_1 = Language.objects.get(name=options['from_language'])
        language_2 = Language.objects.get(name=options['to_language'])

        with open(path, 'r') as file:
            while line := file.readline():
                words = line.rstrip().split(',')

                if len(words) != 2:
                    self.stderr.write(f'{len(words)} is not 2')
                    continue

                word_1 = Word.objects.get_or_create(
                    name=words[0], language=language_1)
                word_2 = Word.objects.get_or_create(
                    name=words[1], language=language_2)

                Translation.objects.get_or_create(
                    word=word_1, translation=word_2)
