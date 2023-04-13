from django.conf import settings
from rest_framework import serializers
from quiz.models import Language, Word, Translation, Wordlist, Sentence, Material
from accounts.serializers import BasicUserProfileSerializer


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ['pk', 'name']
        read_only_fields = ['pk', 'name']


class SentenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sentence
        fields = ['pk', 'sentence', 'language']
        read_only_fields = ['pk', 'sentence', 'language']


class WordSentenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sentence
        fields = ['pk', 'sentence']
        read_only_fields = ['pk', 'sentence']


class WordSerializer(serializers.HyperlinkedModelSerializer):
    usage = WordSentenceSerializer(many=True)
    language = LanguageSerializer()

    class Meta:
        model = Word
        fields = ['pk', 'name', 'language', 'usage']
        read_only_fields = ['pk', 'name', 'language', 'usage']


class TranslationSerializer(serializers.HyperlinkedModelSerializer):
    word = WordSerializer()
    translation = WordSerializer()

    class Meta:
        model = Translation
        fields = ['pk', 'wrong_tries', 'correct_tries',
                  'word', 'translation',]
        read_only_fields = ['pk', 'word', 'translation',
                            'wrong_tries', 'correct_tries']


class MaterialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Material
        fields = ['pk', 'wordlist', 'date_added', 'translation']
        read_only_fields = ['pk', 'wordlist', 'date_added', 'translation']


class MaterialWordlistSerializer(serializers.HyperlinkedModelSerializer):
    translation = TranslationSerializer()

    class Meta:
        model = Material
        fields = ['pk', 'date_added', 'translation']
        read_only_fields = ['pk', 'date_added']


class BasicWordListSerializer(serializers.HyperlinkedModelSerializer):
    owner = BasicUserProfileSerializer()

    class Meta:
        model = Wordlist
        fields = ['pk', 'name', 'date_published', 'owner']
        read_only_fields = ['pk', 'date_published', 'owner']


class WordListSerializer(serializers.HyperlinkedModelSerializer):
    materials = MaterialWordlistSerializer(many=True)
    owner = BasicUserProfileSerializer()

    class Meta:
        model = Wordlist
        fields = ['pk', 'name', 'date_published',
                  'visibility', 'owner', 'materials']
        read_only_fields = ['pk', 'owner', 'date_published']
