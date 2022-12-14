import argparse
import os

import requests

import utils


def get_images(launch_id):
    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["links"]["flickr"]["original"]


def get_fetch_spacex_last_launch(images, path):
    for photo_num, image in enumerate(images):
        filename = os.path.join(path, f"spacex{photo_num}.jpg")
        utils.save_photo(filename, image)


def main():
    path = os.path.join(os.getcwd(), "images")
    os.makedirs(path, exist_ok=True)
    parser = argparse.ArgumentParser()
    parser.add_argument("-launch_id", default="latest")
    args = parser.parse_args()
    images = get_images(args.launch_id)
    get_fetch_spacex_last_launch(images, path)


if __name__ == "__main__":
    main()
