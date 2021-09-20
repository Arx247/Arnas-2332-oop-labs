class Pet:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"I'm {self.name}")

    def move(self):
        print("moving ...")



class Cat:
    def __init__(self, name, owner, color):
        self.name = name
        self.owner = owner
        self.color = color

    def show_info(self):
        print(f"I'm {self.name}\n and is {self.color}\n belonging to {self.owner}")

    def move(self):
        print("Cat likes to walk more than ran")


class Dog(Cat):
    def __init__(self, name, owner, color):
        super().__init__(self, name, name)
        self.name = name
        self.owner = owner
        self.color = color


    def show_info(self):
        print(f"I'm {self.name}\n and is {self.color}\n belonging to {self.owner}")

    def move(self):
        print("Dong likes to run more than walk")
        print(f"Dog {self.name} eats cat {cat1.name} ")

    def get_eat_cat(self):

        return self.name
    def eat_cat(self, name):
        self.name = name


if __name__ == '__main__':
    pet1 = Pet("Thongdaeng")
    pet1.show_info()
    pet1.move()
    cat1 = Cat("Thongdee", "Manee", "white")
    cat1. show_info()
    cat1.move()
    dog1 = Dog("Thongdum", "Mana", "black")
    dog1.show_info()
    dog1.move()
    dog1.eat_cat(cat1)
