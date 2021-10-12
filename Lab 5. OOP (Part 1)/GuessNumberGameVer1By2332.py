#Arnas Oonsadao, 633040233-2
"""""
Exercise: GuessNumberGame using OOP
"""""

from random import randint

#class GuessNumberGameVer1:
class GuessNumberGameVer1:
    # class attribute1
    _numOfGames = 0

    def __init__(self, minNum = 1, maxNum = 10, maxTries = 3):
        self._minNum = minNum
        self._maxNum = maxNum
        self._maxTries = maxTries
        GuessNumberGameVer1.updateNumOfGames()

    #2 @classmethod
    @classmethod
    def updateNumOfGames(cls):
        cls._numOfGames = cls._numOfGames + 1
        cls._MAX_GUESSES = 20

    @classmethod
    def getNumOfGames(cls):
        return cls._numOfGames

    def __str_(self):
        return f"Guess number game:({self._minNum}, {self._maxNum}, {self._maxTries})"

    def playGame(self):
        correct_input = False
        numTries = self._maxTries
        # random number
        answer = randint(self._minNum, self._maxNum)
        print(f"GuessNumberGame with min number as {self._minNum}, max number as {self._maxNum}, max num of tries as {self._maxTries}")
        while not correct_input:
            guess = input(f"Please enter a guess ({self._minNum}, {self._maxNum}):")
            # print (f"Guess is {guess}")
            if int(guess) == answer:
                #print(f"Guess Number Game with min number as {self._minnum), max number as {self._maxNum), max num of tr: while not correct input:
                print(f"Congratulations! That's correct")
                correct_input = True
            elif int(guess) > answer:
                numTries -= 1
                print(f"Please type a lower number! The number of remaining tries is {numTries}")
            elif int(guess) < answer:
                numTries -= 1
                print(f"Please type a higher number! The number of remaining tries is {numTries}")
            else:
                print("Sorry, please keep trying")
            # Non number of Tries
            if numTries == 0:
                print(f"Sorry that you run out of the number of tries")
                correct_input = True

if __name__ == "__main__":
    gng1 = GuessNumberGameVer1()
    gng2 = GuessNumberGameVer1(105, 8)
    gng3 = GuessNumberGameVer1(5, 8, 4)
    print(gng3)
    print(f"The current number of games is {GuessNumberGameVer1.getNumOfGames()}")
    gng3.playGame()



    # gng1 = GuessNumberGameVer1()
    # gng2 = GuessNumberGameVer1(105, 8)
    # gng3 = GuessNumberGameVer1(5, 8, 4)
    # print(gng3)
    # print(f"The current number of games is {GuessNumberGameVer1.getNumOfGames()}")
    # gng3.playGame()

# Test condition if, elif
# if int(guess) == answer:
#     # print(f"Guess Number Game with min number as {self._minnum), max number as {self._maxNum), max num of tr: while not correct input:
#     print(f"Congratulations! That's correct")
#     correct_input = True
# elif int(guess) > answer:
#     numTries -= 1
#     print(f"Please type a lower number! The number of remaining tries is {numTries}")
# elif int(guess) < answer:
#     numTries -= 1
#     print(f"Please type a higher number! The number of remaining tries is {numTries}")
# else:
#     print("Sorry, please keep trying")
# # Non number of Tries
# if numTries == 0:
#     print(f"Sorry that you run out of the number of tries")
#     correct_input = True
