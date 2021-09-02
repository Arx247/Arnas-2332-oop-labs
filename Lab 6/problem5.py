# Arnas Oonsadao, 633040233-2
"""
Lab 6 Input and Output: Problem 5 Flexible number of arguments
"""
with open('words.txt','r') as f:
    list_of_lists = [(line.strip()).split() for line in f]
    f.close()
    print(list_of_lists)