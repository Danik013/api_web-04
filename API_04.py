import requests
import os
from urllib.parse import urlparse
from datetime import datetime
from dotenv import load_dotenv
import sys
import argparse


def get_photo_spasex(api_spacex):
    response = requests.get(api_spacex)
    response.raise_for_status()
    photo_links = response.json()[13]["links"]["flickr"]["original"]
    for index, url in enumerate(photo_links, start=1):
        extension = get_file_extension(url)
        filename = f"spasex_{index}{extension}"
        file_path = os.path.join("imajes", filename)
        get_image(url, file_path)
    return
 

def get_nasa_apod(api_nasa_apods, token):
    apod_payload = {"api_key": token, "start_date": "2025-02-25", "end_date": "2025-03-25"}
    response = requests.get(api_nasa_apods, params=apod_payload)
    response.raise_for_status()
    photo_links = []
    try:
        for nasa_apod in response.json():
            photo_links.append(nasa_apod["url"])
    except KeyError:
        pass

    for index, url in enumerate(photo_links, start=1):
        extension = get_file_extension(url)
        filename = f"nasa_apod_{index}{extension}"
        file_path = os.path.join("imajes", filename)
        get_image(url, file_path)


def get_nasa_epic(api_nasa_epic, token):
    epic_payload = {"api_key": token}
    response = requests.get(api_nasa_epic, params=epic_payload)
    response.raise_for_status()
    photo_links = []

    for photo_elements in response.json():
        image_id = photo_elements["image"]
        date = datetime.strptime(photo_elements["date"], "%Y-%m-%d %H:%M:%S")
        extension = "png" 
        base_url = "https://api.nasa.gov/EPIC/archive/natural"
        photo_links.append(f"{base_url}/{date.strftime("%Y/%m/%d")}/{extension}/{image_id}.{extension}?api_key={token}")

    for index, url in enumerate(photo_links, start=1):
        filename = f"nasa_epic_{index}.png"
        file_path = os.path.join("imajes", filename)
        get_image(url, file_path)


def get_image(url, file_path):
    response = requests.get(url)
    response.raise_for_status()
    with open(file_path, "wb") as file:
        file.write(response.content)
    return


def get_file_extension(url):
    url_elements = urlparse(url)
    path_url = os.path.splitext(url_elements.path)
    file_extension = path_url[1]
    return file_extension


def main():
    load_dotenv()
    token = os.environ["NASA_API_KEY"]
    api_nasa_epic = f"https://api.nasa.gov/EPIC/api/natural/date/2025-03-30"
    api_nasa_apods = "https://api.nasa.gov/planetary/apod"
    api_spacex = "https://api.spacexdata.com/v5/launches"
    os.makedirs("imajes", exist_ok=True)
    get_photo_spasex(api_spacex)
    get_nasa_apod(api_nasa_apods, token)
    get_nasa_epic(api_nasa_epic, token)
    

if __name__ == '__main__':
    main()
