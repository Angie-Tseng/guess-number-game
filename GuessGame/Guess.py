'''
This is a class for Guess-Number Game
'''

from random import *

class Guess:
    #global integers:
        #left
        #right
        #answer
    
    def newGame(self, left = 1, right = 100):
        self.left = left
        self.right = right
        self.answer = randrange(left, right + 1)
        print('answer:', self.answer, ', range:', left, right)

    def __init__(self, left = 1, right = 100):
        self.newGame(left, right)

    def guess(self, number):
        if self.left > number or self.right < number:
            return False

        if self.answer == number:
            return True

        if self.answer < number:
            self.right = number
        else:
            self.left = number
        print(self.left, self.right)
        return False