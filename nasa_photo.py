import os
import requests
import datetime
import utils
from dotenv import load_dotenv
from pathlib import Path
import argparse
from datetime import datetime, timedelta

def get_nasa_photo(api_key, start_date, end_date):
        url = "https://api.nasa.gov/planetary/apod"
        params = {"start_date": start_date, "end_date": end_date, "api_key": api_key}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()


def save_nasa_photos(nasa_photo, path):
    for photo_number, photo in enumerate(nasa_photo):
        if photo["media_type"] == "image":
            url = photo["url"]
            filename = os.path.join(path, f"nasa{photo_number}.jpg")
            utils.save_photo(filename, url)


def main():
    load_dotenv()
    api_key = os.environ['NASA_API_KEY']
    path = os.path.join(os.getcwd(), "images")
    os.makedirs(path, exist_ok=True)
    parser = argparse.ArgumentParser()
    parser.add_argument("-end_date", default=datetime.now())
    parser.add_argument("-start_date", default=datetime.now()-timedelta(days=30))
    args = parser.parse_args()
    start_date = args.start_date.strftime("%Y-%m-%d")
    end_date = args.end_date.strftime("%Y-%m-%d")
    nasa_photo = get_nasa_photo(api_key,start_date, end_date)
    save_nasa_photos(nasa_photo, path)

if __name__ == "__main__":
    main()
