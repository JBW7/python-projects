from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry("460x400")
root.title("Compound Interest")


### PRINCIPLE AMOUNT
# LABEL
principle_amount_label = Label(root, text = "Principle Amount($)", font = ("Courier New", 20))
principle_amount_label.grid(row = 0, column = 0, pady = (30, 10), padx = (30, 10))

# ENTRY
principle_amount_entry = Entry(root, width = 6, font = ("Courier New", 20), borderwidth = 3, justify = CENTER)
principle_amount_entry.grid(row = 0, column = 1, pady = (30, 10), padx = (10, 0))

# CURRENCY LABEL
currency_label = Label(root, text = "USD", font = ("Courier New", 20))
currency_label.grid(row = 0, column = 2, pady = (30, 10))

### INTEREST RATE
# LABEL
interest_rate_label = Label(root, text = "Interest Rate(%)", font = ("Courier New", 20))
interest_rate_label.grid(row = 1, column = 0, pady = 10, padx = (30, 10), sticky = W)

# ENTRY
interest_rate_entry = Entry(root, width = 6, font = ("Courier New", 20), borderwidth = 3, justify = CENTER)
interest_rate_entry.grid(row = 1, column = 1, pady = 10, padx = (10, 0))

# UNITS
interest_rate_units = Label(root, text = "Anually", font = ("Courier New", 15))
interest_rate_units.grid(row = 1, column = 2, pady = 10)

### TOTAL TIME PERIOD
# LABEL
total_period_label = Label(root, text = "Total Period", font = ("Courier New", 20))
total_period_label.grid(row = 2, column = 0, pady = 10, padx = (30, 10), sticky = W)

# ENTRY
total_period_entry = Entry(root, width = 6, font = ("Courier New", 20), borderwidth = 3, justify = CENTER)
total_period_entry.grid(row = 2, column = 1, pady = 10, padx = (10, 0))

# OPTION MENU
def get_time_period_unit(event):
    global total_time_period_unit
    total_time_period_unit = unit_var.get()
    

unit_var = StringVar()
unit_var.set("Year(s)")
get_unit = OptionMenu(root, unit_var, "Year(s)", "Month(s)", command = get_time_period_unit)
get_unit.grid(row = 2, column = 2)


### COMPOUND PERIOD
def get_compound_period(event):
    global compound_period
    compound_period = period_var.get()


# LABEL
compound_period_label = Label(root, text = "Compound Period", font = ("Courier New", 20))
compound_period_label.grid(row = 3, column = 0, pady = 10, padx = (30, 0), sticky = W)

# OPTION MENU
period_var = StringVar()
period_var.set("Yearly")
get_period = OptionMenu(root, period_var, "Yearly", "Half Yearly", "Quarterly", "Monthly", command = get_compound_period)
get_period.config(width = 6)
get_period.grid(row = 3, column = 1, pady = 10, padx = (10, 0))


### TOTAL AMOUNT
# LABEL
total_amount_label = Label(root, text = " ", font = ("Courier New", 25))
total_amount_label.grid(row = 4, column = 0, padx = (30, 0), pady = 10, columnspan = 3)


### INTEREST AMOUNT
# LABEL
interest_amount_label = Label(root, text = " ", font = ("Courier New", 20))
interest_amount_label.grid(row = 5, column = 0, padx = (30, 0), pady = 10, columnspan = 3)



def clear():
    # CLEAR ALL ENTRYS
    principle_amount_entry.delete(0, END)
    interest_rate_entry.delete(0, END)
    total_period_entry.delete(0, END)

    
    # REMOVE ANSWER LABELS
    total_amount_label.grid_forget()
    interest_amount_label.grid_forget()

    
    # CALCULATE BUTTON
    calculate_button.grid(row = 4, column = 0, pady = 20, columnspan = 3)


    # CLEAR BUTTON
    clear_button.grid_forget()


def calculate():
    ### COLLECT DATA
    try :
        # GET PRINCIPAL AMOUNT
        principle_amount = int(principle_amount_entry.get())

        
        # GET INTEREST RATE 
        interest_rate = int(interest_rate_entry.get())

        
        # GET TOTAL PERIOD 
        total_period = int(total_period_entry.get())

        # GET COMPOUND PERIOD
        compound_period = period_var.get()

        # GET TOTAL TIME PERIOD
        total_time_period_unit = unit_var.get()
    
    except :
        # ERROR MESSAGE BOX
        messagebox.showerror(" ERROR ", "INPUT MUST BE A INTEGER / \n ENTRY CANT BE EMPTY")
        
        # CLEAR
        clear()

    # UNIT

    if total_time_period_unit == "Year(s)" :

        # GET TOTAL PERIOD
        if compound_period == "Yearly" :
            total_period = total_period
        else :

            if compound_period == "Half Yearly" :
                total_period = total_period * 2
                interest_rate = interest_rate / 2
            else :

                if compound_period == "Quarterly" :
                    total_period = total_period * 4
                    interest_rate = interest_rate / 4
                else :

                    if compound_period == "Monthly" :
                        total_period = total_period * 12
                        interest_rate = interest_rate / 12
    else :

        if total_time_period_unit == "Month(s)" :

            # GET COMPOUND PERIOD
            if compound_period == "Yearly" :
                total_period = total_period / 12
            else :

                if compound_period == "Half Yearly" :
                    total_period = total_period / 6
                else :

                    if compound_period == "Quarterly" :
                        total_period = total_period / 3
                    else :

                        if compound_period == "Monthly" :
                            total_period = total_period
    
                    

    ## ANSWER LABELS
    # LABEL
    global total_amount_label
    total_amount_label = Label(root, text = " ", font = ("Courier New", 25))
    total_amount_label.grid(row = 4, column = 0, padx = (30, 0), pady = 10, columnspan = 3)


    ### INTEREST AMOUNT
    # LABEL
    global interest_amount_label
    interest_amount_label = Label(root, text = " ", font = ("Courier New", 20))
    interest_amount_label.grid(row = 5, column = 0, padx = (30, 0), pady = 10, columnspan = 3)

    
    ### GET SIMPLE INTEREST
    # TOTAL AMOUNT
    total_amount = 1 + interest_rate/100
    total_amount = total_amount ** total_period
    total_amount = principle_amount * total_amount
    total_amount_text = float(total_amount)
    total_amount_text = '{:,.2f}'.format(total_amount_text)
    total_amount_text = str(total_amount_text)
    
    total_amount_label.config(text = "Total Amount = " + total_amount_text + " USD")


    # INTEREST AMOUNT
    
    interest_amount = int(total_amount) - principle_amount
    
    if interest_amount > 0 :
        interest_amount = interest_amount
    else :
        
        if interest_amount < 0 :
            interest_amount = -1 * interest_amount
        else :

            if interest_amount == 0 :
                interest_amount = 0


    interest_amount = float(interest_amount)
    interest_amount = '{:,.2f}'.format(interest_amount)
    interest_amount_text = str(interest_amount)

    interest_amount_label.config(text = "Interest Amount = " + interest_amount_text + " USD")

    
    # DELETE CALCULATE BUTTON
    calculate_button.grid_forget()


    # CLEAR BUTTON
    global clear_button
    clear_button = Button(root, text = "clear", font = ("Courier New", 15), command = clear)
    clear_button.grid(row = 6, column = 0, columnspan = 3, padx = (20, 0))


# CALCULATE BUTTON
calculate_button = Button(root, text = "Calculate", font = ("Courier New", 25), command = calculate)
calculate_button.grid(row = 4, column = 0, pady = 20, columnspan = 3)







root.mainloop()