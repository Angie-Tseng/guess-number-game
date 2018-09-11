from tkinter import *
from random import *

from GuessGame.Guess import *

from GuessGame.guessGUI import *
from GuessGame.rangeGUI import *

def showGUI():
    gameGUI = GameGUI()
    gameGUI.showGUI()
    gameGUI.window.mainloop()

class GameGUI:
    def newGame(self, left = 1, right = 100):
        self.game = Guess(left, right)
        self.var = StringVar()

    def showGUI(self):
        print('showGUI')
        guessGUI(self.window, self.game, self.var)
        rangeGUI(self.window, self.game, self.var)
    
    def __init__(self):
        self.window = Tk()
        self.window.title("guess number")
        self.window.geometry("800x400")
        self.newGame()


'''
def main():
    gameGUI = GameGUI()
    gameGUI.showGUI()
    gameGUI.window.mainloop()


if __name__ == '__main__':
    main()

'''