from django.urls import path

from . import views

app_name = 'quiz'
urlpatterns = [
    path('', views.word_lists, name='word_lists'),
    path('word_list/<int:word_list_id>/', views.word_list_detail, name='word_list'),
    path('word_list/<int:word_list_id>/exercise/', views.word_list_exercise, name='word_list_exercise'),
    path('translation/<int:translation_id>/multiple_choice_answer', views.multipleChoiceAnswers, name='answer'),
]