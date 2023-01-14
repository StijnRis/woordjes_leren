from django.urls import path

from . import views

app_name = 'quiz'
urlpatterns = [
    path('', views.word_lists, name='word_lists'),
    path('<int:word_list_id>/', views.detail, name='word_list_detail'),
    path('<int:word_list_id>/exercise/', views.words, name='word_list_exercise'),
    path('<int:word_list_id>/edit/', views.words, name='word_list_edit'),
]