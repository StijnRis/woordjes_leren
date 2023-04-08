from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename="userprofile")
router.register(r'group', views.GroupViewSet, basename="group")

# app_name = 'quiz'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('api/', include(router.urls)),
]
