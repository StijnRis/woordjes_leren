from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets

from accounts.serializers import UserSerializer, GroupSerializer
from django.contrib.auth.models import Group


# API
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
