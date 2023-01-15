from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from quiz.models import WordList

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

def word_list_edit(request, word_list_id):
    list = get_object_or_404(WordList, pk=word_list_id)
    return render(request, 'quiz/edit.html', {'word_list': list})


