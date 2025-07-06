from django.db import models
from eMovies_app.models import Movie
from users.models import User, AbstractUser
from django.conf import settings


class Commentary(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    objects = models.Model

    def __str__(self):
        return f"{self.user.username} о {self.movie.title}"

    class Meta:
        ordering = ['-added_at']
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
