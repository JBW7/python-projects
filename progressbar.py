from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.geometry("400x200")

'''
determinate = full bar
indeterminate = only spots
'''

def start_p():
    for x in range(10) :
        progressbar["value"] += 5

        root.update_idletasks()

        time.sleep(1)



progressbar = ttk.Progressbar(root, orient = HORIZONTAL, length = 300, mode = "determinate")
progressbar.pack(pady = 20)


start_button = Button(root, text = "Start", font = ("Courier New", 20), command = start_p)
start_button.pack(pady = 20)


root.mainloop()