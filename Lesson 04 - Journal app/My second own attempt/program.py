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
        cmd = input("[A]dd entry, [S]how entries, E[x]it: ")
        cmd = cmd.lower().strip()

        if cmd == "a":
            add_entry(journal_data)
        elif cmd == "s":
            show_entry(journal_data)
        elif cmd != "x" and cmd:
            print("Sorry, I don't understand what '{}' means.".format(cmd))

    print("Thank you. Saving your journal to '{}'.".format(journal_name))
    journal.save(journal_name, journal_data)


def add_entry(data):
    text = input("What would you like to write? ")

    data.append(text)


def show_entry(data):
    for ind, items in enumerate(data):
        print("[{}] {}".format(ind + 1, items))


main()
