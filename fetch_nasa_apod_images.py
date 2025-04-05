import requests
import os
from urllib.parse import urlparse
from dotenv import load_dotenv
import sys
import argparse
from utils_functions import get_file_extension, download_image


def fetch_nasa_apod_links(nasa_apod_api_url, apod_payload):
    response = requests.get(nasa_apod_api_url, params=apod_payload)
    response.raise_for_status()
    photo_link = response.json()["url"]

    extension = get_file_extension(photo_link)
    filename = f"nasa_apod_{extension}"
    file_path = os.path.join("images", filename)
    download_image(photo_link, file_path)


def main():
    load_dotenv()
    token = os.environ["NASA_API_KEY"]

    nasa_apod_api_url = "https://api.nasa.gov/planetary/apod"

    parser = argparse.ArgumentParser()
    parser.add_argument("date", nargs="?")
    urlspace = parser.parse_args()
    date = urlspace.date
    apod_payload = {"api_key": token}
    if date:
        apod_payload["date"] = date

    os.makedirs("images", exist_ok=True)
    
    fetch_nasa_apod_links(nasa_apod_api_url, apod_payload)
    

if __name__ == '__main__':
    main()