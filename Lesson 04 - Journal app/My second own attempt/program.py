import journal


def main():
    print_header()
    run_journal()


def print_header():
    print("-------------------------------")
    print("        Journal App")
    print("-------------------------------")


def run_journal():
    print("Welcome to your journal. What would you like to do today?")
    cmd = "empty"
    journal_name = "My_Journal"
    journal_data = journal.load(journal_name)


    while cmd != "x" and cmd:
        cmd = input("[A]dd entry, [S]how entries, [D]elete entry, E[x]it: ")
        cmd = cmd.lower().strip()

        if cmd == "a":
            add_entry(journal_data)
        elif cmd == "s":
            show_entry(journal_data)
        elif cmd== "d":
            delete_entry(journal_data)
        elif cmd != "x" and cmd:
            print("Sorry, I don't understand what '{}' means.".format(cmd))

    print("Thank you. Saving your journal to '{}'.".format(journal_name))
    journal.save(journal_name, journal_data)


def add_entry(data):
    text = input("What would you like to write? ")

    data.append(text)


def show_entry(data):
    data = reversed(data)
    for ind, items in enumerate(data):
        print("[{}] {}".format(ind + 1, items))


# Added this function in order to delete entries from the list.
def delete_entry(data):
    # Before asking which entry should be deleted, the list of entries is shown to the user.
    show_entry(data)
    # The user is asked which entry they would like to delete.
    print("Which entry would you like to delete?")

    # The user enters their choice as a string (to avoid ValueErrors if the user just hits enter).
    # The user is asked to enter a value between 1 and the total length of the list.
    user_choice = input("Please enter a value between 1 and {}, or 0 to abort: ".format(len(data)))

    # This I only learned during this attempt. Because the user input is a string, and it needs to be an
    # integer to use it further down, this checks if the user input can be turned into an integer,
    # but if it can't be turned into an integer, the exception is handled in a way controlled by the code
    # rather than the program just throwing out an error code and ending the program.
    try:
        user_choice_int = 0
        user_choice_int = int(user_choice)
    except ValueError:
        print("Please enter either a value between 1 and {} or 0.".format(len(data)))

    # Once the user input is turned into an integer, the user input is subtracted from the length of the list.
    # This is done because we are showing the list in reversed form, which means that in the list shown to the user
    # Item 1 is actually the LAST item in the list, so in a list with len = 4, item 1 in the list shown to the user
    # would actually be item 3 (remember that lists start at 0) in the list journal_data. Confusing, right?
    user_choice_int = len(data) - user_choice_int

    # Conditionals for deciding what to do with the user's input.
    if user_choice_int >= 0 and user_choice_int <= len(data):
        for ind, items in enumerate(data):
            if ind == user_choice_int:
                data.pop(ind)
                print("Deleting '{}'.".format(items))
                break
    else:
        pass

    return data


main()
