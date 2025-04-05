import requests
import os
from datetime import datetime
from dotenv import load_dotenv
from utils_functions import download_image


def fetch_nasa_epic_links(nasa_epic_api_url, token):
    epic_payload = {"api_key": token}
    response = requests.get(nasa_epic_api_url, params=epic_payload)
    response.raise_for_status()
    photo_links = []

    for photo_elements in response.json():
        image_id = photo_elements["image"]
        date = datetime.strptime(photo_elements["date"], "%Y-%m-%d %H:%M:%S")
        base_url = "https://api.nasa.gov/EPIC/archive/natural"
        photo_links.append(f"{base_url}/{date.strftime('%Y/%m/%d')}/png/{image_id}.png?api_key={token}")

    for index, url in enumerate(photo_links, start=1):
        filename = f"nasa_epic_{index}.png"
        file_path = os.path.join("images", filename)
        download_image(url, file_path)


def main():
    load_dotenv()
    token = os.environ["NASA_API_KEY"]

    nasa_epic_api_url = "https://api.nasa.gov/EPIC/api/natural"

    os.makedirs("images", exist_ok=True)
    
    fetch_nasa_epic_links(nasa_epic_api_url, token)
    

if __name__ == '__main__':
    main()