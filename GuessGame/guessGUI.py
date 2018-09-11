from tkinter import *
from tkinter import messagebox

from GuessGame.Guess import *
from GuessGame.myInput import *

from GuessGame.myFont import *

def guessGUI(frame, game, var):
    #label
    label = Label(frame, textvariable = var, font = myfont['label'])
    label.pack(pady = 10)
    label.place(x = 200, y = 205, width = 400)
    var.set("Enter a number in range %3d ~ %3d" % (game.left, game.right))

    #input box
    input_box = Entry(frame, font = myfont['input'], justify = 'center')
    input_box.pack(pady = 10)
    input_box.place(x = 250, y = 265, width = 300)

    #function for enter button
    def input_number():
        number = input_by_entry(input_box)
        print('number:', number)
        if game.guess(number):
            #if correct: show messagebox
            messagebox.showinfo(message = "Correct!!")
        else:
            var.set("Enter a number in range %3d ~ %3d" % (game.left, game.right))


    #enter button
    enter = Button(frame, text = "enter", command = input_number, font = myfont['button'])
    enter.pack(pady = 10)
    enter.place(x = 350, y = 325, width = 100)
