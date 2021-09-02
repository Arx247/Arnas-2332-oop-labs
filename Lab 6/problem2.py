# Arnas Oonsadao, 633040233-2
"""
Lab 6 Input and Output: Problem 2
"""
file_name = input("Enter a file name: ")
with open(f'{file_name}') as f:
    print(f.read())
    #print(contents)