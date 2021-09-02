file_name = input("Enter a file name: ")
with open(f'{file_name}') as f:
    print(f.read())
    #print(contents)