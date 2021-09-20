class Rectangle:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'This rectangle has width as ' + str(self.x) + ' height as ' + str(self.y)

    def get_width(self):
        return self.x

    def get_height(self):
        return self.y

    def set_height(self, y):
        self.y = y

if __name__ == '__main__':
    rect1 = Rectangle(3,4)
    print(rect1)
    print(f'Width is {rect1.get_width()}')
    rect1.set_height(5)
    print(f'Height is {rect1.get_height()}')