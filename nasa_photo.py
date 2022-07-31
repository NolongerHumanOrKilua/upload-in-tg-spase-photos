import os
import requests
import datetime

api_key = os.environ['NASA_API_KEY']


def nasa_photo(api_key):
  start_date = datetime.date.fromisoformat('2022-06-29')
  end_date = datetime.date.fromisoformat('2022-07-29')
  api_key=f"{api_key}"
  url = "https://api.nasa.gov/planetary/apod"
  parameters = { "start_date": f"{start_date}",
        "end_date": f"{end_date}", "api_key": f"{api_key}"}
  response = requests.get(url, params=parameters)
  response.raise_for_status()  
  return response.json()
  
def save_nasa_ph(nasa_photo):
  i = 0
  for photo in nasa_photo:
    url = photo["url"]
    filename = f'images_nasa/nasa{i}.jpg'
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as f:
      f.write(response.content)
    i +=1  

nasa_photo = nasa_photo(api_key)
save_nasa_ph(nasa_photo)