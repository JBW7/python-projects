from tkinter import *
from PIL import Image

screen = Tk()
screen.title("tkinter test")

image= ImageTk.PhotoImage(Image.open("download.png"))
label= Label(img=image)
label.pack()



screen.mainloop()



