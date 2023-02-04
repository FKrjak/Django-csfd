from unidecode import unidecode


def normalize(text: str):
    return unidecode(text).lower()
