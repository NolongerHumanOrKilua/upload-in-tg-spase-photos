import requests


def save_photo(filename, image, params=None):
    response = requests.get(image, params=params)
    response.raise_for_status()
    with open(filename, "wb") as f:
        f.write(response.content)
