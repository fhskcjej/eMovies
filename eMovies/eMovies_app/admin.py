from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import *


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'director', 'rating', 'price')
    list_filter = ('release_date', 'genres', 'director')
    search_fields = ('title', 'summary')
    filter_horizontal = ('actors', 'genres')
    autocomplete_fields = ('director',)
    ordering = ('-release_date',)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


