from django.utils import timezone
import datetime
from django.db import models
import random

# python manage.py makemigrations
# python manage.py migrate


class Language(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Word(models.Model):
    name = models.CharField(max_length=200)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Sentence(models.Model):
    sentence = models.CharField(max_length=1000)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)


class ExampleUsage(models.Model):
    sentence = models.ForeignKey(Sentence, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)


class Translation(models.Model):
    word_one = models.ForeignKey(
        Word, on_delete=models.CASCADE, related_name='translations_from')
    word_two = models.ForeignKey(
        Word, on_delete=models.CASCADE, related_name='translations_to')
    wrong_tries = models.IntegerField(default=0)
    correct_tries = models.IntegerField(default=0)
    difficulty = models.FloatField()

    def getOptions(self):
        words = list(Word.objects.all())
        random_words = random.sample(words, 3)
        random_words.append(self.word_two)
        return random_words

    def __str__(self):
        return f'{self.word_one} - {self.word_two}  ({self.correct_tries} vs {self.wrong_tries})'

class WordList(models.Model):
    owner = models.ForeignKey('auth.User', related_name='word_lists', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    published_date = models.DateTimeField('date published')
    translations = models.ManyToManyField(Translation)

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.published_date >= timezone.now() - datetime.timedelta(days=1)



