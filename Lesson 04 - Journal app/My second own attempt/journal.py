import os


def save(name, data):
    filename = os.path.abspath(os.path.join(".", "Journals", name + ".jrl"))

    with open(filename, "w") as saving:
        for items in data:
            saving.write(items + "\n")


def load(name):
    data = []
    filename = os.path.abspath(os.path.join(".", "Journals", name + ".jrl"))

    if os.path.exists(filename):
        with open(filename) as loading:
            for entries in loading.readlines():
                data.append(entries.strip())

    return data
