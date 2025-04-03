import requests
import os
from urllib.parse import urlparse
import sys
import argparse
from API_04_common_functions import get_file_extension, get_image


def get_photo_spasex(api_spacex, user_input):
    response = requests.get(api_spacex)
    response.raise_for_status()
    launches = response.json()
    if user_input:
        for launch_elements in launches:
            if launch_elements["id"] == user_input:
                photo_links = launch_elements["links"]["flickr"]["original"]
                break
            else:
                photo_links = []
    else:
        photo_links = launches[0]["links"]["flickr"]["original"]
    if not photo_links:
        print("Нет фотографий последнего запуска")
        return

    for index, url in enumerate(photo_links, start=1):
        extension = get_file_extension(url)
        filename = f"spasex_{index}{extension}"
        file_path = os.path.join("imajes", filename)
        get_image(url, file_path)


def main():
    api_spacex = "https://api.spacexdata.com/v5/launches"
    parser = argparse.ArgumentParser()
    parser.add_argument ('id', nargs='?')
    urlspace = parser.parse_args()
    user_input = urlspace.id
    os.makedirs("imajes", exist_ok=True)
    get_photo_spasex(api_spacex, user_input)
    

if __name__ == '__main__':
    main()
