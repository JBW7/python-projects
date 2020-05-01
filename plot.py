from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

screen = Tk()
screen.geometry("400x200")


def graph():
	steak_prices = np.random.normal(200000, 25000, 5000)
	plt.hist(steak_prices, 200)
	plt.show()



button = Button(screen, height = 100, width = 100, command = graph)
button.pack()









screen.mainloop()