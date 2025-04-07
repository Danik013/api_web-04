import requests
import os
from urllib.parse import urlparse


def download_image(url, file_path):
    response = requests.get(url)
    response.raise_for_status()
    with open(file_path, "wb") as file:
        file.write(response.content)
    return


def get_file_extension(url):
    url_elements = urlparse(url)
    path_url = os.path.splitext(url_elements.path)
    _, file_extension = path_url
    return file_extension


def get_file_paths():
    file_paths = []
    directory = "images"
    files_in_dir = os.listdir(directory)
    for files_in_dirs in files_in_dir:
        file = os.path.join(directory, files_in_dirs)
        file_paths.append(file)
    return file_paths
