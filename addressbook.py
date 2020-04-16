from tkinter import *
import sqlite3

screen = Tk()
screen.geometry("350x500")
screen.title("addresses")

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

# def save button
def save():
	# create a database/connect to one
    conn = sqlite3.connect("address_book.db")
	
	# create cursor
    c = conn.cursor()

    record_id = delete_box.get()


    c.execute("""UPDATE addresses SET
 		first_name = :first,
 		last_name = :last,
 		address = :address,
 		city = :city,
 		state = :state,
 		zipcode = :zipcode

 		WHERE oid = :oid""", 
 		{
 		"first" : f_name_editor.get(),
 		"last" : l_name_editor.get(),
 		"address" : address.get(),
 		"city" : city_editor.get(),
 		"state" : state_editor.get(),
 		"zipcode" : zipcode_editor.get(),
		"oid" : record_id
		})

	# commit changes
    conn.commit()

    # close connection
    conn.close()

    

# def update button
def update():
	editor = Tk()
	editor.geometry("350x200")
	editor.title("edit a record")


	# create a database/connect to one
	conn = sqlite3.connect("address_book.db")

    # create cursor
	c = conn.cursor()
    
	record_id = delete_box.get()
    #select data from database
	c.execute("SELECT * FROM addresses WHERE oid= " + record_id)
	records = c.fetchall()
	
	#create global variables for entrys
	global f_name_editor
	global l_name_editor
	global address_editor
	global city_editor
	global state_editor
	global zipcode_editor
	    


    # text box
	f_name_editor = Entry(editor, width= 30)
	f_name_editor.grid(row= 0, column= 1, padx= 20, pady=(10,0))

	l_name_editor = Entry(editor, width= 30)
	l_name_editor.grid(row= 1, column= 1)

	address_editor = Entry(editor, width= 30)
	address_editor.grid(row= 2, column= 1)

	city_editor = Entry(editor, width= 30)
	city_editor.grid(row= 3, column= 1)

	state_editor = Entry(editor, width= 30)
	state_editor.grid(row= 4, column= 1)

	zipcode_editor = Entry(editor, width= 30)
	zipcode_editor.grid(row= 5, column= 1)

	
	# text box label
	f_name_label = Label(editor, text = "First Name")
	f_name_label.grid(row= 0, column= 0, pady=(10,0))

	l_name_label = Label(editor, text = "Last Name")
	l_name_label.grid(row= 1, column= 0)

	address_label = Label(editor, text = "Address")
	address_label.grid(row= 2, column= 0)

	city_label = Label(editor, text = "City")
	city_label.grid(row= 3, column= 0)

	state_label = Label(editor, text = "State")
	state_label.grid(row= 4, column= 0)

	zipcode_label = Label(editor, text = "Zipcode")
	zipcode_label.grid(row= 5, column= 0)

	# put results in text boxes
	for record in records:
		f_name_editor.insert(0, record[0])
		l_name_editor.insert(0, record[1])
		address_editor.insert(0, record[2])
		city_editor.insert(0, record[3])
		state_editor.insert(0, record[4])
		zipcode_editor.insert(0, record[5])

	# save button
	save_button = Button(editor, text= "Save Record", command= save) 
	save_button.grid(row= 6, column= 0, columnspan= 2, padx= 10, pady= 10, ipadx= 125)



# delete a record
def delete():
	# create a database/connect to one
    conn = sqlite3.connect("address_book.db")

    # create cursor
    c = conn.cursor()
	
	#delete
    c.execute("DELETE FROM addresses WHERE oid= " + delete_box.get())

    # commit changes
    conn.commit()

    # close connection
    conn.close()


# def record button
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
    	print_records += str(record[0]) + " "  + str(record[1]) + " "  + "\t" + str(record[6]) + "\n"

    record_label = Label(screen, text = print_records)
    record_label.grid(row= 11, column= 0, columnspan= 2)
    # commit changes
    conn.commit()

    # close connection
    conn.close()




# text box
f_name = Entry(screen, width= 30)
f_name.grid(row= 0, column= 1, padx= 20, pady=(10,0))

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

delete_box = Entry(screen, width= 30)
delete_box.grid(row= 8, column= 1, pady=5)

# text box label
f_name_label = Label(screen, text = "First Name")
f_name_label.grid(row= 0, column= 0, pady=(10,0))

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

delete_label = Label(screen, text = "ID")
delete_label.grid(row= 8, column= 0, pady= 5)
# button
submit_button = Button(screen, text = "Add Data To Database", command = submit)
submit_button.grid(row= 6, column= 0, columnspan= 2, padx= 10, pady= 10, ipadx= 100)

# records button
record_button = Button(screen, text= "show records", command= records)
record_button.grid(row= 7, column= 0, columnspan= 2, padx= 10, pady= 10, ipadx= 125)

# button to delete records
delete_button = Button(screen, text= "delete record", command= delete)
delete_button.grid(row= 9, column= 0, columnspan= 2, padx= 10, pady= 10, ipadx= 125)

# update button
update_button = Button(screen, text= "edit record", command= update)
update_button.grid(row= 10, column= 0, columnspan= 2, padx= 10, pady= 10, ipadx= 125)


# commit changes
conn.commit()

# close connection
conn.close()

screen.mainloop()