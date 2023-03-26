from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.views import generic
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User, Group
from quiz.permissions import IsOwnerOrReadOnly
from quiz.serializers import TranslationSerializer, UserSerializer, WordListSerializer, WordSerializer
from quiz.models import Wordlist, Word, Translation
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework import viewsets

class IndexView(generic.ListView):
    template_name = 'quiz/wordlists.html'
    context_object_name = 'latest_wordlists'

    def get_queryset(self):
        return Wordlist.objects.order_by('-published_date')[:5]


class DetailView(generic.DetailView):
    model = Wordlist
    template_name = 'quiz/detail.html'
    context_object_name = 'wordlist'


class ExerciseView(generic.DetailView):
    model = Wordlist
    template_name = 'quiz/exercise.html'
    context_object_name = 'wordlist'

def answers(request, wordlist_id):
    wordlist = get_object_or_404(Wordlist, pk=wordlist_id)
    print(request.POST)
    for material in wordlist.material_set.all():
        try:
            translation = material.translation
            print(request.POST[f'translation_{translation.id}_choice'])
            selected_word = Word.objects.all().get(
                pk=request.POST[f'translation_{translation.id}_choice'])
        except (KeyError, Word.DoesNotExist) as e:
            messages.error(request, "You didn't select a choice.")
            return HttpResponseRedirect(reverse('quiz:wordlist_exercise', args=(wordlist.id, )))
        else:
            if selected_word == translation.word_two:
                translation.correct_tries += 1
            else:
                translation.wrong_tries += 1
            translation.save()
    return HttpResponseRedirect(reverse('quiz:wordlists'))

class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class WordListViewSet(viewsets.ModelViewSet):
    queryset = Wordlist.objects.all()
    serializer_class = WordListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TranslationViewSet(viewsets.ModelViewSet):
    queryset = Translation.objects.all()
    serializer_class = TranslationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
