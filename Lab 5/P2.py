# Arnas Oonsadao, 633040233-2
"""
Lab 5 Functions : Problem 2
"""
import math
def hypotenuse(a,b):
    try:
        n = math.sqrt((a**2) + (b**2))
        return (n)
    except TypeError:
        return None

hypotenuse(3.0, 4.0)
hypotenuse(3, 4)
hypotenuse(3, 4.0)

print(f"hypotenuse(3,4) is {hypotenuse(3.0,4.0)}")
print(f"hypotenuse('3', '4') is {hypotenuse('3', '4')}")
print(f"hypotenuse(3,'4') is {hypotenuse(3, '4.0')}")
