# Arnas Oonsadao, 633040233-2
"""
Lab 3 Loops and Functional Programming Functions : Problem 4
"""
def letter():
    list_of_letters = list(words)
    print(f"characters in string are {list_of_letters}")

def Check_Vow(words):
    for vowel in 'AaEeIiOoUu':
        if vowel in words:
            print(vowel)

words = input("Enter a string: ")
#vowels = "AaEeIiOoUu"


if __name__ == "__main__":
    letter()
    print("The entered string is %s and the result of convert a vowel to uppercase is" % words)
    Check_Vow(words)