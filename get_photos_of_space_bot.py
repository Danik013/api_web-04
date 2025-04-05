import telegram
import os
import random
import time
from dotenv import load_dotenv
import sys
import argparse
from utils_functions import getting_file_path


DEFAULT_TIMING = 4


def publishing_content(chat_id, publication_timing, bot):
    file_paths = getting_file_path()
    while True:
        for file_path in file_paths:
            with open(file_path, "rb") as file:
                bot.send_document(chat_id=chat_id, document=file)
            time.sleep(publication_timing)
        random.shuffle(file_paths)
        for file_path in file_paths:
            with open(file_path, "rb") as file:
                bot.send_document(chat_id=chat_id, document=file)
            time.sleep(publication_timing)


def main():
    load_dotenv()
    token = os.environ["TELEGRAM_TOKEN"]
    chat_id = os.environ["TG_CHAT_ID"]

    parser = argparse.ArgumentParser()
    parser.add_argument("hours", nargs="?")
    urlspace = parser.parse_args()
    hours = urlspace.hours or DEFAULT_TIMING
    publication_timing = hours*3600

    bot = telegram.Bot(token=token)

    publishing_content(chat_id, publication_timing, bot)


if __name__ == '__main__':
    main()