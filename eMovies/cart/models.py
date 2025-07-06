from django.db import models
from eMovies_app.models import User, Movie
from django.conf import settings


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart_items')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    objects = models.Model

    def __str__(self):
        return f"{self.user.username} -> {self.movie.title}"

    class Meta:
        unique_together = ('user', 'movie')
        ordering = ['-added_at']
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

# users/models.py

