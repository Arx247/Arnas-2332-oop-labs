# Arnas Oonsadao, 633040233-2
"""
Lab 3 Loops and Functional Programming Functions : Problem 1
"""

import random
n = random.randint(1, 10)
guess = 5
def guess_remaining():
    if guess > 1:
        print("You have %s guess remaining"%(guess))
    else:
        print("You have %s guess remaining"%(guess))

for i in range(5):
    integer = int(input("Enter a integer to guess:"))
    if integer < n:
        guess = guess - 1
        print("Try a higher number.")
        guess_remaining()
    elif integer > n:
        guess = guess - 1
        print("Try a lower number.")
        guess_remaining()
    else:
        print("Congrats that you can guess the number correctly")
        break

if __name__ == "__main__":
    guess_remaining()