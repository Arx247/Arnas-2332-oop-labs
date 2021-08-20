# Arnas Oonsadao, 633040233-2
"""
Lab 5 Functions : Problem 3
"""
def fibonacci():
    correct_input = False
    while not correct_input:
        try:
            n = int(input("Enter a non-negative integer:"))
            fact = 1
            if n >= 1:
                for i in range(1, n + 1):
                    fact = fact * i
                print("The factorial of %d is %d." % (n, fact))

            else:
                if n == 0:
                    print("The factorial of ", n, " is ")
                else:
                    print("Please enter an integer that is non-negative"),
        except ValueError:
            print("Please enter a valid integer")


if __name__ == "__main__":
    fibonacci()
