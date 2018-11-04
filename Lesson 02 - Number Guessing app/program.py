# importing the random module for generating the random number of this game
import random

print("---------------------------------")
print("     GUESS THE NUMBER APP")
print("---------------------------------")
print()

# This generates the random number the user will try and guess
the_number = random.randint(0, 100)

# Here we define guess, which will be the user's guess.
# Here it is defined a 'dummy', it will be filled in the while-loop below.
guess = -1

# The while-loop cycles enables the user to guess the number until he guesses correctly.
while guess != the_number:
    # guess_test gives the user input as a STRING.
    guess_text = input("Please enter your guess: ")
    # guess converts the string into an integer. This needs to be done in order to compare it to the_number
    # (you can't compare strings with integers)
    guess = int(guess_text)
    if guess < the_number:
        print("The entered number is too LOW, please try again.")
    elif guess > the_number:
        print("The entered number is too HIGH, please try again.")
    else:
        print("Congratulations, you won! The number was {}".format(the_number))