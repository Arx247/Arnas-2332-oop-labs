#Arnas Oonsadao
#633040233-2
# Lab 11.  Useful modules : Problem 5.  Simple Maths Script Using Command Line Arguments
import sys
try: #use try and except [may show error]
    operator = sys.argv[1]
    operand_1 = sys.argv[2]
    operand_2 = sys.argv[3]
    operators = ["+", "-", "x", "/"]
    try: #use try and except [may show error]
        operand_1 - float(sys.argv[2])
        operand_2 = float(sys.argv[3])
        if operator in ["+", "-", "x", "/"]:
            if operator == "+":
                print(f"{operand_1} + {operand_2} is {operand_1 + operand_2}")
            elif operator == "-":
                print(f"{operand_1} - {operand_2} is {operand_1 - operand_2}")
            elif operator == "x":
                print(f"{operand_1} x {operand_2} is {operand_1 * operand_2}")
            elif operator == "/":
                try: #use try and except [may show error]
                    print(f"{operand_1} / {operand_2} is {operand_1 / operand_2}")
                except ZeroDivisionError: #use try and except [may show error]
                    print(f"{operand_1} cannot be divided by {operand_1}")
            else:
                print(f"{operator} is not in {operators}")
    except ValueError: #use try and except [may show error]
        print("Operands are invalid. They are not numbers")

except IndexError: #use try and except [may show error]
    if sys.argv[1] == "Q" or sys.argv[1] == "q":
        print("Program quit...")
        quit() # exit the program
    else:
        print(f"Usage: python3 {sys.argv[0]} <operator> <operand1> <operand2>")

        # if operator in ["+", "-", "x", "/"]:
        #     if operator == "+":
        #         print(f"{operand_1} + {operand_2} is {operand_1 + operand_2}")
        #     elif operator == "-":
        #         print(f"{operand_1} - {operand_2} is {operand_1 - operand_2}")
        #     elif operator == "x":
        #         print(f"{operand_1} x {operand_2} is {operand_1 * operand_2}")
        #     elif operator == "/":
        #         try:
        #             print(f"{operand_1} / {operand_2} is {operand_1 / operand_2}")
        #         except ZeroDivisionError:
        #             print(f"{operand_1} cannot be divided by {operand_1}")
        #     else:
        #         print(f"{operator} is not in {operators}")