import requests
import os
from datetime import datetime
from dotenv import load_dotenv
import sys
import argparse
from API_04_common_functions import get_image


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


def main():
    load_dotenv()
    token = os.environ["NASA_API_KEY"]
    parser = argparse.ArgumentParser()
    parser.add_argument ('id', nargs='?')
    urlspace = parser.parse_args()
    user_input = urlspace.id
    if not user_input:
        api_nasa_epic = f"https://api.nasa.gov/EPIC/api/natural"
    else:
        api_nasa_epic = f"https://api.nasa.gov/EPIC/api/natural/date/{user_input}"
    os.makedirs("imajes", exist_ok=True)
    get_nasa_epic(api_nasa_epic, token)
    

if __name__ == '__main__':
    main()
