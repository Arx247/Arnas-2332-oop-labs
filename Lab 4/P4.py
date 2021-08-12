# Arnas Oonsadao, 633040233-2
"""
Lab 4 Errors and Exceptions: Problem 4 'Using Debugger'
"""
def enter_integer():
    sum = 0
    count = 0
    average = 0
    while True:
        try:
            n = int(input("Enter an integer:"))
            if n < 0:
                break
            sum = sum + n
            count = count + 1

        except ValueError:
            print("Please enter a valid integer")

    avg = sum / count
    print(f"Average is {avg}")


if __name__ == "__main__":
    enter_integer()