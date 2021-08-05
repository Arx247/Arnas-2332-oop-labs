# Arnas Oonsadao, 633040233-2
"""
Lab 3 Loops and Functional Programming Functions : Problem 6
"""
from functools import reduce
def sum_of_the_square():
    [num.append(i) for i in range(1, inte + 1)]
    squa = list(map(lambda x: x * x, num))
    sum_squa = reduce(lambda x, y: x + y, squa)
    return print("The sum of the square of %s is %s"%(num,sum_squa))

num = []
inte = int(input("Enter an integer: "))

if __name__ == '__main__':
    sum_of_the_square()
