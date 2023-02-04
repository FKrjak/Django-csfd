from django.shortcuts import render

from csfd.forms import MovieForm
from csfd.models import Movie, Actor
from csfd.functions.normalize import normalize


def index(request):
    # Main index function

    movies = []
    actors = []
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movies = Movie.objects.filter(
                unaccent_movie_name__contains=normalize(form.cleaned_data["input"])
            )[:20]
            actors = Actor.objects.filter(
                unaccent_name__contains=normalize(form.cleaned_data["input"])
            )[:20]
    else:
        form = MovieForm()

    return render(
        request, "index.html", {"form": form, "movies": movies, "actors": actors}
    )


def movie(request, id):
    # Show movie function

    movie = Movie.objects.filter(unaccent_movie_name=id.replace("_", " "))[0]
    actors = Actor.objects.filter(movies__pk=movie.id)
    return render(request, "movie.html", {"movie": movie, "actors": actors})


def actor(request, id):
    # Show actor function

    actor = Actor.objects.filter(unaccent_name=id.replace("_", " "))[0]
    movies = actor.movies.all()
    return render(request, "actor.html", {"movies": movies, "actor": actor})
