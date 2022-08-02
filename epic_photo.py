import os
import requests
import datetime
api_key_nasa = os.environ['API_KEY']

def epic_photo(epic_image):
    i = 0
    for photo in epic_image:
      date = photo["date"]
      date = date.split(maxsplit=1)
      date = date[0]
      image = photo["image"]
      photo_date = datetime.date.fromisoformat(f'{date}')
      photo_date = photo_date.strftime("%Y/%m/%d")
      api_key="xrORzILSdTVL4akZk0CUjPvzVNQq7mhyaTW4eyBS"
      url = f"https://api.nasa.gov/EPIC/archive/natural/{photo_date}/png/{image}.png?api_key={api_key}"
      filename = f'images/epic{i}.jpg'
      response = requests.get(url)
      response.raise_for_status()
      with open(filename, 'wb') as f:
        f.write(response.content)
      i +=1  


def epic_image():
    api_key = api_key_nasa
    url = f"https://api.nasa.gov/EPIC/api/natural/images?api_key={api_key}"
    response = requests.get(url)
    response.raise_for_status()    
    return response.json()

epic_image = epic_image()
epic_photo(epic_image)    