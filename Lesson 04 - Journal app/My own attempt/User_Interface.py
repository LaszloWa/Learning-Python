# This is my attempt to replicate the exercise on my own as much as possible, only looking for guidance when
# I'm stuck. I had to look a few times, but most of the code, especially in the beginning, I was able to write myself
# I started off by writing everything in one file to see if I could make it work, and for my own comprehension.
# Once everything worked, I then outsourced certain functions into a second file ("User_operation") and imported the
# functions. This was to see if I could then also make it work when splitting it in two, another comprehension exercise


# Importing the functions that I outsourced
import User_operations

# main function with which I run the app. I call the function at the very bottom, it is listed here to give a
# high level overview of what is going on.
def main():
    print_header()
    input_loop()


# Just the header, nice and simple
def print_header():
    print("--------------------------------------")
    print("          JOURNAL APP")
    print("--------------------------------------")


# All other functions are basically being called upon in this function. It cycles through the while-loop until
# the user enters 'x' or provides no input and hits enter
def input_loop():
    print("Welcome to you journal. What would you like to do?")

    # The name of the journal, the file to which the entries are being saved
    journal_name = "My_Journal"

    # The list. It called upon the function 'load' in the other .py file. The load function contains the list
    # and also loads the existing list (if it is named "My_Journal" if it exists in the specified path.
    journal_data = User_operations.load(journal_name)

    # The cmd variable, which is the user input, has to be defined before it can be called upon in the loop.
    # It is just set to the string "empty" as a non-empty, non-'y' placeholder
    cmd = "empty"

    # The while loop cycles through asking the user for input until the loop is exited. The loop continues until
    # the user enters 'x' or provides no input when pressing enter
    while cmd != "x" and cmd:

        # The user is asked to input either A, L, or x to execute commands.
        cmd = input("[A]dd entry, [L]ist entries, E[x]it: ")

        # To make the accepted input more robust, we turn the input into lower-case letters and strip whitespace
        # away. This way we don't have to specify l and L seperately, or '   l'.
        cmd = cmd.lower().strip()

        # The next parts are just the conditionals for accepting user input, and the respective functions that are
        # called upon when a specific input is given
        if cmd == "a":
            add_entry(journal_data)
        elif cmd == "l":
            list_entry(journal_data)
        elif cmd != "x" and cmd:
            print("Sorry, I don't know what '{}' means.".format(cmd))

    # If the loop is broken, the text is printed and the input is saved to the file. The 'save' function is
    # specified in the other .py file.
    print("I will treasure your input, always.")
    User_operations.save(journal_name, journal_data)


# Function to add an entry to the list. Calls upon the 'add_entry' function in the other file. Not sure why
# the author of this course chose to do that in another file, have to research that.
# todo: find out why author of course outsourced 'add_entry' to other file.
def add_entry(data):
    text = input("Please make your entry: ")
    User_operations.add_entry(text, data)


# Function to display the entries already provided by the user, in reversed order so that the last entered items
# will be displayed first.
def list_entry(data):
    entries = reversed(data)

    # This says that for idx (index, can be named whatever, used here to control the formatting of the numbering
    # introduced through 'enumerate()', and items (can also be named at random) in the variable 'entries'
    # print them so that idx is displayed first in brackets, followed by a space and then the entered user
    # input
    for idx, items in enumerate(entries):
        print("[{}] {}".format(idx + 1, items))


# Here the main function from the very top is called upon. It is called upon at the very bottom of the code
# as calling upon it before all code is defined messes with the app.
main()