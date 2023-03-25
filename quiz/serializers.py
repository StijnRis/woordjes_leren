from rest_framework import serializers
from quiz.models import Language, Word, Translation, WordList
from django.contrib.auth.models import User

class WordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Word
        fields = ['name']


class TranslationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Translation
        fields = ['id', 'word_one', 'word_two', 'wrong_tries', 'correct_tries', 'difficulty']


class WordListSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)#ReadOnlyField(source='owner.username')

    class Meta:
        model = WordList
        fields = ['owner', 'name', 'published_date', 'translations']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    word_lists = serializers.HyperlinkedRelatedField(view_name='word_list-detail', many=True, queryset=WordList.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'word_lists']