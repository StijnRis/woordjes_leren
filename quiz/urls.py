from django.urls import path

from . import views

app_name = 'quiz'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:list_id>/', views.detail, name='detail'),
    path('<int:list_id>/words/', views.words, name='results'),
]