# Arnas Oonsadao, 633040233-2
"""
Lab 7 OOP (Part 1: Class and Object) : Problem 4
"""
class Cat:
    # class attribute
    legs_num = "4"


    # Initializer / Instance Attributes
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def print_info(self):
        print(f"Cat name is {self.name} and its color is {self.color}")


    #@classmethod and @staticmethod
    @classmethod
    def get_num_legs(self):
        return self.legs_num
    @staticmethod
    def get_owner_name():
        return "Lalisa Manobal."


if __name__ == '__main__':
    leo = Cat("Leo", "brown")
    luca = Cat("Lily", "white")
    leo.print_info()
    luca.print_info()
    print(f"The number of legs of all cats is {Cat.get_num_legs()}")
    print(f"The owner of these cats is {Cat.get_owner_name()}")