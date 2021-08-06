# Arnas Oonsadao, 633040233-2
"""
Lab 3 Loops and Functional Programming Functions : Problem 1
"""

import random

random_randint = random.randint(1, 10)
MAX_NUM_GUESSES = 5
def guess_remaining():
    if MAX_NUM_GUESSES > 1:
        print("You have %s guess remaining"%(MAX_NUM_GUESSES))
    else:
        print("You have %s guess remaining"%(MAX_NUM_GUESSES))

for i in range(5):
    integer = int(input("Enter a integer to guess:"))
    if integer < random_randint:
        MAX_NUM_GUESSES = MAX_NUM_GUESSES - 1
        print("Try a higher number.")
        guess_remaining()
    elif integer > random_randint:
        MAX_NUM_GUESSES = MAX_NUM_GUESSES - 1
        print("Try a lower number.")
        guess_remaining()
    else:
        print("Congrats that you can guess the number correctly")
        break

if __name__ == "__main__":
    guess_remaining()