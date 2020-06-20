from tkinter import *
from tkinter import filedialog
import os


root = Tk()
root.geometry("100x100")


def open_program():
    # GET PROGRAM LOCATION
    program = filedialog.askopenfilename()

    # OPEN PROGRAM
    os.system(program)


b = Button(root, text = "Open program", command = open_program)
b.pack()




root.mainloop()