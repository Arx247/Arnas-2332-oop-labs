def demo_prob1():
    import random
    n = random.randint(1, 10)

    print(f"{n}")
    #print(f"The final total is {total}")



MAX_NUM_GUESSES = 5
n = demo_prob1()

def demo_prob2():
    num_guesses = MAX_NUM_GUESSES
    while n != 0:
        guess_word = input("Enter a word:")
        if guess_word == 'n':
            print("Congrats that you can guess the word correctly")
            break
        if guess_word < 'n':
                print("Your guess is too low.")
        if guess_word > 'n':
                print("Your guess is too high.")
        else:
            num_guesses = num_guesses - 1
            print(f"Incorrect! You have {num_guesses} guesses left")



if __name__ == "__main__":
    demo_prob2()