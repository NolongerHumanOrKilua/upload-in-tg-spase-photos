from random import random
from turtle import delay
import telegram
import os   
import random
import time

bot = telegram.Bot(token='5333820970:AAFur-aO1wotqdFxDupuXZGBBZ3dLZhjQcE')


delay = 14400
while True:
    for dir_path, dir_names, files in os.walk('images/'):
        for file in files:
            with open(os.path.join(dir_path, file), "rb") as file:
                bot.send_document(
                        chat_id="@spase_photo",
                        document=file
                        )
            time.sleep(delay)
      