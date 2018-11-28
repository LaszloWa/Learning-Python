import os
import shutil

import requests


def get_cats(folder, name):
    data = download_cats_from_web()
    save_image(folder, name, data)


def download_cats_from_web():
    url = "http://consuming-python-services-api.azurewebsites.net/cats/random"
    response = requests.get(url, stream=True)

    return response.raw


def save_image(folder, name, data):
    filename = os.path.join(folder, name + ".jpg")

    with open(filename, "wb") as fout:
        shutil.copyfileobj(data, fout)