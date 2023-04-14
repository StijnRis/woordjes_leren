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
            return super().create(validated_data)


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


class WordSerializer(UniqueFieldsMixin, serializers.HyperlinkedModelSerializer):
    usage = BasicSentenceSerializer(many=True, read_only=True)
    language = LanguageSerializer(read_only=False)

    class Meta:
        model = Word
        fields = ['pk', 'name', 'language', 'usage']
        read_only_fields = ['pk', 'name']

    def create(self, validated_data):
        try:
            return Language.objects.get(name=validated_data['name'], language=validated_data['language'])
        except ObjectDoesNotExist:
            return super().create(validated_data)


class TranslationSerializer(UniqueFieldsMixin, serializers.HyperlinkedModelSerializer):
    word = WordSerializer(read_only=False)
    translation = WordSerializer(read_only=False)

    class Meta:
        model = Translation
        fields = ['pk', 'wrong_tries', 'correct_tries',
                  'word', 'translation',]
        read_only_fields = ['pk', 'wrong_tries', 'correct_tries',]

    def create(self, validated_data):
        try:
            return Language.objects.get(word=validated_data['word'], translation=validated_data['translation'])
        except ObjectDoesNotExist:
            return super().create(validated_data)


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


class BasicWordlistSerializer(serializers.HyperlinkedModelSerializer):
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


'''
{
    "name": "Test123",
    "visibility": "pl",
    "materials": [
        {
            "translation": {
                "word": {
                    "name": "lopen",
                    "language": {
                        "name": "Nederlands"
                    }
                },
                "translation": {
                    "name": "to walk",
                    "language": {
                        "name": "English"
                    }
                }
            }
        },
        {
            "translation": {
                "word": {
                    "name": "spring",
                    "language": {
                        "name": "Nederlands"
                    }
                },
                "translation": {
                    "name": "to jump",
                    "language": {
                        "name": "English"
                    }
                }
            }
        }
    ]
}
'''
