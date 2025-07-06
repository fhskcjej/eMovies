import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from eMovies_app.models import Movie


class Command(BaseCommand):
    help = "Получает YouTube ID трейлеров с Кинопоиска"

    def handle(self, *args, **kwargs):
        headers = {"User-Agent": "Mozilla/5.0"}

        movies = Movie.objects.filter(kinopoisk_id__isnull=False, youtube_trailer_id__isnull=True)

        for film in movies:
            url = f"https://www.kinopoisk.ru/film/{film.kinopoisk_id}/"
            response = requests.get(url, headers=headers)

            if response.status_code != 200:
                self.stdout.write(f"❌ Ошибка загрузки: {film.title}")
                continue

            soup = BeautifulSoup(response.text, "html.parser")
            trailer_tag = soup.find("a", class_="trailer")

            if trailer_tag and trailer_tag.get("data-youtube-id"):
                yt_id = trailer_tag["data-youtube-id"]
                film.youtube_trailer_id = yt_id
                film.save()
                self.stdout.write(f"✅ {film.title}: YouTube ID {yt_id}")
            else:
                self.stdout.write(f"⚠ Трейлер не найден: {film.title}")