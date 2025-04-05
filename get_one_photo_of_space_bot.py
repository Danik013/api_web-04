import telegram
import os
import random
import time
from dotenv import load_dotenv
import sys
import argparse
from utils_functions import getting_file_path


def publishing_image(chat_id, image_name, bot):
    file_paths = getting_file_path()
    matched_files = [file_path for file_path in file_paths if image_name in os.path.basename(file_path)]
    if matched_files:
        with open(matched_files[0], "rb") as file:
            bot.send_document(chat_id=chat_id, document=file)
    else:
        with open(random.choice(file_paths), "rb") as file:
            bot.send_document(chat_id=chat_id, document=file)


def main():
    load_dotenv()
    token = os.environ["TELEGRAM_TOKEN"]
    chat_id = os.environ["TG_CHAT_ID"]

    parser = argparse.ArgumentParser()
    parser.add_argument("image_name", nargs="?")
    urlspace = parser.parse_args()
    image_name = urlspace.image_name
    if image_name is None:
        image_name = ""
        
    bot = telegram.Bot(token=token)

    publishing_image(chat_id, image_name, bot)


if __name__ == '__main__':
    main()