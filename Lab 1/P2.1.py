#Lab 1 : Problem 2
#Problem 2.1
import random

def compute_avg_list(n):
    num = input(f'Enter {n} positive numbers: ')
    print(f'You entered {num}')
    str_numbers = num.split()
    print(f'Numbers are {str_numbers}')
    numbers = [float(i) for i in str_numbers]
    ag = (sum(numbers)) / n
    print(f'The average number of the list is {ag}')
    return ag

def test_compute_avg_list():
    min_number = 1
    max_number = 10
    n = random.randint(min_number, max_number)
    compute_avg_list(n)
    
    
if __name__ == '__main__':
    test_compute_avg_list()