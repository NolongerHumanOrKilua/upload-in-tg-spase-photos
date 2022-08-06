import os
import requests
import datetime
import utils
from dotenv import load_dotenv
from _collections_abc import MutableMapping

api_key = os.environ['NASA_API_KEY']


def epic_photo(epic_image, api_key):
    i = 0
    for photo in epic_image:
        date = photo["date"]
        date = date.split(maxsplit=1)
        date = date[0]
        image = photo["image"]
        photo_date = datetime.date.fromisoformat(f'{date}')
        photo_date = photo_date.strftime("%Y/%m/%d")
        key = api_key
        params = {api_key: key}
        url = f"https://api.nasa.gov/EPIC/archive/natural/{photo_date}/png/{image}.png"
        filename = f'images/epic{i}.jpg'
        utils.save_photo(filename, url, params)
        i += 1


def epic_image(api_key):
    key = api_key
    params = {api_key: key}
    url = f"https://api.nasa.gov/EPIC/api/natural/images"
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def main():
    load_dotenv()
    epic_image = epic_image()
    epic_photo(epic_image)


if __name__ == "__main__":
    main()
