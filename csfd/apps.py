from django.apps import AppConfig
from csfd.functions.scrapper import get_data


class CsfdConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "csfd"

    def ready(self):

        from csfd.models import Movie, Actor, Loaded

        if not Loaded.objects.all().count():
            movies, actors = get_data(Movie, Actor)
            Movie.objects.bulk_create(movies)
            for index, movie in enumerate(movies):
                for actor_dict in actors[index]:
                    actor = actor_dict["model"]
                    db_entity, created = Actor.objects.get_or_create(
                        name=actor.name, unaccent_name=actor.unaccent_name
                    )
                    db_entity.movies.add(Movie.objects.get(movie_url=actor_dict["url"]))
            Loaded.objects.get_or_create(init_load=True)  # Loaded
