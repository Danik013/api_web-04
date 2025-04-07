import requests
import os
from urllib.parse import urlparse
from dotenv import load_dotenv
import sys
import argparse
from contextlib import suppress
from utils_functions import get_file_extension, download_image


def fetch_nasa_apod_links(apod_payload):
    nasa_apod_api_url = "https://api.nasa.gov/planetary/apod"
    response = requests.get(nasa_apod_api_url, params=apod_payload)
    response.raise_for_status()

    apod_links = []
    with suppress(KeyError):
        for nasa_apod in response.json():
            apod_links.append(nasa_apod["url"])
    return apod_links
 
     
def download_nasa_apod(apod_links):
    for index, url in enumerate(apod_links, start=1):
        extension = get_file_extension(url)
        filename = f"nasa_apod_{index}{extension}"
        file_path = os.path.join("images", filename)

        download_image(url, file_path)


def main():
    load_dotenv()
    token = os.environ["NASA_API_KEY"]

    parser = argparse.ArgumentParser(description="""
        Получаем фото дня в космической тематике - по умолчанию 10 фото. 
        Можно ввести необходимое количество фото для скачивания.
    """)
    parser.add_argument("count", nargs="?", default="10", help="Можно ввести необходимое количество фото для скачивания.")
    args = parser.parse_args()
    count = args.count

    apod_payload = {"api_key": token, "count": count}
    
    os.makedirs("images", exist_ok=True)
    
    apod_links = fetch_nasa_apod_links(apod_payload)

    download_nasa_apod(apod_links)

    

if __name__ == '__main__':
    main()