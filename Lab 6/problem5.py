# Arnas Oonsadao, 633040233-2
"""
Lab 4 Errors and Exceptions: Problem 5
"""
with open('words.txt','r') as f:
    list_of_lists = [(line.strip()).split() for line in f]
    f.close()
    print(list_of_lists)