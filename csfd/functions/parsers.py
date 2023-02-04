import re
from bs4 import BeautifulSoup
from typing import List
from csfd.functions.normalize import normalize


def parse_top(site: str, model_type, url: str):
    output = []
    soup = BeautifulSoup(site, "html.parser")
    for movie in soup.find_all("a", {"class": "film-title-name"}):
        output.append(
            model_type(
                movie_name=movie.get("title"),
                movie_url=movie.get("href"),
                unaccent_movie_name=normalize(movie.get("title")),
            )
        )
    return output


def parse_movie(site: str, model_type, url: str):
    output = []
    soup = BeautifulSoup(site, "html.parser")
    get_first = soup.find_all(text=re.compile("Hrají"))[0].parent.parent
    for actor in get_first.find_all("a"):
        if actor.text != "více":
            output.append(
                {
                    "url": url.replace("https://www.csfd.cz/", "").replace(
                        "prehled/", ""
                    ),
                    "model": model_type(
                        name=actor.text, unaccent_name=normalize(actor.text)
                    ),
                }
            )
    return output
