from importlib.resources import path
import os
import telegram
import time
from dotenv import load_dotenv

load_dotenv()
chat = os.environ["TG_CHAT_ID"]
tg_token = os.environ['TG_TOKEN']
delay = 14400
path = "images"
try:
    bot = telegram.Bot(token=tg_token)
    for root, dir_names, files in os.walk(path):
        for file in files:
            with open(os.path.join(root, file), "rb") as file:
                bot.send_document(
                    chat_id=chat,
                    document=file
                )
            time.sleep(delay)
except telegram.error.NetworkError:
    print("network error")             
