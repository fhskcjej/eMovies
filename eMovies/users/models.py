from django.db import models
from django.contrib.auth.models import AbstractUser
from eMovies_app.models import *
import requests
from django.conf import settings


# Расширенный пользователь
class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, default='media/avatars/default.jpeg')
    card = models.OneToOneField('Card', on_delete=models.SET_NULL, null=True, related_name='card_owner')

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username']
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Card(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_card')
    card_number = models.CharField(max_length=16)
    expiration_date = models.CharField(max_length=5)
    CVV = models.CharField(max_length=3)
    objects = models.Model

    def __str__(self):
        return f"{self.user.username} – {self.card_number[-4:]}"

    class Meta:
        verbose_name = "Карта"
        verbose_name_plural = "Карты"

# Create your models here.
