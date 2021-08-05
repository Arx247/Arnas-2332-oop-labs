# Arnas Oonsadao, 633040233-2
"""
Lab 3 Loops and Functional Programming Functions : Problem 5
"""
from functools import reduce
def check_positive(n):
    if n > 0 and (n % 2) != 0:
        return True

def compute_sum_positive_odd_numbers():
    positive_odd = list(filter(lambda x: (x % 2 == 1 and x > 0), num))
    sum_positive_odd = reduce ((lambda x, y: x + y), positive_odd)
    return print(sum_positive_odd)

num = list(map(int, input("Enter numbers in the list: ").split()))
if __name__ == '__main__':
  compute_sum_positive_odd_numbers()


