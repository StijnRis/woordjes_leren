from django.conf import settings
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
from quiz.permissions import IsOwnerOrReadOnly
from quiz.serializers import TranslationSerializer, UserSerializer, WordListSerializer, WordSerializer
from quiz.models import Wordlist, Word, Translation, Language, Sentence
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
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_languages = Language.objects.all().count()
    num_words = Word.objects.all().count()
    num_translations = Translation.objects.count()
    num_practiced_translations = Translation.objects.filter(wrong_tries__gt=0, correct_tries__gt=0).count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits

    context = {
        'num_languages': num_languages,
        'num_words': num_words,
        'num_translations': num_translations,
        'num_practiced_translations': num_practiced_translations,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'quiz/index.html', context=context)


class LanguageListView(generic.ListView):
    model = Language
    paginate_by = 10
    template_name = 'quiz/language_list.html'
    context_object_name = 'languages'

    def get_queryset(self):
        return Language.objects.all()[:5]


class LanguageDetailView(generic.DetailView):
    model = Language
    template_name = 'quiz/language_detail.html'
    context_object_name = 'language'
    

class WordlistListView(generic.ListView):
    model = Wordlist
    paginate_by = 10
    template_name = 'quiz/wordlist_list.html'
    context_object_name = 'latest_wordlists'

    def get_queryset(self):
        return Wordlist.objects.order_by('-date_published')[:5]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super().get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context

class WordlistFromUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing the wordlists the current user owns."""
    model = Wordlist
    template_name = 'quiz/wordlist_personal_list.html'
    paginate_by = 10
    context_object_name = 'wordlists'

    def get_queryset(self):
        return (
            Wordlist.objects.filter(owner=self.request.user)
            .order_by('name')
        )

class WordlistDetailView(generic.DetailView):
    model = Wordlist
    template_name = 'quiz/wordlist_detail.html'
    context_object_name = 'wordlist'


class WordlistExerciseView(generic.DetailView):
    model = Wordlist
    template_name = 'quiz/wordlist_exercise.html'
    context_object_name = 'wordlist'


def answers(request, wordlist_id):
    wordlist = get_object_or_404(Wordlist, pk=wordlist_id)
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
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
