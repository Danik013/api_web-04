import requests
import os
from urllib.parse import urlparse
import sys
import argparse
from utils_functions import get_file_extension, download_image


def fetch_spasex_images_links(spasex_api_url, launch_id):
    response = requests.get(spasex_api_url)
    response.raise_for_status()
    launches = response.json()
    if launch_id:
        for launch_elements in launches:
            if launch_elements["id"] == launch_id:
                images_links = launch_elements["links"]["flickr"]["original"]
                break
            else:
                images_links = []
    else:
        images_links = launches[0]["links"]["flickr"]["original"]
        return images_links

    for index, url in enumerate(images_links, start=1):
        extension = get_file_extension(url)
        filename = f"spasex_{index}{extension}"
        file_path = os.path.join("images", filename)
        download_image(url, file_path)


def main():
    spasex_api_url = "https://api.spacexdata.com/v5/launches"

    parser = argparse.ArgumentParser()
    parser.add_argument ('id', nargs='?')
    urlspace = parser.parse_args()
    launch_id = urlspace.id

    os.makedirs("images", exist_ok=True)
    
    fetch_spasex_images_links(spasex_api_url, launch_id)
        

if __name__ == '__main__':
    main()
