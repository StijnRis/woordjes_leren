import json
from django.conf import settings
from rest_framework import serializers
from quiz.models import Language, Word, Translation, Wordlist, Sentence, Material
from accounts.serializers import BasicUserProfileSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer
from drf_writable_nested.mixins import UniqueFieldsMixin
from django.core.exceptions import ObjectDoesNotExist


class LanguageSerializer(UniqueFieldsMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ['pk', 'name']
        read_only_fields = ['pk']

    def create(self, validated_data):
        language, created = Language.objects.get_or_create(
            name=validated_data['name'])
        return language


class SentenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sentence
        fields = ['pk', 'sentence', 'language']
        read_only_fields = ['pk', 'sentence', 'language']


class BasicSentenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sentence
        fields = ['pk', 'sentence']
        read_only_fields = ['pk', 'sentence']


class WordSerializer(serializers.HyperlinkedModelSerializer):
    language = LanguageSerializer(read_only=False)
    usage = BasicSentenceSerializer(many=True, read_only=True)

    class Meta:
        model = Word
        fields = ['pk', 'name', 'language', 'usage']
        read_only_fields = ['pk']

    def create(self, validated_data):
        language_serializer = LanguageSerializer()
        language = language_serializer.create(validated_data['language'])
        word, created = Word.objects.get_or_create(
            name=validated_data['name'], language=language)
        return word


class TranslationSerializer(serializers.HyperlinkedModelSerializer):
    from_word = WordSerializer(read_only=False)
    to_word = WordSerializer(read_only=False)

    class Meta:
        model = Translation
        fields = ['pk', 'wrong_tries', 'correct_tries',
                  'from_word', 'to_word',]
        read_only_fields = ['pk', 'wrong_tries', 'correct_tries',]

    def create(self, validated_data):
        word_serializer = WordSerializer()
        from_word = word_serializer.create(validated_data['from_word'])
        to_word = word_serializer.create(validated_data['to_word'])
        translation, created = Translation.objects.get_or_create(
            from_word=from_word, to_word=to_word)
        return translation


class MaterialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Material
        fields = ['pk', 'wordlist', 'date_added', 'translation']
        read_only_fields = ['pk', 'wordlist', 'date_added', 'translation']


class MaterialWordlistSerializer(WritableNestedModelSerializer):
    translation = TranslationSerializer(read_only=False)

    class Meta:
        model = Material
        fields = ['pk', 'date_added', 'translation']
        read_only_fields = ['pk', 'date_added']


class BasicWordlistSerializer(WritableNestedModelSerializer):
    owner = BasicUserProfileSerializer(read_only=True)

    class Meta:
        model = Wordlist
        fields = ['pk', 'name', 'date_published', 'owner']
        read_only_fields = ['pk', 'date_published']


class WordlistSerializer(WritableNestedModelSerializer):
    materials = MaterialWordlistSerializer(
        source='material_set', many=True, read_only=False)
    owner = BasicUserProfileSerializer(read_only=True)

    class Meta:
        model = Wordlist
        fields = ['pk', 'name', 'date_published',
                  'visibility', 'owner', 'materials']
        read_only_fields = ['pk', 'owner', 'date_published']

    def create(self, validated_data):
        return super().create(validated_data)
