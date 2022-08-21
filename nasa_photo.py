import os
import requests
import datetime
import utils
from dotenv import load_dotenv
from pathlib import Path


def get_nasa_photo(api_key):
        start_date = datetime.date.fromisoformat('2022-06-29')
        end_date = datetime.date.fromisoformat('2022-07-29')
        url = "https://api.nasa.gov/planetary/apod"
        params = {"start_date": f"{start_date}", "end_date": f"{end_date}", "api_key": f"{api_key}"}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()


def save_nasa_ph(nasa_photo, path):
    for photo_number, photo in enumerate(nasa_photo):
        url = photo["url"]
        filename = os.path.join(path, f"nasa{photo_number}.jpg")
        utils.save_photo(filename, url)


def main():
    load_dotenv()
    api_key = os.environ['NASA_API_KEY']
    path = os.path.join(os.getcwd(), "images")
    nasa_photo = get_nasa_photo(api_key)
    save_nasa_ph(nasa_photo, path)

if __name__ == "__main__":
    main()
