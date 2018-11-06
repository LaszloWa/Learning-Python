# This imports the os module, with which we can find and specify file paths. It is used here to specify where we
# want to save the list that stores the user input, and also where the app can find our previously stored list when
# loading it again
import os


# This function saves the list. It specifies the filename using the imported os module.
def save(name, data):
    filename = os.path.abspath(os.path.join(".", name + ".jrl"))

    # Here we create a variable called 'fin' (can be named whatever) and set it to open(filename) with write access.
    # It's the same as writing fin = open(filename, "w"). It is important to open with "w" access so that we can
    # write the list to the file. If we just say open(filename) it will open the file as read only, which is the default.
    with open(filename, "w") as fin:

        # And here we cycle through all the entries (items) contained in the list 'data' and write it to the variable
        # 'fin', which is essentially the opened file. "\n" adds a line break after every item, as it would otherwise
        # be displayed in one line with one entry following the other.
        for items in data:
            fin.write(items + "\n")


# This function does two things. It creates a list called 'data', and if no saved file exists, it will simply provide
# the empty list. If, however, the file name specified in the other .py file exists in the specified location,
# it will open the file (this tie in read only though, as we don't need to write to the file) and for all entries
# (items) found in fout (which is, essentially, the opened file) it will append (add) them to the list
# .rstrip cleans up any whitespace (in this case the '\n' linebreak (which is also saved in the file) to avoid
# a double spaced output. The list containing all the items is then returned to the function and provided to the
# variable in the other .py file that called upon the function
def load(name):
    data = []
    filename = os.path.abspath(os.path.join(".", name + ".jrl"))

    if os.path.exists(filename):
        with open(filename) as fout:
            for items in fout.readlines():
                data.append(items.rstrip())

    return data


# Outsourced bit of code from the 'add_entry' function from the other .py file. Not sure why the author of the course
# decided to outsource the append part of the function to another file, but will research this.
def add_entry(text, data):
    data.append(text)