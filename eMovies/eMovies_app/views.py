from bs4 import BeautifulSoup
import json
import os
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.core.files import File
import requests

from .forms import *
from eMovies_app.models import Movie, Director, Actor, Genre
from purchases.models import *
from users.models import Card

from django.contrib import messages
from django.utils import timezone


def fetch_trailer_from_kinopoisk(film):
    url = f"https://www.kinopoisk.ru/film/{film.kinopoisk_id}/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        trailer_link = soup.find("a", {"class": "trailer"})  # зависит от структуры сайта
        if trailer_link:
            film.trailer_id = trailer_link["data-youtube-id"]  # поле trailer_id
            film.save()
            return trailer_link["data-youtube-id"]
    return None


def import_movies(request):
    def load(path):
        with open(path, mode="r", encoding="utf-8") as file:
            return json.load(file)


    flag = True
    if flag:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        json_path = os.path.join(BASE_DIR, 'movies.json')
        data = load(json_path)
        movies_data = data.get("movies", [])
        print(movies_data)

        # Очистка предыдущих записей
        Movie.objects.all().delete()
        Director.objects.all().delete()
        Actor.objects.all().delete()
        Genre.objects.all().delete()

        for entry in movies_data:
            # Режиссёр
            director_name = entry.get("director")
            director, _ = Director.objects.get_or_create(name=director_name)

            # Создание фильма
            movie = Movie.objects.create(
                title=entry["title"],
                release_date=int(entry["release_date"]),
                director=director,
                kinopoisk_id=entry.get("kinopoisk_id"),
                trailer_id=entry.get("trailer_id"),
                summary=entry.get("description", ""),
                rating=float(entry.get("rating", 0.0)),
                price=float(entry.get("price", 0.0)),
            )

            # Постер
            poster_filename = entry.get("poster")
            poster_path = os.path.join(settings.BASE_DIR, 'media', 'poster', poster_filename)
            if os.path.exists(poster_path):
                with open(poster_path, "rb") as f:
                    movie.poster.save(poster_filename, File(f), save=True)

            # Актёры
            for actor_name in entry.get("actors", []):
                actor, _ = Actor.objects.get_or_create(name=actor_name)
                movie.actors.add(actor)

            # Жанры
            for genre_name in entry.get("genres", []):
                genre, _ = Genre.objects.get_or_create(name=genre_name)
                movie.genres.add(genre)

            print(f"Импортировано: {movie.title}")

    return HttpResponseRedirect("/")



def movie_detail(request, pk):
    movie = Movie.objects.filter(pk=pk).first()
    if movie:
        return render(request, 'eMovies/movie_detail.html', {'movie': movie})
    else:
        raise Http404("Фильм не найден")


def home(request):
    featured_movies = Movie.objects.order_by('-rating')[:3]  # топ-3 по рейтингу
    latest_movies = Movie.objects.order_by('-release_date')[:8]
    return render(request, 'home.html', {'featured_movies': featured_movies,
                                         'latest_movies': latest_movies})


def movie_list(request):
    movies = Movie.objects.all()
    print(f"Найдено фильмов: {movies.count()}")
    return render(request, 'eMovies/movie_list.html', {'movies': movies})

