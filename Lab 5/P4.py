# Arnas Oonsadao, 633040233-2
"""
Lab 5 Functions : Problem 4
"""
def get_operand(n):
    correct_input = False
    while not correct_input:
        try:
            number = input(f"Please enter {n} operand('q' to quit): ")
            if number == 'q' or number == 'Q':
                exit()
            try:
                number = float(number)
                return number
            except ValueError:
                raise ValueError
        except ValueError:
            print("Please enter a floating point number")


def check_operator(OP, n1, n2):
    if OP == '+':
        answer = n1 + n2
        print(f'{n1 :.1f} + {n2 :.1f} = {answer :.0f}')
        obust_calculator()
    if OP == '-':
        answer = n1 - n2
        print(f'{n1 :.1f} - {n2 :.1f} = {answer :.0f}')
        obust_calculator()
    if OP == '*':
        answer = n1 * n2
        print(f'{n1} * {n2} = {answer }')
        obust_calculator()
    if OP == '/':
        try:
            answer = n1 / n2
            print(f'{n1 :.1f} / {n2 :.1f} = {answer :.0f}')
            obust_calculator()
        except ZeroDivisionError:
            print("Cannot divide by zero")
            print("We cannot perform your requested calculation")
            obust_calculator()
    else :
        print("Operation must be ADD, SUM, MUL or DIV")


def obust_calculator():
    n1 = get_operand("the first")
    n2 = get_operand("the second")
    correct_input = False
    while not correct_input:

        try:
            OP = input("Please enter an operator ('+','-','*','/'): ")
            answer = input("Enter output format (float, int): ")
            if answer == 'int':
                n1 = int(n1)
                n2 = int(n2)
                check_operator(OP, n1, n2)
            if answer == 'float':
                n1 = float(n1)
                n2 = float(n2)
                check_operator(OP, n1, n2)

        except ValueError:
            print("Operation must be ADD, SUM, MUL or DIV")
            obust_calculator()


if __name__ == "__main__":
    obust_calculator()