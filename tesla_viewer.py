from tkinter import *
from PIL import ImageTk, Image

screen = Tk()
screen.geometry("750x750")
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
label = Label(image = model_s)
label.grid(row = 0, column = 0, columnspan = 3)

# def button
def back(image_number):
	global label
	global back_button
	global next_button

	label.grid_forget()
	label.grid_forget()
	label = Label(image = img_list[image_number - 1])
	next_button = Button(screen, text = ">>", command = lambda: next(image_number + 1))
	back_button = Button(screen, text = "<<", command = lambda: back(image_number - 1))

	if image_number == 1 :
		back_button = Button(screen, text = "<<", state = DISABLED)

	
	label.grid(row = 0, column = 0, columnspan = 3)
	back_button.grid(row = 1, column = 0)
	next_button.grid(row = 1, column = 2)

	# status bar
	status_bar = Label(screen, text = "Image "+ str(image_number) + " of " + str(len(img_list)), bd = 1, relief = SUNKEN, anchor = E)
	status_bar.grid(row = 2, column = 0, columnspan = 3, sticky = W + E)



def next(image_number):
	global label
	global back_button
	global next_button

	label.grid_forget()
	label = Label(image = img_list[image_number - 1])
	next_button = Button(screen, text = ">>", command = lambda: next(image_number + 1))
	back_button = Button(screen, text = "<<", command = lambda: back(image_number - 1))

	if image_number == 6 :
		next_button = Button(screen, text = ">>", state = DISABLED)

	label.grid(row = 0, column = 0, columnspan = 3)
	back_button.grid(row = 1, column = 0)
	next_button.grid(row = 1, column = 2)

	# status bar
	status_bar = Label(screen, text = "Image "+ str(image_number) + " of " + str(len(img_list)), bd = 1, relief = SUNKEN, anchor = E)
	status_bar.grid(row = 2, column = 0, columnspan = 3, sticky = W + E)



# status bar
status_bar = Label(screen, text = "Image 1 of " + str(len(img_list)), bd = 1, relief = SUNKEN, anchor = E)
status_bar.grid(row = 2, column = 0, columnspan = 3, sticky = W + E)



# buttons
back_button = Button(screen, text = "<<", command = back, state = DISABLED)
exit_button = Button(screen, text = "EXIT PROGRAM", command = screen.quit)
next_button = Button(screen, text = ">>", command = lambda: next(2))

back_button.grid(row = 1, column = 0)
exit_button.grid(row = 1, column = 1)
next_button.grid(row = 1, column = 2, pady = 10)







screen.mainloop()