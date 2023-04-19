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
        try:
            return Language.objects.get(name=validated_data['name'])
        except ObjectDoesNotExist:
            return super().create(**validated_data)


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


class WordSerializer(WritableNestedModelSerializer):
    usage = BasicSentenceSerializer(many=True, read_only=True)
    language = LanguageSerializer(read_only=False)

    class Meta:
        model = Word
        fields = ['pk', 'name', 'language', 'usage']
        read_only_fields = ['pk']

    def create(self, validated_data):
        try:
            return Language.objects.get(name=validated_data['name'], language=validated_data['language'])
        except ObjectDoesNotExist:
            return super().create(**validated_data)


class TranslationSerializer(WritableNestedModelSerializer):
    from_word = WordSerializer(read_only=False)
    to_word = WordSerializer(read_only=False)

    class Meta:
        model = Translation
        fields = ['pk', 'wrong_tries', 'correct_tries',
                  'from_word', 'to_word',]
        read_only_fields = ['pk', 'wrong_tries', 'correct_tries',]

    def create(self, validated_data):
        try:
            return Translation.objects.get(from_word=validated_data['from_word'], to_word=validated_data['to_word'])
        except ObjectDoesNotExist:
            return super().create(**validated_data)


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

    # def create(self, validated_data):
    #     materials_data = validated_data.pop('material_set')
    #     wordlist = Wordlist.objects.create(**validated_data)
    #     wordlist.save()
    #     for material_data in materials_data:
    #         translation, created = Translation.objects.get_or_create(
    #             **material_data['translation'])
    #         wordlist.materials.add(translation)
    #     return wordlist
