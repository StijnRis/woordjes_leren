from django.conf import settings
from rest_framework import serializers
from quiz.models import Language, Word, Translation, Wordlist, Sentence, Material


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ['name']


class SentenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sentence
        fields = ['sentence', 'language']


class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ['name', 'language', 'usage']


class TranslationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Translation
        fields = ['id', 'word', 'translation',
                  'wrong_tries', 'correct_tries', 'difficulty']


class WordListSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.HyperlinkedRelatedField(
    #     view_name='wordlist-detail', read_only=True)  # ReadOnlyField(source='owner.username')
    materials = serializers.HyperlinkedRelatedField(
        view_name='material-detail', many=True, queryset=Sentence.objects.all())

    class Meta:
        model = Wordlist
        fields = ['owner', 'name', 'date_published', 'materials']


class MaterialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Material
        fields = ['wordlist', 'translation', 'date_added']
