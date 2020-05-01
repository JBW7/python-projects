from tkinter import *

root = Tk()


time = 10

def countdown():
        global time
        time = time - 1
        label.config(text = time)
        label.after(1000, countdown)
    
       




label = Label(root, font = "times 20")
label.pack()

button = Button(root, command = countdown, height = 100, width = 100, background = "red")
button.pack()

root.mainloop()