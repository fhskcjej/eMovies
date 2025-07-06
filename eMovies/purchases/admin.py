from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import *


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'purchased_at')
    list_filter = ('purchased_at',)
    search_fields = ('user__username', 'movie__title')


