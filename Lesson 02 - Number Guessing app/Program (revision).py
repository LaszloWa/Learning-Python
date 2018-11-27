import random


def main():
    print_header()
    user_name = input("Hi. What's your name? ")
    play = "GO"
    while play == "GO":
        number_guessing(user_name)
        play = play_again()


def print_header():
    print("----------------------------------------")
    print("          Number Guessing App")
    print("----------------------------------------")
    print()


def number_guessing(user_name):
    rand_num = random.randint(0, 100)

    user_guess = -1

    while user_guess != rand_num:

        try:
            user_guess = int(input("Please guess a number between 0 and 100. "))
        except ValueError:
            print("Sorry, but you have to enter a whole number between 0 and 100.")
            continue

        if user_guess < 0:
            print("Sorry, but your number is too small, please choose a number between 0 and 100.")
            continue
        elif user_guess > 100:
            print("Sorry, but your number is too large, please choose a number between 0 and 100.")
            continue
        else:
            pass

        if user_guess < rand_num:
            print("Sorry, but your guess is too LOW.")
        elif user_guess > rand_num:
            print("Sorry, but your guess is too HIGH.")
        elif user_guess == rand_num:
            print("Congratulations {}, you guessed the number {} correctly!".format(user_name, rand_num))


def play_again():
    user_choice = input("Would you like to play again[Y or N]? ")

    user_choice = user_choice.lower()

    if user_choice == "y":
        return "GO"
    elif user_choice == "n":
        return "NO"
    else:
        print("Sorry, I don't understand {}.".format(user_choice))


if __name__ == "__main__":
    main()
