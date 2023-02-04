from django.db import models


class Movie(models.Model):
    movie_name = models.CharField(max_length=200)
    unaccent_movie_name = models.CharField(max_length=200, default="")
    movie_url = models.CharField(max_length=200)

    class Meta:
        ordering = ["movie_name"]

    def __str__(self):
        return self.movie_name

    def __url__(self):
        return self.movie_url


class Actor(models.Model):
    name = models.CharField(max_length=200)
    unaccent_name = models.CharField(max_length=200, default="")
    movies = models.ManyToManyField(Movie)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def __movies__(self):
        return self.movies.all()


class Loaded(models.Model):
    init_load = models.BooleanField(default=False)
