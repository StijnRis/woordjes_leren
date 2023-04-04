from django.conf import settings
from rest_framework import serializers
from quiz.models import Language, Word, Translation, Wordlist


class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ['name']


class TranslationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Translation
        fields = ['id', 'word', 'translation',
                  'wrong_tries', 'correct_tries', 'difficulty']


class WordListSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(
        view_name='wordlist-detail', read_only=True)  # ReadOnlyField(source='owner.username')

    class Meta:
        model = Wordlist
        fields = ['owner', 'name', 'published_date', 'translations']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    wordlists = serializers.HyperlinkedRelatedField(
        view_name='user-detail', many=True, queryset=Wordlist.objects.all())

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ['id', 'username', 'wordlists']
