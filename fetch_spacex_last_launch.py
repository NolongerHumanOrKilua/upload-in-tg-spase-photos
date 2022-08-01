import requests
import datetime
import argparse


def images():
    id = "5eb87d46ffd86e000604b388"
    url = f"https://api.spacexdata.com/v5/launches/{id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["links"]['flickr']['original']


def fetch_spacex_last_launch(images):
    i = 0
    for image in images:
        filename = f'images/hubble{i}.jpeg'
        response = requests.get(image)
        response.raise_for_status()
        with open(filename, 'wb') as f:
            f.write(response.content)
        i += 1


images = images()
fetch_spacex_last_launch(images)