import os


def load(name):
    data = []
    filename = os.path.abspath(os.path.join(".", "journals", name + ".jrl"))

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, data):
    filename = os.path.abspath(os.path.join(".", "journals", name + ".jrl"))
    print("...saving input to {}".format(filename))

    # with open(filename, "w") as fout is the same as declaring fout as the variable as below, but closes the file
    # again after it's done writing the items in it.
    # fout = open(filename, "w")
    with open(filename, "w") as fout:
        for item in data:
            fout.write(item + "\n")


def add_entry(text, data):
    data.append(text)
