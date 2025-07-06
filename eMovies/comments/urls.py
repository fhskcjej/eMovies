from django.urls import path
from . import views

urlpatterns = [
    path('movie/<int:movie_id>/comments/', views.movie_comments, name='movie_comments'),
    path('movie/<int:movie_id>/comments/add/', views.add_comment, name='add_comment'),
]