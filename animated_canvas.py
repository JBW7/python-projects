from tkinter import *

root = Tk()
root.geometry("800x600")


w = 600
h = 400
x = w // 2
y = h // 2


canvas = Canvas(root, width = w, height = h, bg = "white")
canvas.pack(pady = 20)



'''
oval = canvas.create_oval(x, y, x + 50, y + 50)

# ARROW KEYS

def left(event):
    x = -10
    y = 0
    canvas.move(oval, x, y)

def right(event):
    x = 10
    y = 0
    canvas.move(oval, x, y)

def up(event):
    x = 0
    y = -10
    canvas.move(oval, x, y)

def down(event):
    x = 0
    y = 10
    canvas.move(oval, x, y)





# ARROW KEYS
root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)
'''



# MOUSE
img = PhotoImage(file = "/Users/jonathan/Desktop/python/python_pics/check.png")
image = canvas.create_image(200, 300, image = img) 


def move(event):
    global img
    img = PhotoImage(file = "/Users/jonathan/Desktop/python/python_pics/check.png")
    image = canvas.create_image(event.x, event.y, image = img) 









root.bind("<B1-Motion>", move)






root.mainloop()