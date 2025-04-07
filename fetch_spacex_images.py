import requests
import os
from urllib.parse import urlparse
import sys
import argparse
from utils_functions import get_file_extension, download_image


def fetch_spasex_images_links(spasex_api_url):
    response = requests.get(spasex_api_url)
    response.raise_for_status()
    launch = response.json()
    images_links = launch["links"]["flickr"]["original"]
    
    for index, url in enumerate(images_links, start=1):
        extension = get_file_extension(url)
        filename = f"spasex_{index}{extension}"
        file_path = os.path.join("images", filename)
        download_image(url, file_path)


def main():
    parser = argparse.ArgumentParser(description="""
        Загружаем фотографии запуска SpaseX. 
        По умолчанию - последний запуск.
    """)
    parser.add_argument ('id', nargs='?', default="latest", help="Можно ввести id запуска.")
    args = parser.parse_args()
    launch_id = args.id
    spasex_api_url = f"https://api.spacexdata.com/v5/launches/{launch_id}"

    os.makedirs("images", exist_ok=True)
    
    fetch_spasex_images_links(spasex_api_url)
        

if __name__ == '__main__':
    main()
