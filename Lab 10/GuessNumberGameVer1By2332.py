#Arnas Oonsadao
#633040233-2
#Lab 10. Using OOP to Develop GuessNumberGame : P1
from random import randint

#class GuessNumberGameVer1
class GuessNumberGameVer1:
    #Attribute
    _num_of = 2

    def __init__(self, nummin=1, nummax=10, numtries=3):
        self._nummin = nummin
        self._nummax = nummax
        self._numtries = numtries

    def __str__(self):
        return f"Guss number game:{self._nummin, self._nummax, self._numtries}"

    #classmethod  getNumofGame(cls),playgame(self)
    @classmethod
    def getNumofGame(cls):
        cls._num_of = cls._num_of + 1
        return cls._num_of
        # GuessNumberGame
        # return GuessNumberGameVer1._num_of

    def playgame(self):
        answer = randint(self._nummin, self._nummax)
        tries = self._numtries
        print(
            f"GuessNumberGame with min number as {self._nummin},max number as {self._nummax},max num of tries as {self._numtries}")

        # While loop
        while True:
            guess = int(input("Pleas enter a guess (5,8):"))

            if int(guess) == answer:
                print("Congratulation! That's correct")
                break
            elif int(guess) > answer:
                tries -= 1
                print(f"Please type a higher number! The number of remaining tries is {tries}")
            elif int(guess) < answer:
                tries -= 1
                print(f"Please type a lower number! The number of remaining tries is {tries}")

            if tries == 0:
                print("Sorry, please keep trying")
                break

if __name__ == "__main__":
    #Show
    gng1 = GuessNumberGameVer1()
    gng2 = GuessNumberGameVer1(5, 8)
    gng3 = GuessNumberGameVer1(5, 8, 4)
    print(gng3)
    print(f"The current number of game is {GuessNumberGameVer1.getNumofGame()}")
    gng3.playgame()

# while True:
#     guess = int(input("Pleas enter a guess (5,8):"))
#
#     if int(guess) == answer:
#         print("Congratulation! That's correct")
#         break
#     elif int(guess) > answer:
#         tries -= 1
#         print(f"Please type a higher number! The number of remaining tries is {tries}")
#     elif int(guess) < answer:
#         tries -= 1
#         print(f"Please type a lower number! The number of remaining tries is {tries}")
#
#     if tries == 0:
#         print("Sorry, please keep trying")
#         break