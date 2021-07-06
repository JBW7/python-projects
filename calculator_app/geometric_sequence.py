from tkinter import *
import tensorflow as tf
import numpy as np
from tensorflow import keras
from PIL import ImageTk, Image
from tkinter import messagebox


root = Tk()
root.title("Geometric Sequence")
root.geometry("425x300")

### INTIAL VARIABLES 
# INITAL TERM STATUS
term_status = "fixed"

# INITIAL ENTRY DTYPE
entrys = "int"

# INITAL X ENTRYS
x1 = Entry(root)
x2 = Entry(root)
x3 = Entry(root)
x4 = Entry(root)
x5 = Entry(root)


# CLEAR ALL FUNCTION
def clear_all():
    if term_status == "custom" : 
        # DELETE ALL X ENTRYS
        x1.delete(0, END)
        x2.delete(0, END)
        x3.delete(0, END)
        x4.delete(0, END)
        x5.delete(0, END)

    # DELETE ALL Y ENTRYS
    y1.delete(0, END)
    y2.delete(0, END)
    y3.delete(0, END)
    y4.delete(0, END)
    y5.delete(0, END)

    # DELETE ANSWER LABEL
    answer_label.destroy()

    # DELETE CLEAR BUTTON
    clear_button.destroy()

    # SHOW TERM WIDGETS
    # SHOW TERM LABEL
    term_label.grid(row = 2, column = 0, columnspan = 3)

    # SHOW TERM ENTRY
    term_entry.grid(row = 2, column = 3)
    term_entry.delete(0, END)

    # SHOW SELECT BUTTON
    select_button.grid(row = 2, column = 4)



# FIND TERM FUNCTION
def find_term():
    ############################################################################## ML
    # SET UP ML
    model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

    model.compile(optimizer='sgd', loss='mean_squared_error')

    # CHECK IF ENTRYS ARE NOT A STR AND GET ENTRY VALUES
    try : 
        # GET ENTRYS FOR CUSTOM TERMS
        if term_status == "custom" : 
            xs = np.array([x1.get(), x2.get(), x3.get(), x4.get(), x5.get()], dtype=float)
            ys = np.array([y1.get(), y2.get(), y3.get(), y4.get(), y5.get()], dtype=float)
            
        # GET ENTRYS FOR FIXED TERMS
        if term_status == "fixed" : 
            xs = np.array([1.0, 2.0, 3.0, 4.0, 5.0], dtype=float)
            ys = np.array([y1.get(), y2.get(), y3.get(), y4.get(), y5.get()], dtype=float)

        # CHECK IF THE TERM ENTRY IS NOT A STR
        test_term = np.array([term_entry.get()], dtype = float)

        
    except :
        # ERROR MESSAGE BOX
        messagebox.showerror(" ERROR ", "INPUT MUST BE A INTEGER")
        
        # DELETE ENTRYS FOR CUSTOM TERMS
        if term_status == "custom" : 
            x1.delete(0, END)
            x2.delete(0, END)
            x3.delete(0, END)
            x4.delete(0, END)
            x5.delete(0, END)
            
            y1.delete(0, END)
            y2.delete(0, END)
            y3.delete(0, END)
            y4.delete(0, END)
            y5.delete(0, END)

            term_entry.delete(0, END)

        # DELETE ENTRYS FOR FIXED TERMS
        if term_status == "fixed" : 
            y1.delete(0, END)
            y2.delete(0, END)
            y3.delete(0, END)
            y4.delete(0, END)
            y5.delete(0, END)

            term_entry.delete(0, END)

    
    # SET UP ML EPOCH
    model.fit(xs, ys, epochs= 2000)

    ############################################################################## ML

    
    
    
    ############################################################################ ANS = 
    # GET ANS
    ans = model.predict([int(term_entry.get())])
    
    # ROUND ANS OR NOT
    if entrys == "int" : 
        # ROUND ANS
        ans = ans.round()

    else : 
        if entrys == "float" : 
            ans = ans
        
    # FORMAT ANS TO STR
    ans = str(ans)
    
    # REMOVE BRACKETS
    ans = ans.replace("[", "")
    ans = ans.replace("]", "")

    # REMOVE COMMA OR NOT
    if entrys == "int" : 
        ans = ans.replace(".", "")

    else:
        if entrys == "float" :
            ans = ans

    
    # TERM __
    # GET TERM ENTRYS AND CHANGE IT TO A STR
    term = str(term_entry.get())
    
    # REMOVE TERM WIDGETS
    # REMOVE TERM LABEL
    term_label.grid_forget()
    
    # TERM ENTRY
    term_entry.grid_forget()
    
    # REMOVE SELECT BUTTON
    select_button.grid_forget()
    
    
    # ANSWER LABEL
    global answer_label
    answer_label = Label(root, text = "Term" + " " + term + " " + "=" + " " + ans, font = ("Courier New", 40), anchor = CENTER)
    answer_label.grid(row = 2, column = 0, columnspan = 6)


    # CLEAR BUTTON
    global clear_button
    clear_button = Button(root, text = "CLEAR", font = ("Courier New", 20), command = clear_all)
    clear_button.grid(row = 3, column = 0, columnspan = 6)

    ############################################################################ ANS = 
    

# CLEAR X FUNCTION
def clear_x() :
    # DELETE ALL X ENTRYS
    x1.delete(0, END)
    x2.delete(0, END)
    x3.delete(0, END)
    x4.delete(0, END)
    x5.delete(0, END)

    # DELETE ANSWER LABEL
    answer_label.destroy()

    # SHOW TERM WIDGETS
    # SHOW TERM LABEL
    term_label.grid(row = 2, column = 0, columnspan = 3)

    # SHOW TERM ENTRY
    term_entry.grid(row = 2, column = 3)
    term_entry.delete(0, END)

    # SHOW SELECT BUTTON
    select_button.grid(row = 2, column = 4)
    

