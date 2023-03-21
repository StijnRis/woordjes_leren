from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from quiz.models import WordList, Word, Translation

def index(request):
    response = "Welcome!"
    return HttpResponse(response)

def word_lists(request):
    word_lists = WordList.objects.order_by('-published_date')[:5]
    return render(request, 'quiz/word_lists.html', {'word_lists': word_lists})

def word_list_detail(request, word_list_id):
    list = get_object_or_404(WordList, pk=word_list_id)
    return render(request, 'quiz/detail.html', {'word_list': list})

def word_list_exercise(request, word_list_id):
    list = get_object_or_404(WordList, pk=word_list_id)
    return render(request, 'quiz/exercise.html', {'word_list': list})

def multipleChoiceAnswers(request, translation_id):
    translation = get_object_or_404(Translation, pk=translation_id)
    try:
        selected_choice = Word.objects.all().get(pk=request.POST['choice'])
    except (KeyError, Word.DoesNotExist):
        return render(request, 'quiz/exercise.html', {
            'question': translation,
            'error_message': "You didn't select a choice.",
        })
    else:
        translation.tries += 1
        translation.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:word_list', args=(translation.pk,)))

    


