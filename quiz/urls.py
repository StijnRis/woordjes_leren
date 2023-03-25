from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'quiz'
urlpatterns = [
    path('', views.IndexView.as_view(), name='word_lists'),
    path('word_list/<int:pk>/', views.DetailView.as_view(), name='word_list'),
    path('word_list/<int:pk>/exercise/', views.ExerciseView.as_view(), name='word_list_exercise'),
    path('word_list/<int:word_list_id>/answers/', views.answers, name='answers'),
    path('translations/', views.TranslationList.as_view()),
    path('translations/<int:pk>/', views.TranslationDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
