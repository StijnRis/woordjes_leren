from django.core.management.base import BaseCommand, CommandError
from quiz.models import Word, Language, Translation, Source, Wordlist
from bs4 import BeautifulSoup
import os
'''
python back_end/manage.py import_wrts_list C:\\Users\\stijn\\Downloads\\WRTS.html
'''


def dir_path(string):
    if os.path.isfile(string):
        return string
    else:
        raise Exception(f"{string} is not a file")


class Command(BaseCommand):
    help = "Import tranlations from scv file"

    def add_arguments(self, parser):
        parser.add_argument('path', type=dir_path)

    def handle(self, *args, **options):
        with open(options['path']) as file:
            webpage = BeautifulSoup(file.read(), features="html.parser")

        source = Source.objects.get(name='WRTS')

        languages = webpage.find_all("span", {"class": "label"})
        self.stdout.write(f"{languages}")
        self.stdout.write(f"{languages[0].contents}")
        language_1 = Language.objects.get(name=languages[0].contents[0])
        language_2 = Language.objects.get(name=languages[1].contents[0])

        name = webpage.find(
            "h1", {"class": "list-header-title"}).find("span").contents
        wordlist = Wordlist(name=name[0])
        wordlist.save()

        items = webpage.find_all("span", {"class": "notranslate"})
        self.stdout.write(f"{items}")
        for i in range(0, len(items), 3):
            word_1 = Word.objects.get_or_create(
                name=items[i].contents[0], language=language_1)[0]
            word_1.sources.add(source)

            word_2 = Word.objects.get_or_create(
                name=items[i+1].contents[0], language=language_2)[0]
            word_2.sources.add(source)

            translation = Translation.objects.get_or_create(
                word=word_1, translation=word_2)[0]
            translation.sources.add(source)
            wordlist.materials.add(translation)
