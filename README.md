# upload-in-tg-spase-photos# Загрузка фотографий в Telegram

Программа для публикации космических фото в Telegram.

## Как установить

### Окружение
Python должен быть установлен.

### Зависимости
Используйте pip для установки зависимостей :
```bash
pip install -r requirements.txt
```

### epic_photo.py
Загружает с сайта [NASA](https://api.nasa.gov/EPIC) информацию о фотографиях земли. Фотографии сохраняет в директорию `images\`. Запуск:
```bash 
$ python epic_photo.py
```

### fetch_spacex_last_launch.py
Загружает с сайта [SpaceX](https://api.spacexdata.com/v5/launches/) информацию о запусках. Фотографии запуска сохраняет в директорию `images\`. Запуск:
```bash 
$ python fetch_spacex_last_launch.py
```

### photo_nasa.py
Загружает с сайта [NASA](https://api.nasa.gov/planetary/apod) фотографии в директорию `images\n`. Для доступа к фотографиям необходимо сгенерировать API Key [NASA](https://api.nasa.gov/#signUp). Запуск:
```bash 
$ python photo_nasa.py
```

### to_tg_bot.py
Публикует загруженные фотографии в Telegram канал. Запуск:
```bash 
$ python to_tg_bot.py
```


