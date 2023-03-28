from django.urls import reverse
from django.utils import timezone
import datetime
from django.db import models
import random

# python manage.py makemigrations
# python manage.py migrate


class Language(models.Model):
    name = models.CharField(
        max_length=200, help_text='The name of the language')

    def get_absolute_url(self):
        return reverse("language-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f'{self.name}'


class Sentence(models.Model):
    sentence = models.CharField(max_length=1000)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.sentence}'


class Word(models.Model):
    name = models.CharField(
        max_length=200, help_text='How the word is spelled')
    language = models.ForeignKey(
        Language, on_delete=models.SET_NULL, help_text='The language of this word', null=True)
    usage = models.ManyToManyField(Sentence, blank=True)

    def __str__(self):
        return f'{self.name}'


class Translation(models.Model):
    word = models.ForeignKey(
        Word, on_delete=models.RESTRICT, related_name='words')
    translation = models.ForeignKey(
        Word, on_delete=models.RESTRICT, related_name='translations')
    wrong_tries = models.IntegerField(default=0)
    correct_tries = models.IntegerField(default=0)
    difficulty = models.FloatField()

    def get_options(self):
        words = list(Word.objects.all())
        random_words = random.sample(words, 3)
        random_words.append(self.translation)
        return random_words

    def __str__(self):
        percentage = "-"
        if self.correct_tries > 0:
            percentage = str(round(self.correct_tries / (self.correct_tries + self.wrong_tries) * 100)) + '%'
        return f'{self.word} -> {self.translation}  ({percentage})'


class Wordlist(models.Model):
    owner = models.ForeignKey(
        'auth.User', related_name='wordlists', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    date_published = models.DateTimeField('date published', auto_now_add=True)
    translations = models.ManyToManyField(Translation, help_text='The translations in this word list.')

    VISIBILITY_STATUS = (
        ('pr', 'Private'),
        ('pl', 'Public'),
        ('re', 'Under review'),
    )
    visibility = models.CharField(
        max_length=2,
        choices=VISIBILITY_STATUS,
        default='pr',
        help_text='Visibily status',
    )

    def get_absolute_url(self):
        return reverse('wordlist-detail', kwargs={"pk": self.pk})
    
    def get_absolute_exersice_url(self):
        return reverse('wordlist-exercise', kwargs={"pk": self.pk})

    def was_published_recently(self):
        return self.date_published >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return f'{self.name}'
