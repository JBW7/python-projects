from tkinter import *
from tkinter import messagebox
import math


root = Tk()
root.geometry("450x330")
root.title("Pythagoras")


# CREATE CANVAS
canvas = Canvas(root, height = 170, width = 225, bg = "white")

# CREATE LINES
line = canvas.create_line(40,15, 40,135,  40,135, 220,135,  40,15, 220,135, width = 5, fill = "black")

text_a = canvas.create_text(20, 75, font = ("Courier New", 40), text="a")

text_b = canvas.create_text(120, 157, font = ("Courier New", 40), text="b")

text_b = canvas.create_text(145, 57, font = ("Courier New", 40), text="c")

canvas.grid(row = 0, column = 2, rowspan = 4, padx = (30, 0), pady = (0, 50))


# INPUTS
a_label = Label(root, text = "a = ", font = ("Courier New", 40))
a_label.grid(row = 0, column = 0, pady = (30, 0))

a_entry = Entry(root, width = 3, font = ("Courier New", 40), justify = CENTER)
a_entry.grid(row = 0, column = 1, pady = (30, 0))


b_label = Label(root, text = "b = ", font = ("Courier New", 40))
b_label.grid(row = 1, column = 0)

b_entry = Entry(root, width = 3, font = ("Courier New", 40), justify = CENTER)
b_entry.grid(row = 1, column = 1)


c_label = Label(root, text = "c = ", font = ("Courier New", 40))
c_label.grid(row = 2, column = 0)

c_entry = Entry(root, width = 3, font = ("Courier New", 40), justify = CENTER )
c_entry.grid(row = 2, column = 1)

# GET ANSWER FOR A
def get_a():
    a = a_entry.get()
    b = b_entry.get()
    c = c_entry.get()
    
    c = int(c)
    b = int(b)
    
    c = c * c
    b = b * b

    answer_a = c - b

    answer_a = math.sqrt(answer_a)

    answer_s = (answer_a).is_integer()

    if answer_s == True :
        answer_a = str(answer_a)
        answer_l = len(answer_a)

        answer_ = answer_l - 2

        answer_a = answer_a.replace(answer_a[answer_:], "")
    else :
        
        answer_a = str(answer_a)

    
    find_x_button.grid_forget()
    
    global answer_label
    answer_label = Label(root, text = "X = " + answer_a, font = ("Courier New", 40))
    answer_label.grid(row = 3, columnspan = 3, pady = (20, 0))

# GET ANSWER FOR B
def get_b():
    a = a_entry.get()
    b = b_entry.get()
    c = c_entry.get()
    
    c = int(c)
    a = int(a)
    
    c = c * c
    a = a * a

    answer_b = c - a

    answer_b = math.sqrt(answer_b)

    answer_s = (answer_b).is_integer()

    if answer_s == True :
        answer_b = str(answer_b)
        answer_l = len(answer_b)

        answer_ = answer_l - 2

        answer_b = answer_b.replace(answer_b[answer_:], "")
    else :
        answer_b = str(answer_b)

    
    find_x_button.grid_forget()
    
    global answer_label
    answer_label = Label(root, text = "X = " + answer_b, font = ("Courier New", 40))
    answer_label.grid(row = 3, columnspan = 3, pady = (20, 0))

# GET ANSWER FOR C
def get_c():
    a = a_entry.get()
    b = b_entry.get()
    c = c_entry.get()
    
    b = int(b)
    a = int(a)
    
    b = b * b
    a = a * a

    answer_c = b + a

    answer_c = math.sqrt(answer_c)

    answer_s = (answer_c).is_integer()

    if answer_s == True :
        answer_c = str(answer_c)
        answer_l = len(answer_c)

        answer_ = answer_l - 2

        answer_c = answer_c.replace(answer_c[answer_:], "")
    else :
        answer_c = str(answer_c)

    
    find_x_button.grid_forget()
    
    global answer_label
    answer_label = Label(root, text = "X = " + answer_c, font = ("Courier New", 40))
    answer_label.grid(row = 3, columnspan = 3, pady = (20, 0))


# CLEAR FUNCTION
def clear():
    a_entry.delete(0, END)
    b_entry.delete(0, END)
    c_entry.delete(0, END)

    answer_label.destroy()

    find_x_button.grid(row = 3, column = 0, columnspan = 3, pady = (20, 0))


# FIND WHICH ENTRY IS UNKNOWN
def find_x():
    a = a_entry.get()
    b = b_entry.get()
    c = c_entry.get()

    if a == "x" :
        get_a()
    else :

        if a == "X" :
            get_a()
        else :
            
            if b == "x" :
                get_b()
            else :

                if b == "X" :
                    get_b()
                else :

                    if c == "x" :
                        get_c()
                    else :

                        if c == "X" :
                            get_c()
                        else :
                            
                            messagebox.showerror(" ERROR ", "INPUT UNKNOWN SIDE AS X/ \n THERE MUST BE 1 UNKNOWN SIDE")
                            clear()


# FIND X BUTTON
find_x_button = Button(root, text = "Find X!", font = ("Courier New", 40), command = find_x)
find_x_button.grid(row = 3, column = 0, columnspan = 3, pady = (20, 0))

# CLEAR BUTTON
clear_button = Button(root, text = "Clear", font = ("Courier New", 15), command = clear)
clear_button.grid(row = 4, column = 0, columnspan = 3, pady = (5, 0))

# INFO TEXT
info_label = Label(root, text = "Input Unknown Side As X", font = ("Courier New", 10))
info_label.grid(row = 5, column = 0, columnspan = 3, pady = (10, 0))







root.mainloop()