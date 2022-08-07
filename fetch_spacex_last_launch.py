from email.mime import image
import requests
import datetime
import argparse
import utils
import os
from pathlib import Path


def get_images():
    id = "5eb87d46ffd86e000604b388"
    url = f"https://api.spacexdata.com/v5/launches/{id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["links"]['flickr']['original']


def get_fetch_spacex_last_launch(get_images, path):
    for photo_num, image in enumerate(get_images):
        filename = os.path.join(path, f"spacex{photo_num}.jpg")
        utils.save_photo(filename, image, params=None)


def main():
    path = os.path.join(os.getcwd(), "images")
    get_images = get_images()
    get_fetch_spacex_last_launch(get_images)


if __name__ == "__main__":
    main()
