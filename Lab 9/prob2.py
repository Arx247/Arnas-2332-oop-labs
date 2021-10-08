# Arnas Oonsadao, 633040233-2
"""
Lab 9 Abstract classes and UML diagrams : Problem 2
"""
from abc import ABC, abstractmethod
# import abc


class AbstractClassImage(ABC):
    @abstractmethod
    def load_image(self, image):
        pass

    @abstractmethod
    def save_image(self, image):
        pass


class Bitmap(AbstractClassImage):
    # def __init__(self, image):
    #     super(Bitmap, self).__init__(image)

    def load_image(self, image):
        self.image = image
        print(f'loading bitmap filename {self.image}')


    def save_image(self, image):
        self.image = image
        print(f'saving bitmap filename  {self.image} ')


class Jpeg(AbstractClassImage):
    # def __init__(self, name):
    #     super(Jpeg, self).__init__(name)
    #     self.image = []

    def load_image(self, image):
        self.image = image
        print(f'loading jpeg filename {self.image}')

    def save_image(self, image):
        self.image = image
        print(f'saving jpeg filename  {self.image} ')


if __name__ == "__main__":
    bitmap1 = Bitmap()
    bitmap1.save_image("kku.bmp")
    bitmap1.load_image("kku.bmp")
    jpeg1 = Jpeg()
    jpeg1.save_image("en.jpg")
    jpeg1.load_image("en.jpg")