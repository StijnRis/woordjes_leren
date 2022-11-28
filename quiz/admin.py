from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import List, Question

admin.site.register(List)
admin.site.register(Question)