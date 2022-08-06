import requests


def save_photo(filename, url, params):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(filename, 'wb') as f:
        f.write(response.content)     