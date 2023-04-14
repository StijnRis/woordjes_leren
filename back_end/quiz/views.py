from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from quiz.forms import EditWordlistForm
from quiz import permissions as customPermissions
from quiz import serializers
from quiz.models import Wordlist, Word, Translation, Language, Sentence, Material
from django.http import HttpResponse
from rest_framework.reverse import reverse
from rest_framework import viewsets, permissions
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def is_wordlist_owner(func):
    def check_and_call(request, *args, **kwargs):
        # user = request.user
        # print user.id
        pk = kwargs["pk"]
        wordlist = Wordlist.objects.get(pk=pk)
        if not (wordlist.owner == request.user):
            return HttpResponse("It is not yours ! You are not permitted !",
                                content_type="application/json", status=403)
        return func(request, *args, **kwargs)
    return check_and_call


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_languages = Language.objects.all().count()
    num_words = Word.objects.all().count()
    num_translations = Translation.objects.count()
    num_practiced_translations = Translation.objects.filter(
        wrong_tries__gt=0, correct_tries__gt=0).count()

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


class WordlistFromUserListView(LoginRequiredMixin, generic.ListView):
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


@login_required
@is_wordlist_owner
def edit_wordlist(request, pk):
    """View function for editing a specific wordlist by the owner."""
    wordlist = get_object_or_404(Wordlist, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = EditWordlistForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            wordlist.name = form.cleaned_data['name']
            wordlist.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('wordlist-detail', kwargs={'pk': pk}))

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_name = 'a beatifull name'
        form = EditWordlistForm(initial={'renewal_date': proposed_name})

    context = {
        'form': form,
        'wordlist': wordlist,
    }

    return render(request, 'quiz/wordlist_edit.html', context)

# def answers(request, wordlist_id):
#     wordlist = get_object_or_404(Wordlist, pk=wordlist_id)
#     for material in wordlist.material_set.all():
#         try:
#             translation = material.translation
#             print(request.POST[f'translation_{translation.id}_choice'])
#             selected_word = Word.objects.all().get(
#                 pk=request.POST[f'translation_{translation.id}_choice'])
#         except (KeyError, Word.DoesNotExist) as e:
#             messages.error(request, "You didn't select a choice.")
#             return HttpResponseRedirect(reverse('quiz:wordlist_exercise', args=(wordlist.id, )))
#         else:
#             if selected_word == translation.word_two:
#                 translation.correct_tries += 1
#             else:
#                 translation.wrong_tries += 1
#             translation.save()
#     return HttpResponseRedirect(reverse('quiz:wordlists'))


'''
API vieuws start from here
'''


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = serializers.LanguageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SentenceViewSet(viewsets.ModelViewSet):
    queryset = Sentence.objects.all()
    serializer_class = serializers.SentenceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = serializers.WordSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class WordlistViewSet(viewsets.ModelViewSet):
    queryset = Wordlist.objects.all()
    serializer_class = serializers.WordlistSerializer
    permission_classes = [
        permissions.IsAuthenticated, customPermissions.IsOwner | customPermissions.IsPublicReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.BasicWordlistSerializer
        return serializers.WordlistSerializer


class TranslationViewSet(viewsets.ModelViewSet):
    queryset = Translation.objects.all()
    serializer_class = serializers.TranslationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = serializers.MaterialSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
