# tutorial = https://www.youtube.com/watch?v=wb2yOsgEJJg

from tkinter import *

screen = Tk()
screen.geometry("2500x2500")

canvas = Canvas(screen, height = 2500, width = 2500, bg = "white")

line = canvas.create_line(10,10, 350,10, width = 5, fill = "black")

circle = canvas.create_oval(200,200, 300,300, fill = "red")

rectangle = canvas.create_rectangle(700,700, 1000,1000, fil = "yellow")

arc = canvas.create_arc(10,400, 200,600, extent = 90, fill = "orange" ) # extent = angle of sector

text = canvas.create_text(20, 30, anchor=W, font="Purisa", text="this is a text")



canvas.pack()

screen.mainloop()