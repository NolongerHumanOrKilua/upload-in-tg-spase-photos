import requests
import datetime

def images():
  id = input("Введите id запуска или  введите 6243aec2af52800c6e91925d: ")
  url = f"https://api.spacexdata.com/v5/launches/{id}"
  response = requests.get(url) 
  response.raise_for_status()
  return response.json()["links"]['flickr']['original']

def fetch_spacex_last_launch(images):
  i = 0
  for image in images:
    filename = f'images/hubble{i}.jpeg'
    response = requests.get(image)
    response.raise_for_status()
    with open(filename, 'wb') as f:
      f.write(response.content)
    i +=1  

images =  images() 
fetch_spacex_last_launch(images)