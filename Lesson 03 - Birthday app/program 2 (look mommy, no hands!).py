# After making this app with the help of the tutorial, this is my attempt to make it without 'looking'

import datetime


def print_title():
    print("-----------------------------")
    print("       BIRTHDAY APP")
    print("-----------------------------")


def get_user_birthday():
    print("Hello. Please enter your birthday.")
    year = int(input("Enter year [YYYY]: "))
    month = int(input("Enter month [MM]: "))
    day = int(input("Enter day [DD]: "))

    birthday = datetime.date(year, month, day)

    return birthday


def compute_days_from_birthday(date1, date2):
    present_year = datetime.date(date2.year, date1.month, date1.day)

    delta = present_year - date2

    days = delta.days

    return days


def print_birthday_message(days):
    if days < 0:
        print("Your birthday was {} days ago.".format(-days))
    elif days >0:
        print("Only {} more days until your birthday!".format(-days))
    else:
        print("Your birthday is today. Happy birthday!")


def main():
    print_title()
    bday = get_user_birthday()
    today = datetime.date.today()
    days_difference = compute_days_from_birthday(bday, today)
    print_birthday_message(days_difference)

main()

# I actually managed it! For some reason the code wouldn't work at the end, so I looked at the first attempt
# but I didn't actually need to change anything, I got it to work in the end without any input from before :)