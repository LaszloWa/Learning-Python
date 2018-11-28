import os
import platform
import subprocess

import cat_service


def main():
    print_header()
    folder = get_or_create_folder()
    download_cats(folder)
    display_cats_to_user(folder)


def print_header():
    print("---------------------------------------")
    print("          LOLcat Factory")
    print("---------------------------------------")
    print()


def get_or_create_folder():
    base_path = os.path.dirname(__file__)
    folder = "Cat_pictures"
    full_path = os.path.join(base_path, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print("Creating new directory {}.".format(full_path))
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = "lolcat {}".format(i)
        print("Downloading {}.".format(name))
        cat_service.get_cats(folder, name)


def display_cats_to_user(folder):
    if platform.system() == "Darwin":
        subprocess.call(["open", folder])
    elif platform.system() == "Windows":
        subprocess.call(["explorer", folder])
    elif platform.system() == "Linux":
        subprocess.call(["xdg-open", folder])
    else:
        print("Sorry, but the OS {} is not supported.".format(platform.system()))


if __name__ == "__main__":
    main()
