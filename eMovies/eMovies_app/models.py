from django.db import models
from django.contrib.auth.models import AbstractUser
import requests
from users.models import *



class Director(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='directors/', null=True, blank=True)
    objects = models.Model

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Режиссёр"
        verbose_name_plural = "Режиссёры"


class Actor(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='actors/', null=True, blank=True)
    objects = models.Model

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Актёр"
        verbose_name_plural = "Актёры"


class Genre(models.Model):
    name = models.CharField(max_length=50)
    objects = models.Model

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"



class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, related_name='eMovies')
    actors = models.ManyToManyField(Actor, related_name='eMovies')
    genres = models.ManyToManyField(Genre, related_name='eMovies')
    kinopoisk_id = models.IntegerField(unique=True, default=0)
    trailer_id = models.CharField(max_length=20, blank=True, null=True)
    poster = models.ImageField(upload_to='poster/')
    summary = models.TextField()
    rating = models.FloatField(default=0.0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    objects = models.Model

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-release_date']
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

