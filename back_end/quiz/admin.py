from django.contrib import admin
from django.apps import apps

from .models import Wordlist, Word, Translation, Language, Sentence, Material, Source


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('name', )


# @admin.register(Material)
# class MaterialAdmin(admin.ModelAdmin):
#     list_display = ('wordlist', 'translation')
#     readonly_fields = ('pk',)


class MaterialInline(admin.TabularInline):
    model = Material
    extra = 0


@admin.register(Wordlist)
class WordlistAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'visibility')
    # inlines = (MaterialInline, )
    list_filter = ('visibility', 'owner')


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('name', 'language')
    list_filter = ('language', )


class WordInline(admin.TabularInline):
    model = Word.usage.through
    extra = 0


@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    list_display = ('word', 'translation')
    fieldsets = (
        (None, {
            'fields': ('word', 'translation')
        }),
        ('Stats', {
            'fields': ('correct_tries', 'wrong_tries')
        }),
    )


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Sentence)
class SentenceAdmin(admin.ModelAdmin):
    list_display = ('language', 'sentence')
    list_filter = ('language', )
    inlines = [WordInline]
