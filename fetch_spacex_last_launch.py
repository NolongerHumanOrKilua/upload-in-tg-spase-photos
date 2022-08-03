import requests
import datetime
import argparse
import utils


def images():
    id = "5eb87d46ffd86e000604b388"
    url = f"https://api.spacexdata.com/v5/launches/{id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["links"]['flickr']['original']


def fetch_spacex_last_launch(images):
    i = 0
    for url in images:
        filename = f'images/hubble{i}.jpeg'
        utils.save_photo(filename, url)
        i += 1


images = images()
fetch_spacex_last_launch(images)
