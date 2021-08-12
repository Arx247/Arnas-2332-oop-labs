# Arnas Oonsadao, 633040233-2
"""
Lab 4 Errors and Exceptions: Problem 3
"""
def covid19_cases(num):
    correct_input = False
    while not correct_input:
        try:
            number = input(f"Enter the number of new infected Covid19 cases for {num}:")
            print("Stay healthy")
            if number < '0':
                print("You can only enter a non-negative integer")
                print("Stay healthy")
            return number
        except ValueError:
            print("Please enter a valid integer")
            print("Stay healthy")

def infected_cases():
    n1 = covid19_cases("yesterday")
    n2 = covid19_cases("today")
    dif = abs(float(n1) - float(n2))
    print(f'The difference of the new infected cases is {dif:0.02f} %')

if __name__ == "__main__":
    infected_cases()