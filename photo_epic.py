import os
import requests
import datetime
import utils
from dotenv import load_dotenv
from _collections_abc import MutableMapping
from pathlib import Path


def get_epic_photo(epic_image, api_key, path):
    for photo_number, photo in enumerate(epic_image):
        date = photo["date"].split(maxsplit=1)[0]
        image = photo["image"]
        photo_date = datetime.date.fromisoformat(date)
        photo_date = photo_date.strftime("%Y/%m/%d")
        params = {"api_key": api_key}
        url = f"https://api.nasa.gov/EPIC/archive/natural/{photo_date}/png/{image}.png"
        filename = os.path.join(path, f"epic{photo_number}.jpg")
        utils.save_photo(filename, url, params)


def get_epic_image(api_key):
    params = {"api_key": api_key}
    url = f"https://api.nasa.gov/EPIC/api/natural/images"
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def main():
    load_dotenv()
    path = os.path.join(os.getcwd(), "images")
    api_key = os.environ['NASA_API_KEY']
    epic_image = get_epic_image(api_key)
    get_epic_photo(epic_image, api_key, path)


if __name__ == "__main__":
    main()
