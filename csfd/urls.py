from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("movie/<str:id>", views.movie, name="movie"),
    path("actor/<str:id>", views.actor, name="actor"),
]
