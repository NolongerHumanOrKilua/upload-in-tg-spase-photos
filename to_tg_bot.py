import os
from xml.dom.minidom import Document
import telegram
import time
from dotenv import load_dotenv
import random

load_dotenv()
chat = os.environ["TG_CHAT_ID"]
tg_token = os.environ['TG_TOKEN']
delay = 1
path = "images"
files = os.listdir(path=path)

while True:
    try:
            bot = telegram.Bot(token=tg_token)
            for root, dir_names, files in os.walk(path):
                random.shuffle(files)
                for file in files:
                    with open(os.path.join(root, file), "rb") as file:
                        bot.send_document(chat_id=chat, document=file)
                    time.sleep(delay)
    except telegram.error.NetworkError:
            time.sleep(10)


        
