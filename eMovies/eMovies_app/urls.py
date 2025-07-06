from django.contrib import admin
from django.urls import path, include
from eMovies_app import views  # view-функция home

from eMovies_app.views import import_movies

app_name = 'eMovies'


urlpatterns = [
    path('import_movies/', import_movies),
    # path('', views.movie_list, name='movie_list'),  # обязательно name="movie_list"
    path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
]