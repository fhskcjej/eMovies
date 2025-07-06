from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from comments.models import Commentary


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'added_at')
    list_filter = ('added_at',)
    search_fields = ('user__username', 'movie__title', 'text')

# Register your models here.
