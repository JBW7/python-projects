from tkinter import *
import tkinter as tk

screen = Tk()
screen.geometry("530x780")
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
        global button_1_clicked
        button_1_clicked = Warspyking(screen, text = symbol, height = 9, width = 17, font = font )
        button_1_clicked.grid(row = 1, column = 0, padx = (17, 350), pady = (23, 365))
        player = symbol

    if position == 2 :
        global button_2_clicked
        button_2_clicked = Warspyking(screen, text = symbol, height = 9, width = 17, font = font )
        button_2_clicked.grid(row = 1, column = 0, padx = (17, 350), pady = (195, 200))
        player = symbol

    if position == 3 :
        global button_3_clicked
        button_3_clicked = Warspyking(screen, text = symbol, height = 9, width = 17, font = font )
        button_3_clicked.grid(row = 1, column = 0, padx = (17, 350), pady = (370, 50))
        player = symbol
    
    if position == 4 :
        global button_4_clicked
        button_4_clicked = Warspyking(screen, text = symbol, height = 9, width = 17, font = font )
        button_4_clicked.grid(row = 1, column = 0, padx = (179, 180), pady = (23, 365))
        player = symbol

    if position == 5 :
        global button_5_clicked
        button_5_clicked = Warspyking(screen, text = symbol, height = 9, width = 17, font = font )
        button_5_clicked.grid(row = 1, column = 0, padx = (179, 180), pady = (195, 200))
        player = symbol

    if position == 6 :
        global button_6_clicked
        button_6_clicked = Warspyking(screen, text = symbol, height = 9, width = 17, font = font )
        button_6_clicked.grid(row = 1, column = 0, padx = (179, 180), pady = (370, 50))
        player = symbol
    
    if position == 7 :
        global button_7_clicked
        button_7_clicked = Warspyking(screen, text = symbol, height = 9, width = 17, font = font )
        button_7_clicked.grid(row = 1, column = 0, padx = (355, 15), pady = (23, 365))
        player = symbol

    if position == 8 :
        global button_8_clicked
        button_8_clicked = Warspyking(screen, text = symbol, height = 9, width = 17, font = font )
        button_8_clicked.grid(row = 1, column = 0, padx = (355, 15), pady = (195, 200))
        player = symbol

    if position == 9 :
        global button_9_clicked
        button_9_clicked = Warspyking(screen, text = symbol, height = 9, width = 17, font = font )
        button_9_clicked.grid(row = 1, column = 0, padx = (355, 15), pady = (370, 50))
        player = symbol

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

    # relation of postion and player
    global position_1
    global position_2
    global position_3
    global position_4
    global position_5
    global position_6
    
    
    
    # PLAYER 1
    ################################### COLUMN 1
    if position == 1 and player == "X":
        position_1 = "player_1_1"
    
    if position == 2 and player == "X":
        position_2 = "player_1_2"
    
    if position == 3 and player == "X":
        position_3 = "player_1_3"

    # win/lose
    if position_1 == "player_1_1" and position_2 == "player_1_2" and position_3 == "player_1_3":
        winner_label = Label(screen, text = "WINNER = PLAYER 1")
        winner_label.config(font=("Courier", 44))
        winner_label.config(anchor = CENTER)
        winner_label.grid(row = 0, column = 0, columnspan = 3)

    
    '''
    ################################### COLUMN 2
    if position == 4 and player == "X":
        position_4 = "player_1_4"
    
    if position == 5 and player == "X":
        position_5 = "player_1_5"
    
    if position == 6 and player == "X":
        position_6 = "player_1_6"

    # win/lose
    if position_4 == "player_1_4" and position_5 == "player_1_5" and position_6 == "player_1_6":
        winner_label = Label(screen, text = "WINNER = PLAYER 1")
        winner_label.config(font=("Courier", 44))
        winner_label.config(anchor = CENTER)
        winner_label.grid(row = 0, column = 0, columnspan = 3)
    '''


    

    
     
    


# starting player__
if turn == 0:
        player_text = "PLAYER 1"
        player_label = Label(screen, text = player_text)
        player_label.config(font=("Courier", 44))
        player_label.config(anchor = CENTER)
        player_label.grid(row = 0, column = 0, columnspan = 3)

# def clear button
def clear():
    button_1_clicked.grid_forget()
    button_2_clicked.grid_forget()
    button_3_clicked.grid_forget()
    button_4_clicked.grid_forget()
    button_5_clicked.grid_forget()
    button_6_clicked.grid_forget()
    button_7_clicked.grid_forget()
    button_8_clicked.grid_forget()
    button_9_clicked.grid_forget()



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

button_clear = Button(screen, height = 9, width = 17, text = "restart", command = clear)
button_clear.grid(row = 4, column = 0, )







screen.mainloop()