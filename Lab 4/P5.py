# Arnas Oonsadao, 633040233-2
"""
Lab 4 Errors and Exceptions: Problem 5
"""
import logging
n1 = int(input("Enter n1:"))
n2 = int(input("Enter n2:"))
result = n1 / n2
print(f"The result is {result}")
logging.basicConfig(level=logging.DEBUG)
logging.debug(f'n1 = {n1}')
logging.debug(f'n2 = {n2}')