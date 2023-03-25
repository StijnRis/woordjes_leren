from rest_framework import serializers
from quiz.models import Language, Word, Translation, WordList
from django.contrib.auth.models import User


class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = ['id', 'word_one', 'word_two', 'wrong_tries', 'correct_tries', 'difficulty']


class UserSerializer(serializers.ModelSerializer):
    word_lists = serializers.PrimaryKeyRelatedField(many=True, queryset=WordList.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'word_lists']