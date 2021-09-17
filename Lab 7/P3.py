# Arnas Oonsadao, 633040233-2
"""
Lab 7 OOP (Part 1: Class and Object) : Problem 3
"""
import math
class Circle:
    # Initializer / Instance Attributes
    def __init__(self, radius):
        self.radius = radius

    #@staticmethod
    def calculate_area_circle(self):
        calculate_area = math.pi * (self.radius * 2)
        return calculate_area

    def calculate_the_perimeter(self):
        calculate_the_perimeter = ((2 * math.pi) * self.radius ** 2)
        return calculate_the_perimeter


if __name__ == '__main__':
    try:
        radius = float(input("Enter a radius: "))
        circle = Circle(radius)
        Circle(circle.calculate_area_circle())
        circle.calculate_the_perimeter()

        print(f"The circle with radius {radius} has the area as {circle.calculate_area_circle() :0.02f} and the perimeter as {circle.calculate_the_perimeter():0.02f} ")
    except ValueError:
        print("Please enter a valid floating-point number for the circle radius")
