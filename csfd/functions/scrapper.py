import itertools
from csfd.functions.loader import Loader
from csfd.functions.parsers import parse_top, parse_movie

TOP_X = 3


def get_data(movie_type, actor_type):
    loader = Loader()
    movies = list(
        itertools.chain(
            *loader.get_urls(
                [
                    f"https://www.csfd.cz/zebricky/filmy/nejlepsi/?from={100*count}"
                    for count in range(TOP_X)
                ],
                parse_top,
                movie_type,
            )
        )
    )

    actors = loader.get_urls(
        [f"https://www.csfd.cz/{movie.movie_url}prehled/" for movie in movies],
        parse_movie,
        actor_type,
    )
    return movies, actors
