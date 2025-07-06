# purchases/models.py
from django.db import models
from django.contrib.auth.models import User
from eMovies_app.models import Movie
from django.conf import settings


class Purchase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='purchases')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    purchased_at = models.DateTimeField(auto_now_add=True)
    objects = models.Model

    def __str__(self):
        return f"{self.user.username} купил {self.movie.title}"

    class Meta:
        unique_together = ('user', 'movie')
        ordering = ['-purchased_at']
        verbose_name = "Покупка"
        verbose_name_plural = "Покупки"