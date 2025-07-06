from django.shortcuts import render, get_object_or_404, redirect
from .models import Commentary
from eMovies_app.models import Movie
from .forms import CommentaryForm
from django.contrib.auth.decorators import login_required


def movie_comments(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    comments = movie.comments.all()
    form = CommentaryForm()
    return render(request, 'comments/movie_comments.html', {
        'movie': movie,
        'comments': comments,
        'form': form
    })


@login_required
def add_comment(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = CommentaryForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            comment.save()
    return redirect('movie_comments', movie_id=movie.id)