# CLEAR Y FUNCTION
def clear_y() :
    # DELETE ALL Y ENTRYS
    y1.delete(0, END)
    y2.delete(0, END)
    y3.delete(0, END)
    y4.delete(0, END)
    y5.delete(0, END)
    
    # DELETE ANSWER LABEL
    answer_label.destroy()

    # SHOW TERM WIDGETS
    # SHOW TERM LABEL
    term_label.grid(row = 2, column = 0, columnspan = 3)

    # SHOW TERM ENTRY
    term_entry.grid(row = 2, column = 3)
    term_entry.delete(0, END)

    # SHOW SELECT BUTTON
    select_button.grid(row = 2, column = 4)



########################################################################### NUMBER ENTRYS
# FIXED TERM FUCTION
def fixed_terms():
    ###### ROW 1 (X) LABELS
    x1 = Label(root, text = "1", font = ("Courier New", 40))
    x1.grid(row = 0, column = 0, pady = 20, padx = (35, 0))

    x2 = Label(root, text = "2", font = ("Courier New", 40))
    x2.grid(row = 0, column = 1, pady = 20)

    x3 = Label(root, text = "3", font = ("Courier New", 40))
    x3.grid(row = 0, column = 2, pady = 20)

    x4 = Label(root, text = "4", font = ("Courier New", 40))
    x4.grid(row = 0, column = 3, pady = 20)

    x5 = Label(root, text = "5", font = ("Courier New", 40))
    x5.grid(row = 0, column = 4, pady = 20)


    # TERM STATUS
    global term_status
    term_status = "fixed"


# CUSTOM TERM FUNCTON
def custom_terms():
    # GLOBAL VARIABLES
    global x1
    global x2
    global x3
    global x4
    global x5
    
    
    ###### ROW 1 (X) ENTRYS
    x1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
    x1.grid(row = 0, column = 0, pady = 20, padx = (35, 0))

    x2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
    x2.grid(row = 0, column = 1, pady = 20)

    x3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
    x3.grid(row = 0, column = 2, pady = 20)

    x4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
    x4.grid(row = 0, column = 3, pady = 20)

    x5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
    x5.grid(row = 0, column = 4, pady = 20)

    # DELETE ENTRYS X
    delete_x = Button(root, text = "CLEAR", command = clear_x)
    delete_x.grid(row = 0, column = 5)
    
    # TERM STATUS
    global term_status
    term_status = "custom"

    
    # CLEAR SCREEN
    # CLEAR Y ENTRYS
    y1.delete(0, END)
    y2.delete(0, END)
    y3.delete(0, END)
    y4.delete(0, END)
    y5.delete(0, END)
    
    # DELETE ANSWER LABEL
    answer_label.destroy()

    
    # SHOW TERM WIDGETS
    # SHOW TERM LABEL
    term_label.grid(row = 2, column = 0, columnspan = 3)

    # SHOW TERM ENTRY
    term_entry.grid(row = 2, column = 3)
    term_entry.delete(0, END)

    # SHOW SELECT BUTTON
    select_button.grid(row = 2, column = 4)


# CALL INITAL TERM STATUS
fixed_terms()

# DECIMAL ENTRYS FUNCTION
def decimal_entrys():
    global entrys
    entrys = "float"

# DECIMAL ENTRYS FUNCTION
def int_entrys():
    global entrys
    entrys = "int"



###### ROW 2 (Y)
y1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
y1.grid(row = 1, column = 0, pady = 20, padx = (35, 0))

y2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
y2.grid(row = 1, column = 1, pady = 20)

y3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
y3.grid(row = 1, column = 2, pady = 20)

y4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
y4.grid(row = 1, column = 3, pady = 20)

y5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
y5.grid(row = 1, column = 4, pady = 20)

# DELETE ENTRYS Y
delete_y = Button(root, text = "CLEAR", command = clear_y)
delete_y.grid(row = 1, column = 5)

############################################################################ NUMBER ENTRY




############################################################################ FIND TERM __
# TERM LABEL
term_label = Label(root, text = "Find Term: ", font = ("Courier New", 20))
term_label.grid(row = 2, column = 0, columnspan = 3)

# TERM ENTRY
term_entry = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
term_entry.grid(row = 2, column = 3)

# TERM BUTTON
# CHECK ICON

check_icon = ImageTk.PhotoImage(Image.open("/Users/jonathan/Desktop/python/python_pics/check.png"))


# BUTTON
select_button = Button(root, image = check_icon, command = find_term)
select_button.grid(row = 2, column = 4)

############################################################################ FIND TERM __




############################################################################ MENU BAR
# CREATE MENU BAR
menu_bar = Menu(root)
root.config(menu = menu_bar)

# ADD ITEMS TO MENU BAR
option_menu = Menu(menu_bar)
menu_bar.add_cascade(label = "option", menu = option_menu)

# ADD ITEMS TO OPTION MENU BAR
# CUSTOM TERMS
option_menu.add_command(label = "Custom Terms", command = custom_terms)

# FIXED TERMS
option_menu.add_command(label = "Fixed Terms", command = fixed_terms)

# DECIMAL VALUES
option_menu.add_command(label = "Decimal Values", command = decimal_entrys)

# INTEGER VALUES
option_menu.add_command(label = "Integer Values", command = int_entrys)

############################################################################ MENU BAR





root.mainloop()