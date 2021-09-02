# Arnas Oonsadao, 633040233-2
"""
Lab 4 Errors and Exceptions: Problem 3
"""
file_name = input("Enter a file name to read: ")
with open(f'{file_name}') as f:
    enter_text = input("Enter text to append: ")
    file_name2 = input("Enter a file name to write: ")
    print(f.read())
    with open(f"{file_name2}","a") as fi:
        fi.write(f"{enter_text}\n")
        with open(f"{file_name2}") as file:
            print(file.read())



