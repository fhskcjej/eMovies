from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import *


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'added_at')
    list_filter = ('added_at',)
    search_fields = ('user__username', 'movie__title')


# Register your models here.
