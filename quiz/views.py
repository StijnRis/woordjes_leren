from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from quiz.models import List

# Create your views here.
def index(request):
    latest_question_list = List.objects.order_by('-pub_date')[:5]
    template = loader.get_template('quiz/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    # return HttpResponse("Hello, world. You're at the quiz index.")

def detail(request, list_id):
    list = get_object_or_404(List, pk=list_id)
    return render(request, 'quiz/detail.html', {'list': list})

def words(request, list_id):
    response = "You're looking at the words of question %s."
    return HttpResponse(response % list_id)
