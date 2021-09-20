# !/user/bin/env python3

# Created by Trent Hodgins
# Created on 09/20/2021
# This is a guessing game program
# The user enters in a number between 1 and 100

import random


def main():
    # this function checks to see if the user guessed the correct number
    random_number = random.randint(1, 100)
    # a number between 1 and 100

    # input
    guessed_number = int(input("Guess a number between 0 and 100 (integer): "))
    print("")

    # process and output
    if random_number == guessed_number:
        print("You Guessed Correctly")
    else:
        print("You Guessed Wrong!")

    print("\nDone")


if __name__ == "__main__":
    main()
