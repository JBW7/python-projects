from tkinter import *
import sqlite3

screen = Tk()
screen.geometry("400x400")


# create a database/connect to one
conn = sqlite3.connect("address_book.db")

# create cursor
c = conn.cursor()

# create table
'''
c.execute("""CREATE TABLE addresses (
		first_name text,
        last_name text, 
        address text,
        city text,
        state text,
        zipcode integer
        )""")
'''
 
 # submit button
def submit():
    # create a database/connect to one
    conn = sqlite3.connect("address_book.db")

    # create cursor
    c = conn.cursor()
    
    # insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)", 
            {
                "f_name": f_name.get(),
                "l_name": l_name.get(),
                "address": address.get(),
                "city": city.get(),
                "state": state.get(),
                "zipcode": zipcode.get()
            })
   
    # commit changes
    conn.commit()

    # close connection
    conn.close()

    # clear text box
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# record button
def records():
	# create a database/connect to one
    conn = sqlite3.connect("address_book.db")

    # create cursor
    c = conn.cursor()
    
    #select data from database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print(records)

    # loop through results
    print_records = ""
    for  record in records:
    	print_records += str(record) + "\n"

    record_label = Label(screen, text = print_records)
    record_label.grid(row= 8, column= 0, columnspan= 2)
    # commit changes
    conn.commit()

    # close connection
    conn.close()

# text box
f_name = Entry(screen, width= 30)
f_name.grid(row= 0, column= 1, padx= 20)

l_name = Entry(screen, width= 30)
l_name.grid(row= 1, column= 1)

address = Entry(screen, width= 30)
address.grid(row= 2, column= 1)

city = Entry(screen, width= 30)
city.grid(row= 3, column= 1)

state = Entry(screen, width= 30)
state.grid(row= 4, column= 1)

zipcode = Entry(screen, width= 30)
zipcode.grid(row= 5, column= 1)

# text box label
f_name_label = Label(screen, text = "First Name")
f_name_label.grid(row= 0, column= 0)

l_name_label = Label(screen, text = "Last Name")
l_name_label.grid(row= 1, column= 0)

address_label = Label(screen, text = "Address")
address_label.grid(row= 2, column= 0)

city_label = Label(screen, text = "City")
city_label.grid(row= 3, column= 0)

state_label = Label(screen, text = "State")
state_label.grid(row= 4, column= 0)

zipcode_label = Label(screen, text = "Zipcode")
zipcode_label.grid(row= 5, column= 0)

#button
submit_button = Button(screen, text = "Add Data To Database", command = submit)
submit_button.grid(row= 6, column= 0, columnspan= 2, padx= 10, pady= 10, ipadx= 100)

#records button
record_button = Button(screen, text= "show records", command= records)
record_button.grid(row= 7, column= 0, columnspan= 2, padx= 10, pady= 10, ipadx= 125)
# commit changes
conn.commit()

# close connection
conn.close()

screen.mainloop()