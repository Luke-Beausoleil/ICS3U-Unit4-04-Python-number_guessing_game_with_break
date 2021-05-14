#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: May 2021
# This program gets the user to guess a pseudo-random number

import random


def main():
    # this function generates a pseudo-random number and gets the user
    #   to guess the number

    # generate random number
    correct_number = 8  # a number from 0 - 9

    # process & output
    while True:
        guess_as_string = input("Guess a number from 0 - 9: ")  # input
        try:
            guess_as_int = int(guess_as_string)
            if guess_as_int == correct_number:
                break
            elif guess_as_int < correct_number:
                print("Too Low! Try Again")
            else:
                print("Too High! Try Again")
        except Exception:
            print("{0} is invalid. Try Again".format(guess_as_string))
    print("\nCorrect!")
    print("\nDone.")


if __name__ == "__main__":
    main()
