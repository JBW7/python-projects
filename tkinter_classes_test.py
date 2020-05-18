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

'''
https://www.youtube.com/watch?v=Jl1xsH6MR1g&list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&index=43
'''

