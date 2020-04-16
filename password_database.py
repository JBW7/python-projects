from tkinter import *
import sqlite3

screen = Tk()
screen.geometry("325x150")
screen.title("passwords")

# create a database/connect to one
conn = sqlite3.connect("passwords.db")

# create cursor
c = conn.cursor()

# create table
'''
c.execute("""CREATE TABLE addresses (
		sign_in text,
		sign_up text,
		email text,
        facebook text, 
        instagram text,
        amazon text,
        goat text,
        stockx text
        )""")
'''
 
def sign_in():













# create/login to account
username_label = Label(screen, text = "Username : ")
username_label.grid(row = 0, column = 0, padx = 20, pady=(10,0))

username_entry = Entry(screen, width = 30)
username_entry.grid(row = 0, column = 1, pady=(10,0))

password_label = Label(screen, text = "Password : ")
password_label.grid(row = 1, column = 0)

password_entry = Entry(screen, width = 30)
password_entry.grid(row = 1, column = 1)

sign_in_button = Button(screen, text = "Sign in", height = 1, width = 5, command = sign_in)
sign_in_button.grid(row = 2, column = 0, pady = (25, 0), columnspan = 2)

sign_up_button = Button(screen, text = "Sign up", height = 1, width = 5, command = sign_up)
sign_up_button.grid(row = 3, column = 0, columnspan = 2)








screen.mainloop()