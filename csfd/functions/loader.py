import concurrent.futures
import requests
from typing import List, Callable


CONNECTIONS = 20  # LIVE CONNECTIONS
TIMEOUT = 20  # CONNECTION TIMEOUT


class Loader:
    def __init__(self) -> None:
        pass

    def get_urls(self, urls: List[str], parser: Callable, model_type):
        output = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
            future_to_url = (
                executor.submit(self.load_url, url, parser, model_type) for url in urls
            )
            for future in concurrent.futures.as_completed(future_to_url):
                try:
                    data = future.result()
                except Exception as exc:
                    data = str(type(exc))
                finally:
                    output.append(data)
        return output

    def load_url(self, url: str, parser: Callable, model_type):
        ans = requests.get(
            url,
            headers={
                "User-Agent": "PostmanRuntime/7.29.2",
            },
            timeout=TIMEOUT,
        )
        return parser(ans.text, model_type, url)
