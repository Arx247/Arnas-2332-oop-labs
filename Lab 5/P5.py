# Arnas Oonsadao, 633040233-2
"""
Lab 5 Functions : Problem 5
"""
# Arnas Oonsadao, 633040233-2
"""
Lab 5 Functions : Problem 5
"""
ADD, SUB, MUL, DIV = range(4)
def flexible_calculator(operator = ADD, format = float, *args):
    #ADD, SUB, MUL, DIV = range(4)
    if operator == MUL:
        result = 1
    else:
        result = 0
    if operator == ADD:
        for i in args:
            result += i
    elif operator == SUB:
        result = args[0]
        for i in range(len(args) - 1):
            result -= args[i + 1]
    elif operator == MUL:
        for i in args:
            result *= i
    elif operator == DIV:
        try:
            if len(args) == 0:
                raise ValueError("At least one number must be entered")
        except ValueError as err:
            print(err)
            return None
        else:
            for i in args:
                try:
                    a = i
                    result = a / i
                except ZeroDivisionError:
                    return "Cannot divide by zero"
    else:
        raise ValueError("Operator must be ADD,SUB,MUL or DIV")

    if format == float:
        result = float(result)
    elif format == int:
        result = int(result)
    else:
        raise ValueError("Format must be float or int")
    return result


print(f"flexible_calculate(ADD, int, 1) = {flexible_calculator(ADD, int,1)}")
print(f"flexible_calculate(ADD, int, 2, 3, 4) = {flexible_calculator(MUL, int, 2, 3, 4)}")
print(f"flexible_calculate(ADD, int, 1, 2) = {flexible_calculator(ADD, int, 1, 2)}")
print(f"flexible_calculate(ADD, int, 1, 2, 3, 4) = {flexible_calculator(ADD, int, 1, 2, 3, 4)}")
print(f"flexible_calculate(SUB, int, 6, 4, 9, 1) = {flexible_calculator(SUB, int,6, 4,9,1)}")
print(f"flexible_calculate(ADD, int, 10, 5, 2,) = {flexible_calculator(DIV, float, 10, 5, 2)}")
print(f"flexible_calculate(ADD, int, 5, 0) = {flexible_calculator(DIV, float, 5, 0)}")
