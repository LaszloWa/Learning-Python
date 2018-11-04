# After having completed lesson 03, I am revisiting this lesson to see if I can build this app on my own.

import random

def print_header():
    print("-----------------------")
    print("      NUMBERS APP")
    print("-----------------------")


def guessing_iteration():
    random_number = random.randint(0, 100)
    guess = -1
    print("Guess a number between 0 and 100.")
    print()

    while guess != random_number:
        guess = int(input("Please guess a number: "))
        if guess < random_number:
            print("The value is too LOW. Please try again.")
        elif guess > random_number:
            print("The value is too HIGH. Please try again.")
        else:
            print("Congratulations! You guessed the number {} correctly!".format(random_number))

def main():
    print_header()
    guessing_iteration()

main()
