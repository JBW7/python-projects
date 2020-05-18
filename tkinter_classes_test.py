from tkinter import *

root = Tk()
root.title("Classes")

class Tkinter:

    def __init__ (self, master):

        self.button = Button(master, text = "click me", command = self.clicked)
        self.button.pack()

    def clicked(self):
        print("hello")

t = Tkinter(root)


root.mainloop()

