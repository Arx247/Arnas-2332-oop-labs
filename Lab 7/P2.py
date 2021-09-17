# Arnas Oonsadao, 633040233-2
"""
Lab 7 OOP (Part 1: Class and Object) : Problem 2
"""
class Numbers:
    # Initializer / Instance Attributes
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        add1 = self.x + self.y
        return add1

    # @classmethod and @staticmethod
    @classmethod
    def display_factors(cls, num):
        if num % 2 == 0:
            num1 = num/2
            num2 = num/2
            return(f"Factor of {num} is {num1} and {num2}")
        elif num % 2 == 1:
            num += 1
            num1 = ((num / 2) - 1)
            num2 = num / 2
            return (f"Factor of {num} is {num1} and {num2}")
        else:
            print("please")

    @staticmethod
    def is_valid_divisor(check_num):
        if check_num != 0:
            return(f"{check_num} is a valid divisor")
        else:
            return (f"{check_num} is not a valid divisor")


# num1 = Number(2)
# num1.display_factors()
# num2 = Number(3)
# num2.display_factors()


if __name__ == '__main__':
    print(f'2 + 3 is {Numbers(2, 3).add()}')
    print(Numbers.display_factors(6))
    print(Numbers.display_factors(7))
    print(Numbers.display_factors(2))
    print(Numbers.display_factors(0))