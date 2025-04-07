import telegram
import os
import random
import time
from dotenv import load_dotenv
import sys
import argparse
from utils_functions import get_file_paths


def publishes_image(chat_id, image_name, bot, file_paths):
    matched_files = [file_path for file_path in file_paths if image_name in os.path.basename(file_path)]
    file_to_send = matched_files[0] if matched_files else random.choice(file_paths)
    with open(file_to_send, "rb") as file:
        bot.send_document(chat_id=chat_id, document=file)
    

def main():
    load_dotenv()
    token = os.environ["TELEGRAM_TOKEN"]
    chat_id = os.environ["TG_CHAT_ID"]

    parser = argparse.ArgumentParser(description="""
        Бот отправляет фото выбранное по названию. 
        Если не нашел, отправляет случайное фото из папки.
    """)
    parser.add_argument("image_name", nargs="?", default="no_name", help="Можно указать название файла.")
    args = parser.parse_args()
    image_name = args.image_name

    file_paths = get_file_paths()
            
    bot = telegram.Bot(token=token)

    publishes_image(chat_id, image_name, bot, file_paths)


if __name__ == '__main__':
    main()