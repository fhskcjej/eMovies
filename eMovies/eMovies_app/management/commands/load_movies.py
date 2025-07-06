import json
import os
import requests
from urllib.parse import urlparse
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.conf import settings
from eMovies_app.models import Movie


class Command(BaseCommand):
    help = 'Импорт фильмов из JSON по URL и сохранение постеров в media/poster/'

    def handle(self, *args, **kwargs):
        json_path = os.path.join(settings.BASE_DIR, 'eMovies.json')
        with open(json_path, encoding='utf-8') as file:
            data = json.load(file)

        for item in data['eMovies']:
            title = item['title']
            if Movie.objects.filter(title=title).exists():
                self.stdout.write(self.style.WARNING(f"⏩ Уже есть: {title}"))
                continue

            poster_url = item['poster']
            poster_filename = os.path.basename(urlparse(poster_url).path)

            try:
                response = requests.get(poster_url)
                response.raise_for_status()
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Ошибка при загрузке {poster_url}: {e}"))
                continue

            movie = Movie(
                title=item['title'],
                release_date=item['release_date'],
                description=item['description'],
                rating=item['rating'],
                genre=item['genre'],
                director=item['director'],
                cast=item['cast'],
                price=item['price']
            )

            movie.poster.save(poster_filename, ContentFile(response.content), save=True)
            self.stdout.write(self.style.SUCCESS(f"Добавлен: {title}"))