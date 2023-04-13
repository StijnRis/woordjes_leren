from django.core.management.base import BaseCommand, CommandError
import argparse
import os
import sys
from quiz.models import Word, Language, Translation, Source, Wordlist


'''
python back_end/manage.py import_scv_file SSL_woordenlijst_engels C:\\Users\\stijn\\Downloads\\nl-en_words.xml English Nederlands --url https://www.sslleiden.nl/files/voorbereiding/V_EN_Woordenlijsten.pdf
'''



def dir_path(string):
    if os.path.isfile(string):
        return string
    else:
        raise Exception(f"{string} is not a file")


class Command(BaseCommand):
    help = "Import tranlations from scv file"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str)
        parser.add_argument('--url', type=str, default='')
        parser.add_argument('path', type=dir_path)
        parser.add_argument('from_language', type=str)
        parser.add_argument('to_language', type=str)

    def handle(self, *args, **options):
        name = options['name'] 
        url = options['url']
        source = Source.objects.get_or_create(name=name, url=url)[0]

        path = options['path']
        language_1 = Language.objects.get(name=options['from_language'])
        language_2 = Language.objects.get(name=options['to_language'])

        wordlist = Wordlist(name=name)
        wordlist.save()

        with open(path, 'r') as file:
            while line := file.readline():
                words = line.rstrip().split(',')

                if len(words) != 2:
                    self.stderr.write(f'{len(words)} is not 2')
                    continue

                word_1 = Word.objects.get_or_create(
                    name=words[0], language=language_1)[0]
                word_1.sources.add(source)

                word_2 = Word.objects.get_or_create(
                    name=words[1], language=language_2)[0]
                word_2.sources.add(source)

                translation = Translation.objects.get_or_create(
                    word=word_1, translation=word_2)[0]
                translation.sources.add(source)

                wordlist.materials.add(translation)
