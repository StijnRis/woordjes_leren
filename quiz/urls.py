from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'translations', views.TranslationViewSet, basename="api-translation")
router.register(r'wordlists', views.WordListViewSet, basename="api-wordlist")
router.register(r'users', views.UserViewSet, basename="api-user")
router.register(r'words', views.WordViewSet, basename="api-word")

# app_name = 'quiz'
urlpatterns = [
    path('', views.index, name='index'),
    path('languages/', views.LanguageListView.as_view(), name='language-list'),
    path('language/<int:pk>/', views.LanguageDetailView.as_view(), name='language-detail'),
    path('wordlists/', views.WordlistListView.as_view(), name='wordlist-list'),
    path('my_wordlists/', views.WordlistFromUserListView.as_view(), name='my-wordlist-list'),
    path('wordlist/<int:pk>/', views.WordlistDetailView.as_view(), name='wordlist-detail'),
    path('wordlist/<int:pk>/edit', views.edit_wordlist, name='wordlist-edit'),
    path('wordlist/<int:pk>/exercise/', views.WordlistExerciseView.as_view(), name='wordlist-exercise'),
    # path('wordlist/<int:wordlist_id>/answers/', views.answers, name='answers'),
    path('api/', include(router.urls)),
]
 