from django.contrib import admin
from django.apps import apps

# from .models import WordList, Word, Translation, Material

app = apps.get_app_config('quiz')

# Register all models
for model_name, model in app.models.items():
    admin.site.register(model)
