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


def sending_photos(chat_id, user_input, bot):
    files_path = take_files()
    matched_files = [file_path for file_path in files_path if user_input in os.path.basename(file_path)]
    if matched_files:
        bot.send_document(chat_id=chat_id, document=open(matched_files[0], "rb"))
    else:
        bot.send_document(chat_id=chat_id, document=open(random.choice(files_path), "rb"))


def main():
    load_dotenv()
    token = os.environ["TELEGRAM_TOKEN"]
    chat_id = os.environ["TG_CHAT_ID"]

    parser = argparse.ArgumentParser()
    parser.add_argument ('name_photo', nargs='?')
    urlspace = parser.parse_args()
    user_input = urlspace.name_photo
    if user_input is None:
        user_input = ""
        
    bot = telegram.Bot(token=token)

    sending_photos(chat_id, user_input, bot)


if __name__ == '__main__':
    main()