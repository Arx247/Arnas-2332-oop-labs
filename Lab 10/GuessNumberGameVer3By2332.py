#Arnas Oonsadao
#633040233-2
#Lab 10. Using OOP to Develop GuessNumberGame : P3
from GuessNumberGameVer2By2332 import GuessNumberGameVer2
from random import randint

#class GuessNumberGameVer1 import from P1 to ver 2
class GuessNumberGameVer3(GuessNumberGameVer2):
   def __init__(self, *args, **kwargs):
        super(GuessNumberGameVer2, self).__init__(*args, **kwargs)
        self.guesses = []
        self._numGuesses = 0

   @classmethod
   def getNumofGame(cls):
       cls._num_of = cls._num_of + 1
       return cls._num_of

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

   def playGames(self):
        gng1.playGame()
        while True:
            print(f"If want to play again? type 'y' to continue or 'q' to quit:")

            get_input_2 = input(f"Type 'a' to see all your guesses or 'g' to see a guess on a specific play:")
            if get_input_2 == 'y':
                self.guess.clear()
                numTries = self.maxTries
                gng1.playGames()
                break
            elif get_input_2 == 'q':
                exit()
            elif get_input_2 == 'a':
                gng1.showGuesses()
            elif get_input_2 == 'g':
                gng1.showSpecific()
            else:
                pass


if __name__ == "__main__":
    #Show
    gng1 = GuessNumberGameVer3()
    gng1.playgame()
    print("Now let's play only one game")
    gng1.playgame()
    gng2 = GuessNumberGameVer3(5, 8)
    gng3 = GuessNumberGameVer3(5, 8, 4)
    print(gng3)
    print(f"The current number of game is {GuessNumberGameVer3.getNumofGame()}")
    gng3.playgame()