from tkinter import *
import time


root = Tk()
root.geometry("400x300")



def start_clock():
    h = time.strftime("%I") # %I FOR 12 HOUR FORMAT, %H FOR 24 HOUR FORMAT
    m = time.strftime("%M")
    s = time.strftime("%S")


    time_label.config(text = h + ":" + m + ":" + s)
    

    root.after(1000, start_clock)



time_label = Label(root, text = "", font = ("Courier New", 60))
time_label.pack(pady = 20)


start_clock()







root.mainloop()