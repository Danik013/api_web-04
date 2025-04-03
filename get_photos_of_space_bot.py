import telegram
import os
import random
import time
from dotenv import load_dotenv
import sys
import argparse


def take_files():
    files_path = []
    directory = "imajes"
    files_in_dir = os.listdir(directory)
    for files_in_dirs in files_in_dir:
        file = os.path.join(directory, files_in_dirs)
        files_path.append(file)
    return files_path


def sending_photos(chat_id, publication_timing, bot):
    files_path = take_files()
    while True:
        for file_path in files_path:
            bot.send_document(chat_id=chat_id, document=open(file_path, "rb"))
            time.sleep(publication_timing)
        random.shuffle(files_path)
        for file_path in files_path:
            bot.send_document(chat_id=chat_id, document=open(file_path, "rb"))
            time.sleep(publication_timing)


def main():
    load_dotenv()
    token = os.environ["TELEGRAM_TOKEN"]
    chat_id = os.environ["TG_CHAT_ID"]

    parser = argparse.ArgumentParser()
    parser.add_argument ('hours', nargs='?')
    urlspace = parser.parse_args()
    user_input = urlspace.hours

    if user_input is None:
        publication_timing = 4*3600
    else:
        publication_timing = user_input*3600

    bot = telegram.Bot(token=token)

    sending_photos(chat_id, publication_timing, bot)


if __name__ == '__main__':
    main()