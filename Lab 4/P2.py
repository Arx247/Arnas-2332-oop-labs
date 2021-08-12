# Arnas Oonsadao, 633040233-2
"""
Lab 4 Errors and Exceptions: Problem 2
"""
def floating_point_number(n):
    correct_input = False
    while not correct_input:
        try:
            number = float(input(f"Enter {n} floating point number:"))
            return number
        except ValueError:
            print("Please enter a valid floating point number")
def enter_operator():
    n1 = floating_point_number("the first")
    n2 = floating_point_number("the second")
    correct_input = False
    while not correct_input:
        try:
            OP = input("Please enter an operator (+,-,*,/): ")
            if OP == "+":
                answer = n1 + n2
                print(f'The answer of {n1} + {n2} is {answer}')
                break
            if OP == "-":
                answer = n1 - n2
                print(f'The answer of {n1} - {n2} is {answer}')
                break
            if OP == "*":
                answer = n1 * n2
                print(f'The answer of {n1} * {n2} is {answer}')
                break
            if OP == "/":
                try:
                    answer = n1 / n2
                    print(f'The answer of {n1} / {n2} is {answer}')
                    break
                except ZeroDivisionError:
                    print("Cannot divide by zero")
                    break
        except ValueError:
            print("Unknown operator")
            break

if __name__ == "__main__":
    enter_operator()