def letter():
    list_of_letters = list(words)
    print(f"chr are {list_of_letters}")

def Check_Vow(words, vowels):
    final = [each for each in words if each in vowels]
    print("The entered string is %s and the result of convert a vowel to uppercase is" % words)
    print(final)

words = input("Enter a string: ")
vowels = "AaEeIiOoUu"


if __name__ == "__main__":
    letter()
    Check_Vow(words, vowels)