#Arnas Oonsadao, 633040233-2
"""
Lab 2 Variables and Collections: Problem 4
"""
def Check_vowels(string, vowels):
    final = [each for each in string if each in vowels]
    print("Vowels in %s are %s"%(string,final))


string = input("Enter string input: ")
vowels = "AaEeIiOoUu"
Check_vowels(string, vowels)