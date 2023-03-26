from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'translations', views.TranslationViewSet, basename="translation")
router.register(r'wordlists', views.WordListViewSet, basename="wordlist")
router.register(r'users', views.UserViewSet, basename="user")
router.register(r'words', views.WordViewSet, basename="word")

# app_name = 'quiz'
urlpatterns = [
    path('', views.IndexView.as_view(), name='wordlist-list'),
    path('wordlist/<int:pk>/', views.DetailView.as_view(), name='wordlist-detail'),
    path('wordlist/<int:pk>/exercise/', views.ExerciseView.as_view(), name='wordlist-exercise'),
    path('wordlist/<int:wordlist_id>/answers/', views.answers, name='answers'),
    path('api/', include(router.urls)),
]
