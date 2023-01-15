from django.urls import path

from . import views

app_name = 'quiz'
urlpatterns = [
    path('', views.word_lists, name='word_lists'),
    path('<int:word_list_id>/', views.word_list_detail, name='word_list_detail'),
    path('<int:word_list_id>/exercise/', views.word_list_exercise, name='word_list_exercise'),
    path('<int:word_list_id>/exercise/answer', views.word_list_exercise, name='answer'),
    path('<int:word_list_id>/edit/', views.word_list_edit, name='word_list_edit'),
]