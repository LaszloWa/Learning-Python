# Import datetime library to use later for working with dates
import datetime


# The header
def print_header():
    print("------------------------------")
    print("        BIRTHDAY APP")
    print("------------------------------")


# This function gets the birthday from the user
def get_birthday_from_user():
    # First the user is asked to enter his birthday
    print("Please enter your birthday.")

    # The input is wrapped in int() to turn the string into an integer. We need this in order to work with the dates.
    year = int(input("Enter year [YYYY]: "))
    month = int(input("Enter month [MM]: "))
    day = int(input("Enter day[DD]: "))

    # Now putting the user's birthday into one variable
    birthday = datetime.date(year, month, day)

    # And returning that variable to the function
    return birthday


# Here we calculate the number of days between this year's birthday and today
def compute_difference_in_days(date1, date2):
    # Because the birth year is most likely not in the current year, we need to turn the birthday variable we use
    # for the calculation into this year's birthday date (e.g. if born on 01.01.1990, we need to turn it into
    # 01.01. 2018 (it is 2018 at the time of writing), otherwise our delta calculation will basically only show the user
    # how many days he is old
    bday_current_year = datetime.date(date2.year, date1.month, date1.day)

    # Now we take this year's birthday and subtract today from it
    days_from_bday = bday_current_year - date2

    # Finally, we return the number of days from the birthday to the function
    return days_from_bday.days


def print_birthday_information(days):
    if days < 0:
        print("Your birthday was {} days ago.".format(-days))
    elif days > 0:
        print("Your birthday is in {} days.".format(-days))
    else:
        print("Today is your birthday. Happy birthday!")


def main():
    print_header()
    bday = get_birthday_from_user()
    today = datetime.date.today()
    number_of_days = compute_difference_in_days(bday, today)
    print_birthday_information(number_of_days)


main()