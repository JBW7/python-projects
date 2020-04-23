from tkinter import *
import tkinter as tk

screen = Tk()
screen.geometry("530x600")
screen.title("Tic Tac Toe")


# canvas
canvas = Canvas(screen, height = 500, width = 500, bg = "white")
line = canvas.create_line(166,0, 166,500, width = 5, fill = "black")
line = canvas.create_line(332,0, 332,500, width = 5, fill = "black")
line = canvas.create_line(0,166, 500,166, width = 5, fill = "black")
line = canvas.create_line(0,332, 500,332, width = 5, fill = "black")
canvas.grid(row = 1, column = 0, padx = 15, rowspan = 3, columnspan = 3)


# button font and size
class Warspyking(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master)
        self.rowconfigure(0, minsize=kwargs.pop('height', None))
        self.columnconfigure(0, minsize=kwargs.pop('width', None))
        self.btn = tk.Button(self, **kwargs)
        self.btn.grid(row=0, column=0, sticky="nsew")
        self.config = self.btn.config

font = ("Courier", 175)

# turn variable
global turn
turn = 0

# def button
def button(position):
    global turn
    turn += 1

    if turn == 1:
        symbol = "X"
    
    if turn == 2:
        symbol = "O"
    
    if turn == 3:
        symbol = "X"

    if turn == 4:
        symbol = "O"

    if turn == 5:
        symbol = "X"

    if turn == 6:
        symbol = "O"

    if turn == 7:
        symbol = "X"

    if turn == 8:
        symbol = "O"

    if turn == 9:
        state = DISABLED

    if position == 1 :
        button_1 = Warspyking(screen, text = symbol, height = 9, width = 17, font = font )
        button_1.grid(row = 1, column = 0, padx = (17, 350), pady = (23, 365))

    if position == 2 :
        button_2 = Warspyking(screen, text = symbol, height = 9, width = 17, font = font )
        button_2.grid(row = 1, column = 0, padx = (17, 350), pady = (195, 200))

    if position == 3 :
        button_3 = Warspyking(screen, text = symbol, height = 9, width = 17, font = font )
        button_3.grid(row = 1, column = 0, padx = (17, 350), pady = (370, 50))
    
    if position == 4 :
        button_4 = Warspyking(screen, text = symbol, height = 9, width = 17, font = font )
        button_4.grid(row = 1, column = 0, padx = (179, 180), pady = (23, 365))

    if position == 5 :
        button_5 = Warspyking(screen, text = symbol, height = 9, width = 17, font = font )
        button_5.grid(row = 1, column = 0, padx = (179, 180), pady = (195, 200))

    if position == 6 :
        button_6 = Warspyking(screen, text = symbol, height = 9, width = 17, font = font )
        button_6.grid(row = 1, column = 0, padx = (179, 180), pady = (370, 50))
    
    if position == 7 :
        button_7 = Warspyking(screen, text = symbol, height = 9, width = 17, font = font )
        button_7.grid(row = 1, column = 0, padx = (355, 15), pady = (23, 365))

    if position == 8 :
        button_8 = Warspyking(screen, text = symbol, height = 9, width = 17, font = font )
        button_8.grid(row = 1, column = 0, padx = (355, 15), pady = (195, 200))

    if position == 9 :
        button_9 = Warspyking(screen, text = symbol, height = 9, width = 17, font = font )
        button_9.grid(row = 1, column = 0, padx = (355, 15), pady = (370, 50))

    # player__
    if turn == 1:
        player_text = "PLAYER 2"
        player_label = Label(screen, text = player_text)
        player_label.config(font=("Courier", 44))
        player_label.config(anchor = CENTER)
        player_label.grid(row = 0, column = 0, columnspan = 3)

    if turn == 2:
        player_text = "PLAYER 1"
        player_label = Label(screen, text = player_text)
        player_label.config(font=("Courier", 44))
        player_label.config(anchor = CENTER)
        player_label.grid(row = 0, column = 0, columnspan = 3)

    if turn == 3:
        player_text = "PLAYER 2"
        player_label = Label(screen, text = player_text)
        player_label.config(font=("Courier", 44))
        player_label.config(anchor = CENTER)
        player_label.grid(row = 0, column = 0, columnspan = 3)

    if turn == 4:
        player_text = "PLAYER 1"
        player_label = Label(screen, text = player_text)
        player_label.config(font=("Courier", 44))
        player_label.config(anchor = CENTER)
        player_label.grid(row = 0, column = 0, columnspan = 3)

    if turn == 5:
        player_text = "PLAYER 2"
        player_label = Label(screen, text = player_text)
        player_label.config(font=("Courier", 44))
        player_label.config(anchor = CENTER)
        player_label.grid(row = 0, column = 0, columnspan = 3)

    if turn == 6:
        player_text = "PLAYER 1"
        player_label = Label(screen, text = player_text)
        player_label.config(font=("Courier", 44))
        player_label.config(anchor = CENTER)
        player_label.grid(row = 0, column = 0, columnspan = 3)

    if turn == 7:
        player_text = "PLAYER 2"
        player_label = Label(screen, text = player_text)
        player_label.config(font=("Courier", 44))
        player_label.config(anchor = CENTER)
        player_label.grid(row = 0, column = 0, columnspan = 3)

    if turn == 8:
        player_text = "PLAYER 1"
        player_label = Label(screen, text = player_text)
        player_label.config(font=("Courier", 44))
        player_label.config(anchor = CENTER)
        player_label.grid(row = 0, column = 0, columnspan = 3)

    # win/lose
    
    


# starting player__
if turn == 0:
        player_text = "PLAYER 1"
        player_label = Label(screen, text = player_text)
        player_label.config(font=("Courier", 44))
        player_label.config(anchor = CENTER)
        player_label.grid(row = 0, column = 0, columnspan = 3)








# button
button_1 = Button(screen, height = 9, width = 17, command =lambda: button(1))
button_1.grid(row = 1, column = 0, padx = (17, 350), pady = (23, 365))

button_2 = Button(screen, height = 9, width = 17, command =lambda: button(2))
button_2.grid(row = 1, column = 0, padx = (17, 350), pady = (195, 200))

button_3 = Button(screen, height = 9, width = 17, command =lambda: button(3))
button_3.grid(row = 1, column = 0, padx = (17, 350), pady = (370, 50))

button_4 = Button(screen, height = 9, width = 17, command =lambda: button(4))
button_4.grid(row = 1, column = 0, padx = (179, 180), pady = (23, 365))

button_5 = Button(screen, height = 9, width = 17, command =lambda: button(5))
button_5.grid(row = 1, column = 0, padx = (179, 180), pady = (195, 200))

button_6 = Button(screen, height = 9, width = 17, command =lambda: button(6))
button_6.grid(row = 1, column = 0, padx = (179, 180), pady = (370, 50))

button_7 = Button(screen, height = 9, width = 17, command =lambda: button(7))
button_7.grid(row = 1, column = 0, padx = (355, 15), pady = (23, 365))

button_8 = Button(screen, height = 9, width = 17, command =lambda: button(8))
button_8.grid(row = 1, column = 0, padx = (355, 15), pady = (195, 200))

button_9 = Button(screen, height = 9, width = 17, command =lambda: button(9))
button_9.grid(row = 1, column = 0, padx = (355, 15), pady =(370, 50))







screen.mainloop()