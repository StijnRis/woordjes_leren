from django.conf import settings
from rest_framework import serializers
from accounts.models import UserProfile
from django.contrib.auth.models import Group


class BasicUserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['pk', 'username']
        read_only_fields = ['pk', 'username']


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['pk', 'username', 'groups']
        read_only_fields = ['pk', 'username', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ['name']
