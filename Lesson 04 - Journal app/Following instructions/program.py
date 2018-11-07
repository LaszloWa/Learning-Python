import journal


def main():
    print_header()
    event_loop()



def print_header():
    print("-------------------------")
    print("     JOURNAL APP")
    print("-------------------------")


def event_loop():
    print("What do you want to do with your journal?")
    cmd = "empty"
    journal_name = "My_Journal"
    journal_data = journal.load(journal_name)

    while cmd != "x" and cmd:
        cmd = input("[L]ist entries, [A]dd entries, E[x]it. ")
        cmd = cmd.lower().strip()

        if cmd == "l":
            list_entry(journal_data)
        elif cmd == "a":
            add_entry(journal_data)
        elif cmd != "x" and cmd:
            print("Sorry, I don't know what '{}' means.".format(cmd))

    print("And we're all done.")
    journal.save(journal_name, journal_data)


def list_entry(data):
    print("Your previous entries:")
    entries = reversed(data)

    for idx, entry in enumerate(entries):
        print("* [{}] {}".format(idx + 1, entry))


def add_entry(data):
    text = input("Type your entry, <enter> to exit: ")
    journal.add_entry(text, data)


main()