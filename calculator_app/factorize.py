from tkinter import  *
from tkinter import messagebox
import math

root = Tk()
root.geometry("500x400")
root.title("Factorize")


def clear():
    # CLEAR PREVIOUS WIDGETS
    answer_title.grid_forget()
    answer_label.grid_forget()
    clear_button.grid_forget()

    # SHOW PREVIOUS WIDGETS
    a_entry.grid(row = 1, column = 0, padx = (60, 0))
    a_x_label.grid(row = 1, column = 1)
    x_power_entry.grid(row = 0, column = 1, pady = (120, 0), columnspan = 2, padx = (30, 0))
    a_operator_entry.grid(row = 1, column = 3)
    b_entry.grid(row = 1, column = 4)
    b_x_label.grid(row = 1, column = 5)
    b_operator_entry.grid(row = 1, column = 6)
    c_entry.grid(row = 1, column = 7)
    factorize_button.grid(row = 2, column = 0, columnspan = 8, pady = (40, 0), padx = (40, 0))

    # CLEAR ENTRYS
    a_entry.delete(0, END)
    x_power_entry.delete(0, END)
    a_operator_entry.delete(0, END)
    a_operator_entry.insert(0, "+")
    b_entry.delete(0, END)
    b_operator_entry.delete(0, END)
    b_operator_entry.insert(0, "+")
    c_entry.delete(0, END)

    



def factorize():
    # GET ENTRYS
    a = a_entry.get()
    x_power = x_power_entry.get()
    a_operator = a_operator_entry.get()

    b = b_entry.get()
    b_operator = b_operator_entry.get()

    c = c_entry.get()

    # CHECK EMPTY ENTRYS
    if a == "" :
        a = 1
    
    if x_power == "" :
        x_power = 1

    if b == "" :
        b = 1

    if c == "" :
        c = 1

    
    try :

        # CHECK IF ENTRYS ARE INTEGERS
        a = float(a)
        x_power = float(x_power)
        b = float(b)
        c = float(c)

        # + / -
        if a_operator == "+" :
            b = b
        else :

            if a_operator == "-" :
                b = -1 * b
            else :

                a = "error"
        
        
        if b_operator == "+" :
            c = c
        else :

            if b_operator == "-" :
                c = -1 * c
            else :

                a = "error"
        
        
        # CLEAR PREVIOUS WIDGETS
        a_entry.grid_forget()
        a_x_label.grid_forget()
        x_power_entry.grid_forget()
        a_operator_entry.grid_forget()
        b_entry.grid_forget()
        b_x_label.grid_forget()
        b_operator_entry.grid_forget()
        c_entry.grid_forget()
        factorize_button.grid_forget()

        
        # GET D
        d = b ** x_power 
        ac = 4 * a * c 
        d = d - ac

        # NEW VALUES
        neg_b = -1 * b 
        two_a = 2 * a   


        # GET ANSWER 
        global answer_title
        # ANSWER :
        answer_title = Label(root, text = "Answer :", font = ("Courier New", 40))
        answer_title.grid(row = 0, column = 0, pady = (70, 0))

        global answer_label
        global clear_button  
        if d < 0 :
            answer = "Cannot Factor"

            answer_label = Label(root, text = answer, font = ("Courier New", 40))
            answer_label.grid(row = 1, column = 0, columnspan = 2,pady = (50, 0), padx = (100, 0))
        else :

            if d == 0 :
                sqrt_d = math.sqrt(d)
                answer = neg_b + sqrt_d
                answer = answer / two_a
                answer = round(answer)

                answer_label = Label(root, text = "X = " + str(answer), font = ("Courier New", 40))
                answer_label.grid(row = 1, column = 1, pady = (50, 0))
                
            else :

                if d > 0 :
                    sqrt_d = math.sqrt(d)
                    answer_1 = neg_b + sqrt_d
                    answer_1 = answer_1 / two_a

                    answer_2 = neg_b - sqrt_d
                    answer_2 = answer_2 / two_a
                    
                    # TRY ANSWER
                    t_1 = a * (answer_1 ** x_power) + (b * answer_1) + c
                    t_2 = a * (answer_2 ** x_power) + (b * answer_2) + c

                    if t_1 == 0 :
                        answer = answer_1
                        answer = round(answer)
                    else :

                        if t_2 == 0 :
                            answer = answer_2
                            answer = round(answer)

                    answer_label = Label(root, text = "X = " + str(answer), font = ("Courier New", 40))
                    answer_label.grid(row = 1, column = 1, pady = (50, 0))

            
        clear_button = Button(root, text = "Clear", font = ("Courier New", 20), command = clear)
        clear_button.grid(row = 2, column = 1, pady = (140, 0))
                    
                    


    
    except :
        # ERROR MESSAGE BOX
        messagebox.showerror(" ERROR ", "INPUT MUST BE AN INTEGER \n or + / -")
    


            
        


    
    



# INPUT ENTRYS & LABELS
a_entry = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
a_entry.grid(row = 1, column = 0, padx = (60, 0))

a_x_label = Label(root, text = "X", font = ("Courier New", 40), justify = CENTER)
a_x_label.grid(row = 1, column = 1)

x_power_entry = Entry(root, width = 1, font = ("Courier New", 20), justify =  CENTER)
x_power_entry.grid(row = 0, column = 1, pady = (120, 0), columnspan = 2, padx = (30, 0))

a_operator_entry = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
a_operator_entry.insert(0, "+")
a_operator_entry.grid(row = 1, column = 3)

b_entry = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
b_entry.grid(row = 1, column = 4)

b_x_label = Label(root, text = "X", font = ("Courier New", 40), justify = CENTER)
b_x_label.grid(row = 1, column = 5)

b_operator_entry = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
b_operator_entry.insert(0, "+")
b_operator_entry.grid(row = 1, column = 6)

c_entry = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
c_entry.grid(row = 1, column = 7)


# FACTORIZE BUTTON
factorize_button = Button(root, text = "Factorize", font = ("Courier New", 40), command = factorize)
factorize_button.grid(row = 2, column = 0, columnspan = 8, pady = (40, 0), padx = (40, 0))




root.mainloop()