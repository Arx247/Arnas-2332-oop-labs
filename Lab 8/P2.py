# Arnas Oonsadao, 633040233-2
"""
Lab 8 OOP (Part 2: Encapsulation, Inheritance, and Polymorphism) : Problem 2
"""
class Vehicle:
    def __init__(self, name, speed, mileage):
        self.name = name
        self.speed = speed
        self.mileage = mileage


class Car(Vehicle):
    def __init__(self, name, speed, mileage, num_door):
        self.name = name
        self.speed = speed
        mileage_comma = "{:,}".format(mileage) #add commas to a number
        self.mileage = mileage_comma
        self.num_door = num_door
        #print(f"Name: {self.name} speed: {self.speed} mileage: {self.mileage} num doors: {self.num_door}")
    def __str__(self):
        return "Name: " + str(self.name) + " speed: " + str(self.speed) + " mileage: " + str(self.mileage) + " num doors: " + str(self.num_door)


class Bus(Vehicle):
    def __init__(self, name, speed, mileage, capacity):
        self.name = name
        self.speed = speed
        mileage_comma = "{:,}".format(mileage)#add commas to a number
        self.mileage = mileage_comma
        self.capacity = capacity
        #print(f"Name: {self.name} speed: {self.speed} mileage: {self.mileage} capacity: {self.capacity}")

    def __str__(self):
        return "Name: " + str(self.name) + " speed: " + str(self.speed) + " mileage: " + str(self.mileage) + " capacity: " + str(self.capacity)

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed
        #print(f"Name: {self.name} speed: {self.speed} mileage: {self.mileage} capacity: {self.capacity}")


if __name__ == '__main__':
    car = Car('Toyota Vios', 90, 150000, 4)
    bus = Bus('School Volvo', 12, 200000,100)
    print(car)
    print(bus)
    bus.set_speed(30)
    print(bus)