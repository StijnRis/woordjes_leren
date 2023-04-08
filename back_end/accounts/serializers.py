from django.conf import settings
from rest_framework import serializers
from accounts.models import UserProfile
from django.contrib.auth.models import Group


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # wordlists = serializers.HyperlinkedRelatedField(
    #     view_name='user-detail', many=True, queryset=Wordlist.objects.all())

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ['name']
