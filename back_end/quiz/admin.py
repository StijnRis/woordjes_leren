from django.contrib import admin
from django.apps import apps

from .models import Wordlist, Word, Translation, Language, Sentence, Material


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('wordlist', 'translation')
    readonly_fields = ('pk',)


class MaterialInline(admin.TabularInline):
    model = Material
    extra = 0
    readonly_fields = ('pk',)


@admin.register(Wordlist)
class WordlistAdmin(admin.ModelAdmin):
    readonly_fields = ('pk',)
    list_display = ('name', 'owner', 'visibility')
    inlines = (MaterialInline, )
    list_filter = ('visibility', 'owner')


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('name', 'language')
    list_filter = ('language', )
    readonly_fields = ('pk',)


class WordInline(admin.TabularInline):
    model = Word.usage.through
    extra = 0
    readonly_fields = ('pk',)


@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    list_display = ('word', 'translation', 'difficulty')
    fieldsets = (
        (None, {
            'fields': ('word', 'translation')
        }),
        ('Stats', {
            'fields': ('difficulty', 'correct_tries', 'wrong_tries')
        }),
    )
    readonly_fields = ('pk',)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', )
    readonly_fields = ('pk',)


@admin.register(Sentence)
class SentenceAdmin(admin.ModelAdmin):
    list_display = ('language', 'sentence')
    list_filter = ('language', )
    inlines = [WordInline]
    readonly_fields = ('pk',)
