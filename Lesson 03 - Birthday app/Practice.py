import datetime


def main():
    print_header()
    bday = get_bday()
    today = datetime.date.today()
    this_year = current_year_bday(bday, today)
    days = calc_diff(this_year, today)
    print_message(days)


def print_header():
    print("--------------------------------")
    print("        Birthday app")
    print("--------------------------------")


def get_bday():
    print("When is your birthday?")
    year = int(input("Year [YYYY]: "))
    month = int(input("Month [MM]: "))
    day = int(input("Day[DD]: "))

    bdate = datetime.date(year, month, day)

    return bdate


def current_year_bday(date1, date2):
    this_year_bday = datetime.date(date2.year, date1.month, date1.day)

    return this_year_bday


def calc_diff(date1, today):
    delta = date1 - today

    return delta.days


def print_message(data):
    if data < 0:
        print("Your birthday was {} days ago.".format(-data))
    elif data > 0:
        print("Your birthday is in {} days!".format(data))
    else:
        print("Happy birthday! It's your birthday today!")


main()