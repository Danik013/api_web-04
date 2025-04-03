import requests
import os
from urllib.parse import urlparse
from dotenv import load_dotenv
import sys
import argparse
from API_04_common_functions import get_file_extension, get_image


def get_nasa_apod(api_nasa_apods, token, user_input):
    if not user_input:
        apod_payload = {"api_key": token}
    else:
        apod_payload = {"api_key": token, "date": user_input}
    response = requests.get(api_nasa_apods, params=apod_payload)
    response.raise_for_status()
    photo_link = response.json()["url"]

    extension = get_file_extension(photo_link)
    filename = f"nasa_apod_{extension}"
    file_path = os.path.join("imajes", filename)
    get_image(photo_link, file_path)


def main():
    load_dotenv()
    token = os.environ["NASA_API_KEY"]
    api_nasa_apods = "https://api.nasa.gov/planetary/apod"
    parser = argparse.ArgumentParser()
    parser.add_argument ('id', nargs='?')
    urlspace = parser.parse_args()
    user_input = urlspace.id
    os.makedirs("imajes", exist_ok=True)
    get_nasa_apod(api_nasa_apods, token, user_input)
    

if __name__ == '__main__':
    main()
