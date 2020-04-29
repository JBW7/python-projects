from tkinter import *
from random import randint

screen = Tk()
screen.title("RANDOM NAME GENERATOR")
screen.geometry("400x350")


title = Label(text = "RANDOM NAME GENERATOR", font = ("Helvetica", 24))
title.pack(pady = 10)


# def button function
def pick():
	entries = [
	"Liam", "Noah", "William",
	"James", "Logan", "Benjamin",
	"Mason", "Elijah", "Oliver",
	"Jacob", "Lucas", "Michael"
	"Alexander", "Ethan", "Daniel",
	"Matthew", "Aiden", "Henry",
	"Joseph", "Jackson", "Samuel",
	"Sebastian","David","Carter",
	"Wyatt","Jayden","John",
	"Owen", "Dylan", "Luke",
	"Gabriel", "Anthony", "Christopher",
	"Joshua", "Andrew", "Lincoln",
	"Mateo", "Ryan", "Jaxon",
	"Nathan", "Aaron", "Isaiah", 
	"Thomas", "Charles", "Caleb",
	"Josiah", "Christian", "Hunter",
	"Eli", "Jonathan", "Connor",
	"Landon", "Adrian", "Asher",
	"Cameron", "Leo", "Theodore",
	"Jeremiah", "Hudson", "Robert",
	"Easton", "Nolan", "Nicholas",
	"Ezra", "Colton", "Angel",
	"Brayden", "Jordan", "Dominic",
	"Austin", "Ian", "Adam",
	"Elias", "Jaxson", "Greyson",
	"Jose", "Ezekiel", "Carson",
	"Evan", "Maverick", "Bryson",
	"Jack", "Coope", "Xavier",
	"Parker", "Roman", "Jason",
	"Santiago", "Chase", "Sawyer",
	"Gavin", "Leonardo ", "Kayden"
]
	
	# REMOVE ANY DUPLICATES
	
	# convert to a set
	entries_set = set(entries)

	# convert back to lists 
	unique_entries = list(entries_set)

	# number of entries
	n_entries = len(unique_entries) -1


	# random number between 0-91
	random = randint(0, n_entries)
 
	# winner label

	winner_label = Label(screen, text = unique_entries[random], font = ("Helvetica", 24))
	winner_label.pack()



start_button = Button(screen, text = "START", font = ("Helvetica", 24), command = pick)
start_button.pack(pady = 10)






screen.mainloop()