from tkinter import *

screen = Tk()
screen.geometry("530x600")

# turn
turn = Label(screen, text = "player")
turn.config(font=("Courier", 44))
turn.config(anchor = CENTER)
turn.grid(row = 0, column = 0, columnspan = 3)


# canvas
canvas = Canvas(screen, height = 500, width = 500, bg = "white")
line = canvas.create_line(166,0, 166,500, width = 5, fill = "black")
line = canvas.create_line(332,0, 332,500, width = 5, fill = "black")
line = canvas.create_line(0,166, 500,166, width = 5, fill = "black")
line = canvas.create_line(0,332, 500,332, width = 5, fill = "black")
canvas.grid(row = 1, column = 0, padx = 15, rowspan = 3, columnspan = 3)

# def button
def button():
	return

# button
button_1 = Button(screen, height = 9, width = 17, command = button)
button_1.grid(row = 1, column = 0, padx = (17, 350), pady = (23, 365))

button_2 = Button(screen, height = 9, width = 17, command = button)
button_2.grid(row = 1, column = 0, padx = (17, 350), pady = (195, 200))

button_3 = Button(screen, height = 9, width = 17, command = button)
button_3.grid(row = 1, column = 0, padx = (17, 350), pady = (370, 50))

button_4 = Button(screen, height = 9, width = 17, command = button)
button_4.grid(row = 1, column = 0, padx = (179, 180), pady = (23, 365))








screen.mainloop()