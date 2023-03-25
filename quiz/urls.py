from django.urls import path

from . import views

app_name = 'quiz'
urlpatterns = [
    path('', views.IndexView.as_view(), name='word_lists'),
    path('word_list/<int:pk>/', views.DetailView.as_view(), name='word_list'),
    path('word_list/<int:pk>/exercise/', views.ExerciseView.as_view(), name='word_list_exercise'),
    path('word_list/<int:word_list_id>/answers/', views.answers, name='answers'),
]