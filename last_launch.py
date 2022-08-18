from ast import arguments, parse
from email.mime import image
import requests
import datetime
import argparse
import utils
import os
from pathlib import Path
import argparse


def get_images(input_id):
    url = f"https://api.spacexdata.com/v5/launches/{input_id}" 
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["links"]['flickr']['original']


def get_fetch_spacex_last_launch(images, path):
    for photo_num, image in enumerate(images):
        filename = os.path.join(path, f"spacex{photo_num}.jpg")
        utils.save_photo(filename, image, params=None)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_id", type=str, default="latest")
    args = parser.parse_args()
    path = os.path.join(os.getcwd(), "images")
    os.makedirs(path, exist_ok=True)
    images = get_images(args.input_id)
    get_fetch_spacex_last_launch(images, path)


if __name__ == "__main__":
    main()
