from django.conf import settings
from rest_framework import serializers
from accounts.models import UserProfile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # wordlists = serializers.HyperlinkedRelatedField(
    #     view_name='user-detail', many=True, queryset=Wordlist.objects.all())

    class Meta:
        model = UserProfile
        fields = ['id', 'username']
