from tkinter import *
from PIL import ImageTk, Image

screen = Tk()
screen.geometry("350x500")
screen.title("Image")

# screen icon
screen.iconbitmap("d:/JOEY/python_pics/tesla_logo.ico")

# add pic
model_s = ImageTk.PhotoImage(Image.open("d:/JOEY/python_pics/model_s.JPG"))
model_3 = ImageTk.PhotoImage(Image.open("d:/JOEY/python_pics/model_3.JPG"))
model_x = ImageTk.PhotoImage(Image.open("d:/JOEY/python_pics/model_x.JPG"))
model_y = ImageTk.PhotoImage(Image.open("d:/JOEY/python_pics/model_y.JPG"))
roadster = ImageTk.PhotoImage(Image.open("d:/JOEY/python_pics/roadster.JPG"))
cybertruck = ImageTk.PhotoImage(Image.open("d:/JOEY/python_pics/cybertruck.JPG"))

img_list = [model_s, model_3, model_x, model_y, roadster, cybertruck ]

# insert image to screen
label = Label(image = img)
label.grid(row = 0, column = 0, columnspan = 3)

#buttons
back_button = Button(screen, text = "<<")






screen.mainloop()