import os
import requests
import datetime
import utils
from dotenv import load_dotenv

def nasa_photo(api_key):
  start_date = datetime.date.fromisoformat('2022-06-29')
  end_date = datetime.date.fromisoformat('2022-07-29')
  api_key=api_key
  url = "https://api.nasa.gov/planetary/apod"
  parameters = { "start_date": f"{start_date}",
        "end_date": f"{end_date}", "api_key": f"{api_key}"}
  response = requests.get(url, params=parameters)
  response.raise_for_status()  
  return response.json()
  
def save_nasa_ph(nasa_photo):
  for photo_number, photo in enumerate(nasa_photo):
    url = photo["url"]
    filename = f'images/nasa{photo_number}.jpg'
    utils.save_photo(filename, url)



def main():
    load_dotenv()
    api_key = os.environ['NASA_API_KEY']
    try:
        nasa_photo = nasa_photo(api_key)
        save_nasa_ph(nasa_photo)  
    except:
        return print("error")


if __name__ == "__main__":
    main()