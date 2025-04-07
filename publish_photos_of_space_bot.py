import telegram
import os
import random
import time
from dotenv import load_dotenv
import sys
import argparse
from utils_functions import get_file_paths


def publishes_content(chat_id, publication_timing, bot, file_paths):
    while True:
        for file_path in file_paths:
            with open(file_path, "rb") as file:
                bot.send_document(chat_id=chat_id, document=file)
            time.sleep(publication_timing)
        random.shuffle(file_paths)
        

def main():
    load_dotenv()
    token = os.environ["TELEGRAM_TOKEN"]
    chat_id = os.environ["TG_CHAT_ID"]

    parser = argparse.ArgumentParser("""
        Бот отправляет все фото из папки по порядку в бесконечном цикле по таймингу. 
        По умолчанию 4 часа. Либо введите количество часов.
    """)
    parser.add_argument("hours", nargs="?", default=4, help="Можно указать интервал в часах.")
    args = parser.parse_args()
    hours = args.hours
    
    publication_timing = hours * 3600

    file_paths = get_file_paths()

    bot = telegram.Bot(token=token)

    publishes_content(chat_id, publication_timing, bot, file_paths)


if __name__ == '__main__':
    main()