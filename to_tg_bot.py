import os
from turtle import delay
import telegram
import os   
import time

chat = input()
tg_token = os.environ['TG_TOKEN']
bot = telegram.Bot(token=tg_token)
delay = 14400
while True:
    for dir_names, files in os.walk('images/'):
        for file in files:
            with open(os.path.join(file), "rb") as file:
                bot.send_document(
                        chat_id=chat,
                        document=file
                        )
            time.sleep(delay)
      