from django.core.management.base import BaseCommand, CommandError
import argparse
import os


def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


class Command(BaseCommand):
    help = "Analyse a text and add all the data to the database"

    def add_arguments(self, parser):
        parser.add_argument('path', type=dir_path)

    def handle(self, *args, **options):
        path = options['path']

        with open(path, 'r') as file:
            pass
