import requests
import os
from urllib.parse import urlparse


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