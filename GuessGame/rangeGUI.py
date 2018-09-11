from tkinter import *
from tkinter import messagebox

from GuessGame.Guess import *

from GuessGame.myInput import *
from GuessGame.myFont import *

def rangeGUI(frame, game, var):
    #range label
    range_label = Label(frame, text = "the range of number", font = myfont['label'])
    range_label.pack(pady = 10)
    range_label.place(x = 250, y = 25, width = 300)
    between_label = Label(frame, text = "~", font = myfont['label'])
    between_label.pack(pady = 10)
    between_label.place(x = 350, y = 75, width = 100)

    #input left
    input_left = Entry(
        frame, 
        font = myfont['input'],
        textvariable = StringVar(value = str(game.left)),
        justify = 'center'
    )
    input_left.pack(pady = 10)
    input_left.place(x = 250, y = 75, width = 100)
    
    #input right
    input_right = Entry(
        frame, 
        font = myfont['input'], 
        textvariable = StringVar(value = str(game.right)),
        justify = 'center'
    )
    input_right.pack(pady = 10)
    input_right.place(x = 450, y = 75, width = 100)

    #function for start button
    def start_button():
        print('start button')
        game.newGame(
            input_by_entry(input_left),
            input_by_entry(input_right)
        )
        var.set("Enter a number in range %3d ~ %3d" % (game.left, game.right))
    
    #game start button
    start = Button(frame, text = "start", command = start_button, font = myfont['button'])
    start.pack(pady = 10)
    start.place(x = 350, y = 125, width = 100)