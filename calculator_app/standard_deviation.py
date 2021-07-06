from tkinter import *
import numpy as np

root = Tk()
root.title("Standard Deviation")



# CREATE CANVAS
canvas = Canvas(root, height = 100, width = 200, bg = "white")
canvas.grid(row = 1, column = 0, columnspan = 5)




### INITIAL VARIABLES
# INITIAL ENTRY BOXES
e_1 = Entry(root)
e_2 = Entry(root)
e_3 = Entry(root)
e_4 = Entry(root)
e_5 = Entry(root)
e_6 = Entry(root)
e_7 = Entry(root)
e_8 = Entry(root)
e_9 = Entry(root)
e_10 = Entry(root)
e_11 = Entry(root)
e_12 = Entry(root)
e_13 = Entry(root)
e_14 = Entry(root)
e_15 = Entry(root)
e_16 = Entry(root)
e_17 = Entry(root)
e_18 = Entry(root)
e_19 = Entry(root)
e_20 = Entry(root)
e_21 = Entry(root)
e_22 = Entry(root)
e_23 = Entry(root)
e_24 = Entry(root)
e_25= Entry(root)
e_26 = Entry(root)
e_27 = Entry(root)
e_28 = Entry(root)
e_29 = Entry(root)
e_30 = Entry(root)
e_31 = Entry(root)
e_32 = Entry(root)
e_33 = Entry(root)
e_34 = Entry(root)
e_35 = Entry(root)
e_36 = Entry(root)
e_37 = Entry(root)
e_38 = Entry(root)
e_39 = Entry(root)
e_40 = Entry(root)

# INITIAL OPTION MENU VARIABLE
n_data_var = StringVar()

# INITIAL FIND STD BUTTON
find_std_button = Button(root)


# DELETE ALL ENTRY BOXES FUNCTION
def delete_entry_boxes():
    e_1.destroy()
    e_2.destroy()
    e_3.destroy()
    e_4.destroy()
    e_5.destroy()
    e_6.destroy()
    e_7.destroy()
    e_8.destroy()
    e_9.destroy()
    e_10.destroy()
    e_11.destroy()
    e_12.destroy()
    e_13.destroy()
    e_14.destroy()
    e_15.destroy()
    e_16.destroy()
    e_17.destroy()
    e_18.destroy()
    e_19.destroy()
    e_20.destroy()
    e_21.destroy()
    e_22.destroy()
    e_23.destroy()
    e_24.destroy()
    e_25.destroy()
    e_26.destroy()
    e_27.destroy()
    e_28.destroy()
    e_29.destroy()
    e_30.destroy()
    e_31.destroy()
    e_32.destroy()
    e_33.destroy()
    e_34.destroy()
    e_35.destroy()
    e_36.destroy()
    e_37.destroy()
    e_38.destroy()
    e_39.destroy()
    e_40.destroy()




# SHOW ENTRY BOXES
def get_n_data(event):
    ## GLOBAL VARIABLES
    # GLOBAL N ENTRY BOXES
    global n_data
    
    # GLOBAL ENTRY BOXES
    global e_1
    global e_2
    global e_3
    global e_4
    global e_5 
    global e_6
    global e_7
    global e_8
    global e_9
    global e_10
    global e_11
    global e_12
    global e_13
    global e_14
    global e_15
    global e_16
    global e_17
    global e_18
    global e_19
    global e_20
    global e_21
    global e_22
    global e_23
    global e_24
    global e_25
    global e_26
    global e_27
    global e_28
    global e_29
    global e_30
    global e_31
    global e_32
    global e_33
    global e_34
    global e_35
    global e_36
    global e_37
    global e_38
    global e_39
    global e_40

    
    # DELETE ALL ENTRY BOXES 
    delete_entry_boxes()
    
    # REMOVE CANVAS
    canvas.grid_forget()
    
    # GET N DATA
    n_data = n_data_var.get()

    n_data = int(n_data)
    
    # ENTRY BOXES
    if n_data == 1 :
        e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
        e_1.grid(row = 1, column = 2, pady = 30, padx = 60)
    else :

        if n_data == 2 :
            e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
            e_1.grid(row = 1, column = 1, pady = 30, padx = (30, 0))

            e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
            e_2.grid(row = 1, column = 2, pady = 30, padx = (0, 30))
        else :

            if n_data == 3 :
                e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                e_1.grid(row = 1, column = 1, pady = 30, padx = (30, 0))

                e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                e_2.grid(row = 1, column = 2, pady = 30)

                e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                e_3.grid(row = 1, column = 3, pady = 30, padx = (0, 30))
            else :

                if n_data == 4 :
                    e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_1.grid(row = 1, column = 0, pady = 30, padx = (30, 0))

                    e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_2.grid(row = 1, column = 1, pady = 30)

                    e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_3.grid(row = 1, column = 2, pady = 30)

                    e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_4.grid(row = 1, column = 3, pady = 30, padx = (0, 30))
                else :

                    if n_data == 5 :
                        e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_1.grid(row = 1, column = 0, pady = 30, padx = (30, 0))

                        e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_2.grid(row = 1, column = 1, pady = 30)

                        e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_3.grid(row = 1, column = 2, pady = 30)

                        e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_4.grid(row = 1, column = 3, pady = 30)

                        e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_5.grid(row = 1, column = 4, pady = 30, padx = (0, 30))
                    else :

                        if n_data == 6 :
                            e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                            e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_2.grid(row = 1, column = 1, pady = (30, 0))

                            e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_3.grid(row = 1, column = 2, pady = (30, 0), padx = (0, 30))

                            e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_4.grid(row = 2, column = 0, pady = (0, 30), padx = (30, 0))

                            e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_5.grid(row = 2, column = 1, pady = (0, 30))

                            e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_6.grid(row = 2, column = 2, pady = (0, 30), padx = (0, 30))
                        else :

                            if n_data == 7 :
                                e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                e_2.grid(row = 1, column = 1, pady = (30, 0))

                                e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                e_3.grid(row = 1, column = 2, pady = (30, 0))

                                e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                e_4.grid(row = 1, column = 3, pady = (30, 0), padx = (0, 30))

                                e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                e_5.grid(row = 2, column = 0, pady = (0, 30), padx = (30, 0))

                                e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                e_6.grid(row = 2, column = 1, pady = (0, 30))

                                e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                e_7.grid(row = 2, column = 2, pady = (0, 30))
                            else :

                                if n_data == 8 :
                                    e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                    e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                    e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                    e_2.grid(row = 1, column = 1, pady = (30, 0))

                                    e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                    e_3.grid(row = 1, column = 2, pady = (30, 0))

                                    e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                    e_4.grid(row = 1, column = 3, pady = (30, 0), padx = (0, 30))

                                    e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                    e_5.grid(row = 2, column = 0, pady = (0, 30), padx = (30, 0))

                                    e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                    e_6.grid(row = 2, column = 1, pady = (0, 30))

                                    e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                    e_7.grid(row = 2, column = 2, pady = (0, 30))
                                
                                    e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                    e_8.grid(row = 2, column = 3, pady = (0, 30), padx = (0, 30))
                                else :

                                    if n_data == 9 :
                                        e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                        e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                        e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                        e_2.grid(row = 1, column = 1, pady = (30, 0))

                                        e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                        e_3.grid(row = 1, column = 2, pady = (30, 0))

                                        e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                        e_4.grid(row = 1, column = 3, pady = (30, 0))

                                        e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                        e_5.grid(row = 1, column = 4, pady = (30, 0), padx = (0, 30))

                                        e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                        e_6.grid(row = 2, column = 0, pady = (0, 30), padx = (30, 0))

                                        e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                        e_7.grid(row = 2, column = 1, pady = (0, 30))

                                        e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                        e_8.grid(row = 2, column = 2, pady = (0, 30))
                                    
                                        e_9 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                        e_9.grid(row = 2, column = 3, pady = (0, 30))
                                    else :

                                        if n_data == 10 :
                                            e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                            e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                            e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                            e_2.grid(row = 1, column = 1, pady = (30, 0))

                                            e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                            e_3.grid(row = 1, column = 2, pady = (30, 0))

                                            e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                            e_4.grid(row = 1, column = 3, pady = (30, 0))

                                            e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                            e_5.grid(row = 1, column = 4, pady = (30, 0), padx = (0, 30))

                                            e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                            e_6.grid(row = 2, column = 0, pady = (0, 30), padx = (30, 0))

                                            e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                            e_7.grid(row = 2, column = 1, pady = (0, 30))

                                            e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                            e_8.grid(row = 2, column = 2, pady = (0, 30))
                                        
                                            e_9 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                            e_9.grid(row = 2, column = 3, pady = (0, 30))

                                            e_10 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                            e_10.grid(row = 2, column = 4, pady = (0, 30), padx = (0, 30))
                                        else :

                                            if n_data == 11 :
                                                e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                                e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                e_2.grid(row = 1, column = 1, pady = (30, 0))

                                                e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                e_3.grid(row = 1, column = 2, pady = (30, 0))

                                                e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                e_4.grid(row = 1, column = 3, pady = (30, 0), padx = (0, 30))

                                                e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                e_5.grid(row = 2, column = 0, padx = (30, 0))

                                                e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                e_6.grid(row = 2, column = 1)

                                                e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                e_7.grid(row = 2, column = 2)
                                            
                                                e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                e_8.grid(row = 2, column = 3, padx = (0, 30))

                                                e_9 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                e_9.grid(row = 3, column = 0, pady = (0, 30), padx = (30, 0))

                                                e_10 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                e_10.grid(row = 3, column = 1, pady = (0, 30))
                                            
                                                e_11 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                e_11.grid(row = 3, column = 2, pady = (0, 30))
                                            else :

                                                if n_data == 12 :
                                                    e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                    e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                                    e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                    e_2.grid(row = 1, column = 1, pady = (30, 0))

                                                    e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                    e_3.grid(row = 1, column = 2, pady = (30, 0))

                                                    e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                    e_4.grid(row = 1, column = 3, pady = (30, 0), padx = (0, 30))

                                                    e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                    e_5.grid(row = 2, column = 0, padx = (30, 0))

                                                    e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                    e_6.grid(row = 2, column = 1)

                                                    e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                    e_7.grid(row = 2, column = 2)
                                                
                                                    e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                    e_8.grid(row = 2, column = 3, padx = (0, 30))

                                                    e_9 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                    e_9.grid(row = 3, column = 0, pady = (0, 30), padx = (30, 0))

                                                    e_10 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                    e_10.grid(row = 3, column = 1, pady = (0, 30))
                                                
                                                    e_11 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                    e_11.grid(row = 3, column = 2, pady = (0, 30))

                                                    e_12 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                    e_12.grid(row = 3, column = 3, pady = (0, 30), padx = (0, 30))
                                                else :

                                                    if n_data == 13 :
                                                        e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                        e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                                        e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                        e_2.grid(row = 1, column = 1, pady = (30, 0))

                                                        e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                        e_3.grid(row = 1, column = 2, pady = (30, 0))

                                                        e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                        e_4.grid(row = 1, column = 3, pady = (30, 0))

                                                        e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                        e_5.grid(row = 1, column = 4, pady = (30, 0), padx = (0, 30))

                                                        e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                        e_6.grid(row = 2, column = 0, padx = (30, 0))

                                                        e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                        e_7.grid(row = 2, column = 1)

                                                        e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                        e_8.grid(row = 2, column = 2)
                                                    
                                                        e_9 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                        e_9.grid(row = 2, column = 3)

                                                        e_10 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                        e_10.grid(row = 2, column = 4, padx = (0, 30))

                                                        e_11 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                        e_11.grid(row = 3, column = 1, pady = (0, 30))
                                                    
                                                        e_12 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                        e_12.grid(row = 3, column = 2, pady = (0, 30))

                                                        e_13 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                        e_13.grid(row = 3, column = 3, pady = (0, 30))
                                                    else :

                                                        if n_data == 14 :
                                                            e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                            e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                                            e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                            e_2.grid(row = 1, column = 1, pady = (30, 0))

                                                            e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                            e_3.grid(row = 1, column = 2, pady = (30, 0))

                                                            e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                            e_4.grid(row = 1, column = 3, pady = (30, 0))

                                                            e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                            e_5.grid(row = 1, column = 4, pady = (30, 0), padx = (0, 30))

                                                            e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                            e_6.grid(row = 2, column = 0, padx = (30, 0))

                                                            e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                            e_7.grid(row = 2, column = 1)

                                                            e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                            e_8.grid(row = 2, column = 2)
                                                        
                                                            e_9 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                            e_9.grid(row = 2, column = 3)

                                                            e_10 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                            e_10.grid(row = 2, column = 4, padx = (0, 30))

                                                            e_11 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                            e_11.grid(row = 3, column = 0, pady = (0, 30), padx = (30, 0))
                                                        
                                                            e_12 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                            e_12.grid(row = 3, column = 1, pady = (0, 30))

                                                            e_13 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                            e_13.grid(row = 3, column = 2, pady = (0, 30))

                                                            e_14 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                            e_14.grid(row = 3, column = 3, pady = (0, 30))
                                                        else :

                                                            if n_data == 15 :
                                                                e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                                                e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                e_2.grid(row = 1, column = 1, pady = (30, 0))

                                                                e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                e_3.grid(row = 1, column = 2, pady = (30, 0))

                                                                e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                e_4.grid(row = 1, column = 3, pady = (30, 0))

                                                                e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                e_5.grid(row = 1, column = 4, pady = (30, 0), padx = (0, 30))

                                                                e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                e_6.grid(row = 2, column = 0, padx = (30, 0))

                                                                e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                e_7.grid(row = 2, column = 1)

                                                                e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                e_8.grid(row = 2, column = 2)
                                                            
                                                                e_9 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                e_9.grid(row = 2, column = 3)

                                                                e_10 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                e_10.grid(row = 2, column = 4, padx = (0, 30))

                                                                e_11 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                e_11.grid(row = 3, column = 0, pady = (0, 30), padx = (30, 0))
                                                            
                                                                e_12 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                e_12.grid(row = 3, column = 1, pady = (0, 30))

                                                                e_13 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                e_13.grid(row = 3, column = 2, pady = (0, 30))

                                                                e_14 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                e_14.grid(row = 3, column = 3, pady = (0, 30))

                                                                e_15 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                e_15.grid(row = 3, column = 4, pady = (0, 30), padx = (0, 30))
                                                            else :

                                                                if n_data == 16 :
                                                                    e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                    e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                                                    e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                    e_2.grid(row = 1, column = 1, pady = (30, 0))

                                                                    e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                    e_3.grid(row = 1, column = 2, pady = (30, 0))

                                                                    e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                    e_4.grid(row = 1, column = 3, pady = (30, 0), padx = (0, 30))

                                                                    e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                    e_5.grid(row = 2, column = 0, padx = (30, 0))

                                                                    e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                    e_6.grid(row = 2, column = 1)

                                                                    e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                    e_7.grid(row = 2, column = 2)
                                                                
                                                                    e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                    e_8.grid(row = 2, column = 3, padx = (0, 30))

                                                                    e_9 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                    e_9.grid(row = 3, column = 0, padx = (30, 0))

                                                                    e_10 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                    e_10.grid(row = 3, column = 1)
                                                                
                                                                    e_11 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                    e_11.grid(row = 3, column = 2)

                                                                    e_12 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                    e_12.grid(row = 3, column = 3, padx = (0, 30))

                                                                    e_13 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                    e_13.grid(row = 4, column = 0, pady = (0, 30), padx = (30, 0))

                                                                    e_14 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                    e_14.grid(row = 4, column = 1, pady = (0, 30))
                                                                
                                                                    e_15 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                    e_15.grid(row = 4, column = 2, pady = (0, 30))

                                                                    e_16 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                    e_16.grid(row = 4, column = 3, pady = (0, 30), padx = (0, 30))
                                                                else :

                                                                    if n_data == 17 :
                                                                        e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                        e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                                                        e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                        e_2.grid(row = 1, column = 1, pady = (30, 0))

                                                                        e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                        e_3.grid(row = 1, column = 2, pady = (30, 0))

                                                                        e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                        e_4.grid(row = 1, column = 3, pady = (30, 0))

                                                                        e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                        e_5.grid(row = 1, column = 4, pady = (30, 0), padx = (0, 30))

                                                                        e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                        e_6.grid(row = 2, column = 0, padx = (30, 0))

                                                                        e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                        e_7.grid(row = 2, column = 1)

                                                                        e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                        e_8.grid(row = 2, column = 2)
                                                                    
                                                                        e_9 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                        e_9.grid(row = 2, column = 3)

                                                                        e_10 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                        e_10.grid(row = 2, column = 4, padx = (0, 30))

                                                                        e_11 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                        e_11.grid(row = 3, column = 0, padx = (30, 0))
                                                                    
                                                                        e_12 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                        e_12.grid(row = 3, column = 1)

                                                                        e_13 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                        e_13.grid(row = 3, column = 2)

                                                                        e_14 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                        e_14.grid(row = 3, column = 3)

                                                                        e_15 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                        e_15.grid(row = 3, column = 4, padx = (0, 30))

                                                                        e_16 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                        e_16.grid(row = 4, column = 1, pady = (0, 30))

                                                                        e_17 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                        e_17.grid(row = 4, column = 3, pady = (0, 30))
                                                                    else :

                                                                        if n_data == 18 :
                                                                            e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                            e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                                                            e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                            e_2.grid(row = 1, column = 1, pady = (30, 0))

                                                                            e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                            e_3.grid(row = 1, column = 2, pady = (30, 0))

                                                                            e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                            e_4.grid(row = 1, column = 3, pady = (30, 0))

                                                                            e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                            e_5.grid(row = 1, column = 4, pady = (30, 0), padx = (0, 30))

                                                                            e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                            e_6.grid(row = 2, column = 0, padx = (30, 0))

                                                                            e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                            e_7.grid(row = 2, column = 1)

                                                                            e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                            e_8.grid(row = 2, column = 2)
                                                                        
                                                                            e_9 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                            e_9.grid(row = 2, column = 3)

                                                                            e_10 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                            e_10.grid(row = 2, column = 4, padx = (0, 30))

                                                                            e_11 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                            e_11.grid(row = 3, column = 0, padx = (30, 0))
                                                                        
                                                                            e_12 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                            e_12.grid(row = 3, column = 1)

                                                                            e_13 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                            e_13.grid(row = 3, column = 2)

                                                                            e_14 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                            e_14.grid(row = 3, column = 3)

                                                                            e_15 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                            e_15.grid(row = 3, column = 4, padx = (0, 30))

                                                                            e_16 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                            e_16.grid(row = 4, column = 1, pady = (0, 30))

                                                                            e_17 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                            e_17.grid(row = 4, column = 2, pady = (0, 30))

                                                                            e_18 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                            e_18.grid(row = 4, column = 3, pady = (0, 30))
                                                                        else :

                                                                            if n_data == 19 :
                                                                                e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                                                                e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                e_2.grid(row = 1, column = 1, pady = (30, 0))

                                                                                e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                e_3.grid(row = 1, column = 2, pady = (30, 0))

                                                                                e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                e_4.grid(row = 1, column = 3, pady = (30, 0))

                                                                                e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                e_5.grid(row = 1, column = 4, pady = (30, 0), padx = (0, 30))

                                                                                e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                e_6.grid(row = 2, column = 0, padx = (30, 0))

                                                                                e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                e_7.grid(row = 2, column = 1)

                                                                                e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                e_8.grid(row = 2, column = 2)
                                                                            
                                                                                e_9 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                e_9.grid(row = 2, column = 3)

                                                                                e_10 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                e_10.grid(row = 2, column = 4, padx = (0, 30))

                                                                                e_11 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                e_11.grid(row = 3, column = 0, padx = (30, 0))
                                                                            
                                                                                e_12 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                e_12.grid(row = 3, column = 1)

                                                                                e_13 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                e_13.grid(row = 3, column = 2)

                                                                                e_14 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                e_14.grid(row = 3, column = 3)

                                                                                e_15 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                e_15.grid(row = 3, column = 4, padx = (0, 30))

                                                                                e_16 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                e_16.grid(row = 4, column = 0, pady = (0, 30), padx = (30, 0))

                                                                                e_17 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                e_17.grid(row = 4, column = 1, pady = (0, 30))

                                                                                e_18 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                e_18.grid(row = 4, column = 2, pady = (0, 30))

                                                                                e_19 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                e_19.grid(row = 4, column = 3, pady = (0, 30))
                                                                            else :

                                                                                if n_data == 20 :
                                                                                    e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                    e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                                                                    e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                    e_2.grid(row = 1, column = 1, pady = (30, 0))

                                                                                    e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                    e_3.grid(row = 1, column = 2, pady = (30, 0))

                                                                                    e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                    e_4.grid(row = 1, column = 3, pady = (30, 0))

                                                                                    e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                    e_5.grid(row = 1, column = 4, pady = (30, 0), padx = (0, 30))

                                                                                    e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                    e_6.grid(row = 2, column = 0, padx = (30, 0))

                                                                                    e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                    e_7.grid(row = 2, column = 1)

                                                                                    e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                    e_8.grid(row = 2, column = 2)
                                                                                
                                                                                    e_9 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                    e_9.grid(row = 2, column = 3)

                                                                                    e_10 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                    e_10.grid(row = 2, column = 4, padx = (0, 30))

                                                                                    e_11 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                    e_11.grid(row = 3, column = 0, padx = (30, 0))
                                                                                
                                                                                    e_12 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                    e_12.grid(row = 3, column = 1)

                                                                                    e_13 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                    e_13.grid(row = 3, column = 2)

                                                                                    e_14 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                    e_14.grid(row = 3, column = 3)

                                                                                    e_15 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                    e_15.grid(row = 3, column = 4, padx = (0, 30))

                                                                                    e_16 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                    e_16.grid(row = 4, column = 0, pady = (0, 30), padx = (30, 0))

                                                                                    e_17 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                    e_17.grid(row = 4, column = 1, pady = (0, 30))

                                                                                    e_18 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                    e_18.grid(row = 4, column = 2, pady = (0, 30))

                                                                                    e_19 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                    e_19.grid(row = 4, column = 3, pady = (0, 30))

                                                                                    e_20 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                    e_20.grid(row = 4, column = 4, pady = (0, 30), padx = (0, 30))
                                                                                else :

                                                                                    if n_data == 21 :
                                                                                        e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                        e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                                                                        e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                        e_2.grid(row = 1, column = 1, pady = (30, 0))

                                                                                        e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                        e_3.grid(row = 1, column = 2, pady = (30, 0))

                                                                                        e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                        e_4.grid(row = 1, column = 3, pady = (30, 0))

                                                                                        e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                        e_5.grid(row = 1, column = 4, pady = (30, 0), padx = (0, 30))

                                                                                        e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                        e_6.grid(row = 2, column = 0, padx = (30, 0))

                                                                                        e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                        e_7.grid(row = 2, column = 1)

                                                                                        e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                        e_8.grid(row = 2, column = 2)
                                                                                    
                                                                                        e_9 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                        e_9.grid(row = 2, column = 3)

                                                                                        e_10 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                        e_10.grid(row = 2, column = 4, padx = (0, 30))

                                                                                        e_11 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                        e_11.grid(row = 3, column = 0, padx = (30, 0))
                                                                                    
                                                                                        e_12 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                        e_12.grid(row = 3, column = 1)

                                                                                        e_13 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                        e_13.grid(row = 3, column = 2)

                                                                                        e_14 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                        e_14.grid(row = 3, column = 3)

                                                                                        e_15 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                        e_15.grid(row = 3, column = 4, padx = (0, 30))

                                                                                        e_16 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                        e_16.grid(row = 4, column = 0, padx = (30, 0))

                                                                                        e_17 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                        e_17.grid(row = 4, column = 1)

                                                                                        e_18 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                        e_18.grid(row = 4, column = 2)

                                                                                        e_19 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                        e_19.grid(row = 4, column = 3)

                                                                                        e_20 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                        e_20.grid(row = 4, column = 4, padx = (0, 30))

                                                                                        e_21 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                        e_21.grid(row = 5, column = 2, pady = (0, 30))
                                                                                    else :

                                                                                        if n_data == 22 :
                                                                                            e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                            e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                                                                            e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                            e_2.grid(row = 1, column = 1, pady = (30, 0))

                                                                                            e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                            e_3.grid(row = 1, column = 2, pady = (30, 0))

                                                                                            e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                            e_4.grid(row = 1, column = 3, pady = (30, 0))

                                                                                            e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                            e_5.grid(row = 1, column = 4, pady = (30, 0), padx = (0, 30))

                                                                                            e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                            e_6.grid(row = 2, column = 0, padx = (30, 0))

                                                                                            e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                            e_7.grid(row = 2, column = 1)

                                                                                            e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                            e_8.grid(row = 2, column = 2)
                                                                                        
                                                                                            e_9 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                            e_9.grid(row = 2, column = 3)

                                                                                            e_10 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                            e_10.grid(row = 2, column = 4, padx = (0, 30))

                                                                                            e_11 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                            e_11.grid(row = 3, column = 0, padx = (30, 0))
                                                                                        
                                                                                            e_12 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                            e_12.grid(row = 3, column = 1)

                                                                                            e_13 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                            e_13.grid(row = 3, column = 2)

                                                                                            e_14 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                            e_14.grid(row = 3, column = 3)

                                                                                            e_15 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                            e_15.grid(row = 3, column = 4, padx = (0, 30))

                                                                                            e_16 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                            e_16.grid(row = 4, column = 0, padx = (30, 0))

                                                                                            e_17 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                            e_17.grid(row = 4, column = 1)

                                                                                            e_18 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                            e_18.grid(row = 4, column = 2)

                                                                                            e_19 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                            e_19.grid(row = 4, column = 3)

                                                                                            e_20 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                            e_20.grid(row = 4, column = 4, padx = (0, 30))

                                                                                            e_21 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                            e_21.grid(row = 5, column = 1, pady = (0, 30))

                                                                                            e_22 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                            e_22.grid(row = 5, column = 3, pady = (0, 30))
                                                                                        else :

                                                                                            if n_data == 23 :
                                                                                                e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                                                                                e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                e_2.grid(row = 1, column = 1, pady = (30, 0))

                                                                                                e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                e_3.grid(row = 1, column = 2, pady = (30, 0))

                                                                                                e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                e_4.grid(row = 1, column = 3, pady = (30, 0))

                                                                                                e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                e_5.grid(row = 1, column = 4, pady = (30, 0), padx = (0, 30))

                                                                                                e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                e_6.grid(row = 2, column = 0, padx = (30, 0))

                                                                                                e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                e_7.grid(row = 2, column = 1)

                                                                                                e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                e_8.grid(row = 2, column = 2)
                                                                                            
                                                                                                e_9 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                e_9.grid(row = 2, column = 3)

                                                                                                e_10 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                e_10.grid(row = 2, column = 4, padx = (0, 30))

                                                                                                e_11 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                e_11.grid(row = 3, column = 0, padx = (30, 0))
                                                                                            
                                                                                                e_12 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                e_12.grid(row = 3, column = 1)

                                                                                                e_13 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                e_13.grid(row = 3, column = 2)

                                                                                                e_14 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                e_14.grid(row = 3, column = 3)

                                                                                                e_15 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                e_15.grid(row = 3, column = 4, padx = (0, 30))

                                                                                                e_16 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                e_16.grid(row = 4, column = 0, padx = (30, 0))

                                                                                                e_17 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                e_17.grid(row = 4, column = 1)

                                                                                                e_18 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                e_18.grid(row = 4, column = 2)

                                                                                                e_19 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                e_19.grid(row = 4, column = 3)

                                                                                                e_20 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                e_20.grid(row = 4, column = 4, padx = (0, 30))

                                                                                                e_21 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                e_21.grid(row = 5, column = 1, pady = (0, 30))

                                                                                                e_22 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                e_22.grid(row = 5, column = 2, pady = (0, 30))

                                                                                                e_23 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                e_23.grid(row = 5, column = 3, pady = (0, 30))
                                                                                            else :

                                                                                                if n_data == 24 :
                                                                                                    e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                    e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                                                                                    e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                    e_2.grid(row = 1, column = 1, pady = (30, 0))

                                                                                                    e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                    e_3.grid(row = 1, column = 2, pady = (30, 0))

                                                                                                    e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                    e_4.grid(row = 1, column = 3, pady = (30, 0))

                                                                                                    e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                    e_5.grid(row = 1, column = 4, pady = (30, 0), padx = (0, 30))

                                                                                                    e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                    e_6.grid(row = 2, column = 0, padx = (30, 0))

                                                                                                    e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                    e_7.grid(row = 2, column = 1)

                                                                                                    e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                    e_8.grid(row = 2, column = 2)
                                                                                                
                                                                                                    e_9 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                    e_9.grid(row = 2, column = 3)

                                                                                                    e_10 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                    e_10.grid(row = 2, column = 4, padx = (0, 30))

                                                                                                    e_11 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                    e_11.grid(row = 3, column = 0, padx = (30, 0))
                                                                                                
                                                                                                    e_12 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                    e_12.grid(row = 3, column = 1)

                                                                                                    e_13 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                    e_13.grid(row = 3, column = 2)

                                                                                                    e_14 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                    e_14.grid(row = 3, column = 3)

                                                                                                    e_15 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                    e_15.grid(row = 3, column = 4, padx = (0, 30))

                                                                                                    e_16 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                    e_16.grid(row = 4, column = 0, padx = (30, 0))

                                                                                                    e_17 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                    e_17.grid(row = 4, column = 1)

                                                                                                    e_18 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                    e_18.grid(row = 4, column = 2)

                                                                                                    e_19 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                    e_19.grid(row = 4, column = 3)

                                                                                                    e_20 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                    e_20.grid(row = 4, column = 4, padx = (0, 30))

                                                                                                    e_21 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                    e_21.grid(row = 5, column = 0, pady = (0, 30), padx = (30, 0))

                                                                                                    e_22 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                    e_22.grid(row = 5, column = 1, pady = (0, 30))

                                                                                                    e_23 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                    e_23.grid(row = 5, column = 2, pady = (0, 30))

                                                                                                    e_24 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                    e_24.grid(row = 5, column = 3, pady = (0, 30))
                                                                                                else :

                                                                                                    if n_data == 25 :
                                                                                                        e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                        e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                                                                                        e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                        e_2.grid(row = 1, column = 1, pady = (30, 0))

                                                                                                        e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                        e_3.grid(row = 1, column = 2, pady = (30, 0))

                                                                                                        e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                        e_4.grid(row = 1, column = 3, pady = (30, 0))

                                                                                                        e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                        e_5.grid(row = 1, column = 4, pady = (30, 0), padx = (0, 30))

                                                                                                        e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                        e_6.grid(row = 2, column = 0, padx = (30, 0))

                                                                                                        e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                        e_7.grid(row = 2, column = 1)

                                                                                                        e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                        e_8.grid(row = 2, column = 2)
                                                                                                    
                                                                                                        e_9 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                        e_9.grid(row = 2, column = 3)

                                                                                                        e_10 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                        e_10.grid(row = 2, column = 4, padx = (0, 30))

                                                                                                        e_11 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                        e_11.grid(row = 3, column = 0, padx = (30, 0))
                                                                                                    
                                                                                                        e_12 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                        e_12.grid(row = 3, column = 1)

                                                                                                        e_13 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                        e_13.grid(row = 3, column = 2)

                                                                                                        e_14 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                        e_14.grid(row = 3, column = 3)

                                                                                                        e_15 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                        e_15.grid(row = 3, column = 4, padx = (0, 30))

                                                                                                        e_16 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                        e_16.grid(row = 4, column = 0, padx = (30, 0))

                                                                                                        e_17 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                        e_17.grid(row = 4, column = 1)

                                                                                                        e_18 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                        e_18.grid(row = 4, column = 2)

                                                                                                        e_19 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                        e_19.grid(row = 4, column = 3)

                                                                                                        e_20 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                        e_20.grid(row = 4, column = 4, padx = (0, 30))

                                                                                                        e_21 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                        e_21.grid(row = 5, column = 0, pady = (0, 30), padx = (30, 0))

                                                                                                        e_22 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                        e_22.grid(row = 5, column = 1, pady = (0, 30))

                                                                                                        e_23 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                        e_23.grid(row = 5, column = 2, pady = (0, 30))

                                                                                                        e_24 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                        e_24.grid(row = 5, column = 3, pady = (0, 30))

                                                                                                        e_25 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                        e_25.grid(row = 5, column = 4, pady = (0, 30), padx = (0, 30))
                                                                                                    else :

                                                                                                        if n_data == 26 :
                                                                                                            e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                            e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                                                                                            e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                            e_2.grid(row = 1, column = 1, pady = (30, 0))

                                                                                                            e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                            e_3.grid(row = 1, column = 2, pady = (30, 0))

                                                                                                            e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                            e_4.grid(row = 1, column = 3, pady = (30, 0))

                                                                                                            e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                            e_5.grid(row = 1, column = 4, pady = (30, 0), padx = (0, 30))

                                                                                                            e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                            e_6.grid(row = 2, column = 0, padx = (30, 0))

                                                                                                            e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                            e_7.grid(row = 2, column = 1)

                                                                                                            e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                            e_8.grid(row = 2, column = 2)
                                                                                                        
                                                                                                            e_9 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                            e_9.grid(row = 2, column = 3)

                                                                                                            e_10 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                            e_10.grid(row = 2, column = 4, padx = (0, 30))

                                                                                                            e_11 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                            e_11.grid(row = 3, column = 0, padx = (30, 0))
                                                                                                        
                                                                                                            e_12 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                            e_12.grid(row = 3, column = 1)

                                                                                                            e_13 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                            e_13.grid(row = 3, column = 2)

                                                                                                            e_14 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                            e_14.grid(row = 3, column = 3)

                                                                                                            e_15 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                            e_15.grid(row = 3, column = 4, padx = (0, 30))

                                                                                                            e_16 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                            e_16.grid(row = 4, column = 0, padx = (30, 0))

                                                                                                            e_17 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                            e_17.grid(row = 4, column = 1)

                                                                                                            e_18 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                            e_18.grid(row = 4, column = 2)

                                                                                                            e_19 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                            e_19.grid(row = 4, column = 3)

                                                                                                            e_20 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                            e_20.grid(row = 4, column = 4, padx = (0, 30))

                                                                                                            e_21 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                            e_21.grid(row = 5, column = 0, padx = (30, 0))

                                                                                                            e_22 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                            e_22.grid(row = 5, column = 1)

                                                                                                            e_23 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                            e_23.grid(row = 5, column = 2)

                                                                                                            e_24 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                            e_24.grid(row = 5, column = 3)

                                                                                                            e_25 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                            e_25.grid(row = 5, column = 4, padx = (0, 30))

                                                                                                            e_26 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                            e_26.grid(row = 6, column = 2, pady = (0, 30))
                                                                                                        else :

                                                                                                            if n_data == 27 :
                                                                                                                e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                                                                                                e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                e_2.grid(row = 1, column = 1, pady = (30, 0))

                                                                                                                e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                e_3.grid(row = 1, column = 2, pady = (30, 0))

                                                                                                                e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                e_4.grid(row = 1, column = 3, pady = (30, 0))

                                                                                                                e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                e_5.grid(row = 1, column = 4, pady = (30, 0), padx = (0, 30))

                                                                                                                e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                e_6.grid(row = 2, column = 0, padx = (30, 0))

                                                                                                                e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                e_7.grid(row = 2, column = 1)

                                                                                                                e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                e_8.grid(row = 2, column = 2)
                                                                                                            
                                                                                                                e_9 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                e_9.grid(row = 2, column = 3)

                                                                                                                e_10 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                e_10.grid(row = 2, column = 4, padx = (0, 30))

                                                                                                                e_11 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                e_11.grid(row = 3, column = 0, padx = (30, 0))
                                                                                                            
                                                                                                                e_12 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                e_12.grid(row = 3, column = 1)

                                                                                                                e_13 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                e_13.grid(row = 3, column = 2)

                                                                                                                e_14 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                e_14.grid(row = 3, column = 3)

                                                                                                                e_15 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                e_15.grid(row = 3, column = 4, padx = (0, 30))

                                                                                                                e_16 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                e_16.grid(row = 4, column = 0, padx = (30, 0))

                                                                                                                e_17 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                e_17.grid(row = 4, column = 1)

                                                                                                                e_18 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                e_18.grid(row = 4, column = 2)

                                                                                                                e_19 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                e_19.grid(row = 4, column = 3)

                                                                                                                e_20 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                e_20.grid(row = 4, column = 4, padx = (0, 30))

                                                                                                                e_21 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                e_21.grid(row = 5, column = 0, padx = (30, 0))

                                                                                                                e_22 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                e_22.grid(row = 5, column = 1)

                                                                                                                e_23 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                e_23.grid(row = 5, column = 2)

                                                                                                                e_24 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                e_24.grid(row = 5, column = 3)

                                                                                                                e_25 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                e_25.grid(row = 5, column = 4, padx = (0, 30))

                                                                                                                e_26 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                e_26.grid(row = 6, column = 1, pady = (0, 30))

                                                                                                                e_27 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                e_27.grid(row = 6, column = 3, pady = (0, 30))
                                                                                                            else :

                                                                                                                if n_data == 28 :
                                                                                                                    e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                    e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                                                                                                    e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                    e_2.grid(row = 1, column = 1, pady = (30, 0))

                                                                                                                    e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                    e_3.grid(row = 1, column = 2, pady = (30, 0))

                                                                                                                    e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                    e_4.grid(row = 1, column = 3, pady = (30, 0))

                                                                                                                    e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                    e_5.grid(row = 1, column = 4, pady = (30, 0), padx = (0, 30))

                                                                                                                    e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                    e_6.grid(row = 2, column = 0, padx = (30, 0))

                                                                                                                    e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                    e_7.grid(row = 2, column = 1)

                                                                                                                    e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                    e_8.grid(row = 2, column = 2)
                                                                                                                
                                                                                                                    e_9 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                    e_9.grid(row = 2, column = 3)

                                                                                                                    e_10 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                    e_10.grid(row = 2, column = 4, padx = (0, 30))

                                                                                                                    e_11 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                    e_11.grid(row = 3, column = 0, padx = (30, 0))
                                                                                                                
                                                                                                                    e_12 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                    e_12.grid(row = 3, column = 1)

                                                                                                                    e_13 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                    e_13.grid(row = 3, column = 2)

                                                                                                                    e_14 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                    e_14.grid(row = 3, column = 3)

                                                                                                                    e_15 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                    e_15.grid(row = 3, column = 4, padx = (0, 30))

                                                                                                                    e_16 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                    e_16.grid(row = 4, column = 0, padx = (30, 0))

                                                                                                                    e_17 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                    e_17.grid(row = 4, column = 1)

                                                                                                                    e_18 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                    e_18.grid(row = 4, column = 2)

                                                                                                                    e_19 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                    e_19.grid(row = 4, column = 3)

                                                                                                                    e_20 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                    e_20.grid(row = 4, column = 4, padx = (0, 30))

                                                                                                                    e_21 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                    e_21.grid(row = 5, column = 0, padx = (30, 0))

                                                                                                                    e_22 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                    e_22.grid(row = 5, column = 1)

                                                                                                                    e_23 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                    e_23.grid(row = 5, column = 2)

                                                                                                                    e_24 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                    e_24.grid(row = 5, column = 3)

                                                                                                                    e_25 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                    e_25.grid(row = 5, column = 4, padx = (0, 30))

                                                                                                                    e_26 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                    e_26.grid(row = 6, column = 1, pady = (0, 30))

                                                                                                                    e_27 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                    e_27.grid(row = 6, column = 2, pady = (0, 30))

                                                                                                                    e_28 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                    e_28.grid(row = 6, column = 3, pady = (0, 30))
                                                                                                                else :

                                                                                                                    if n_data == 29 :
                                                                                                                        e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                        e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                                                                                                        e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                        e_2.grid(row = 1, column = 1, pady = (30, 0))

                                                                                                                        e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                        e_3.grid(row = 1, column = 2, pady = (30, 0))

                                                                                                                        e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                        e_4.grid(row = 1, column = 3, pady = (30, 0))

                                                                                                                        e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                        e_5.grid(row = 1, column = 4, pady = (30, 0), padx = (0, 30))

                                                                                                                        e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                        e_6.grid(row = 2, column = 0, padx = (30, 0))

                                                                                                                        e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                        e_7.grid(row = 2, column = 1)

                                                                                                                        e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                        e_8.grid(row = 2, column = 2)
                                                                                                                    
                                                                                                                        e_9 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                        e_9.grid(row = 2, column = 3)

                                                                                                                        e_10 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                        e_10.grid(row = 2, column = 4, padx = (0, 30))

                                                                                                                        e_11 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                        e_11.grid(row = 3, column = 0, padx = (30, 0))
                                                                                                                    
                                                                                                                        e_12 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                        e_12.grid(row = 3, column = 1)

                                                                                                                        e_13 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                        e_13.grid(row = 3, column = 2)

                                                                                                                        e_14 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                        e_14.grid(row = 3, column = 3)

                                                                                                                        e_15 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                        e_15.grid(row = 3, column = 4, padx = (0, 30))

                                                                                                                        e_16 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                        e_16.grid(row = 4, column = 0, padx = (30, 0))

                                                                                                                        e_17 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                        e_17.grid(row = 4, column = 1)

                                                                                                                        e_18 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                        e_18.grid(row = 4, column = 2)

                                                                                                                        e_19 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                        e_19.grid(row = 4, column = 3)

                                                                                                                        e_20 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                        e_20.grid(row = 4, column = 4, padx = (0, 30))

                                                                                                                        e_21 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                        e_21.grid(row = 5, column = 0, padx = (30, 0))

                                                                                                                        e_22 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                        e_22.grid(row = 5, column = 1)

                                                                                                                        e_23 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                        e_23.grid(row = 5, column = 2)

                                                                                                                        e_24 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                        e_24.grid(row = 5, column = 3)

                                                                                                                        e_25 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                        e_25.grid(row = 5, column = 4, padx = (0, 30))

                                                                                                                        e_26 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                        e_26.grid(row = 6, column = 0, pady = (0, 30), padx = (30, 0))

                                                                                                                        e_27 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                        e_27.grid(row = 6, column = 1, pady = (0, 30))

                                                                                                                        e_28 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                        e_28.grid(row = 6, column = 2, pady = (0, 30))

                                                                                                                        e_29 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                        e_29.grid(row = 6, column = 3, pady = (0, 30))
                                                                                                                    else :

                                                                                                                        if n_data == 30 :
                                                                                                                            e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                            e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                                                                                                            e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                            e_2.grid(row = 1, column = 1, pady = (30, 0))

                                                                                                                            e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                            e_3.grid(row = 1, column = 2, pady = (30, 0))

                                                                                                                            e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                            e_4.grid(row = 1, column = 3, pady = (30, 0))

                                                                                                                            e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                            e_5.grid(row = 1, column = 4, pady = (30, 0), padx = (0, 30))

                                                                                                                            e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                            e_6.grid(row = 2, column = 0, padx = (30, 0))

                                                                                                                            e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                            e_7.grid(row = 2, column = 1)

                                                                                                                            e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                            e_8.grid(row = 2, column = 2)
                                                                                                                        
                                                                                                                            e_9 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                            e_9.grid(row = 2, column = 3)

                                                                                                                            e_10 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                            e_10.grid(row = 2, column = 4, padx = (0, 30))

                                                                                                                            e_11 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                            e_11.grid(row = 3, column = 0, padx = (30, 0))
                                                                                                                        
                                                                                                                            e_12 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                            e_12.grid(row = 3, column = 1)

                                                                                                                            e_13 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                            e_13.grid(row = 3, column = 2)

                                                                                                                            e_14 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                            e_14.grid(row = 3, column = 3)

                                                                                                                            e_15 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                            e_15.grid(row = 3, column = 4, padx = (0, 30))

                                                                                                                            e_16 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                            e_16.grid(row = 4, column = 0, padx = (30, 0))

                                                                                                                            e_17 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                            e_17.grid(row = 4, column = 1)

                                                                                                                            e_18 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                            e_18.grid(row = 4, column = 2)

                                                                                                                            e_19 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                            e_19.grid(row = 4, column = 3)

                                                                                                                            e_20 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                            e_20.grid(row = 4, column = 4, padx = (0, 30))

                                                                                                                            e_21 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                            e_21.grid(row = 5, column = 0, padx = (30, 0))

                                                                                                                            e_22 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                            e_22.grid(row = 5, column = 1)

                                                                                                                            e_23 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                            e_23.grid(row = 5, column = 2)

                                                                                                                            e_24 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                            e_24.grid(row = 5, column = 3)

                                                                                                                            e_25 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                            e_25.grid(row = 5, column = 4, padx = (0, 30))

                                                                                                                            e_26 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                            e_26.grid(row = 6, column = 0, pady = (0, 30), padx = (30, 0))

                                                                                                                            e_27 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                            e_27.grid(row = 6, column = 1, pady = (0, 30))

                                                                                                                            e_28 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                            e_28.grid(row = 6, column = 2, pady = (0, 30))

                                                                                                                            e_29 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                            e_29.grid(row = 6, column = 3, pady = (0, 30))

                                                                                                                            e_30 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                            e_30.grid(row = 6, column = 4, pady = (0, 30), padx = (0, 30))
                                                                                                                        else :

                                                                                                                            if n_data == 31 :
                                                                                                                                e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                                                                                                                e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                e_2.grid(row = 1, column = 1, pady = (30, 0))

                                                                                                                                e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                e_3.grid(row = 1, column = 2, pady = (30, 0))

                                                                                                                                e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                e_4.grid(row = 1, column = 3, pady = (30, 0))

                                                                                                                                e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                e_5.grid(row = 1, column = 4, pady = (30, 0), padx = (0, 30))

                                                                                                                                e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                e_6.grid(row = 2, column = 0, padx = (30, 0))

                                                                                                                                e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                e_7.grid(row = 2, column = 1)

                                                                                                                                e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                e_8.grid(row = 2, column = 2)
                                                                                                                            
                                                                                                                                e_9 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                e_9.grid(row = 2, column = 3)

                                                                                                                                e_10 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                e_10.grid(row = 2, column = 4, padx = (0, 30))

                                                                                                                                e_11 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                e_11.grid(row = 3, column = 0, padx = (30, 0))
                                                                                                                            
                                                                                                                                e_12 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                e_12.grid(row = 3, column = 1)

                                                                                                                                e_13 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                e_13.grid(row = 3, column = 2)

                                                                                                                                e_14 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                e_14.grid(row = 3, column = 3)

                                                                                                                                e_15 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                e_15.grid(row = 3, column = 4, padx = (0, 30))

                                                                                                                                e_16 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                e_16.grid(row = 4, column = 0, padx = (30, 0))

                                                                                                                                e_17 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                e_17.grid(row = 4, column = 1)

                                                                                                                                e_18 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                e_18.grid(row = 4, column = 2)

                                                                                                                                e_19 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                e_19.grid(row = 4, column = 3)

                                                                                                                                e_20 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                e_20.grid(row = 4, column = 4, padx = (0, 30))

                                                                                                                                e_21 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                e_21.grid(row = 5, column = 0, padx = (30, 0))

                                                                                                                                e_22 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                e_22.grid(row = 5, column = 1)

                                                                                                                                e_23 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                e_23.grid(row = 5, column = 2)

                                                                                                                                e_24 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                e_24.grid(row = 5, column = 3)

                                                                                                                                e_25 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                e_25.grid(row = 5, column = 4, padx = (0, 30))

                                                                                                                                e_26 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                e_26.grid(row = 6, column = 0, padx = (30, 0))

                                                                                                                                e_27 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                e_27.grid(row = 6, column = 1)

                                                                                                                                e_28 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                e_28.grid(row = 6, column = 2)

                                                                                                                                e_29 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                e_29.grid(row = 6, column = 3)

                                                                                                                                e_30 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                e_30.grid(row = 6, column = 4, padx = (0, 30))

                                                                                                                                e_31 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                e_31.grid(row = 7, column = 2, pady = (0, 30))
                                                                                                                            else :

                                                                                                                                if n_data == 32 :
                                                                                                                                    e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                    e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                                                                                                                    e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                    e_2.grid(row = 1, column = 1, pady = (30, 0))

                                                                                                                                    e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                    e_3.grid(row = 1, column = 2, pady = (30, 0))

                                                                                                                                    e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                    e_4.grid(row = 1, column = 3, pady = (30, 0))

                                                                                                                                    e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                    e_5.grid(row = 1, column = 4, pady = (30, 0), padx = (0, 30))

                                                                                                                                    e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                    e_6.grid(row = 2, column = 0, padx = (30, 0))

                                                                                                                                    e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                    e_7.grid(row = 2, column = 1)

                                                                                                                                    e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                    e_8.grid(row = 2, column = 2)
                                                                                                                                
                                                                                                                                    e_9 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                    e_9.grid(row = 2, column = 3)

                                                                                                                                    e_10 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                    e_10.grid(row = 2, column = 4, padx = (0, 30))

                                                                                                                                    e_11 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                    e_11.grid(row = 3, column = 0, padx = (30, 0))
                                                                                                                                
                                                                                                                                    e_12 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                    e_12.grid(row = 3, column = 1)

                                                                                                                                    e_13 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                    e_13.grid(row = 3, column = 2)

                                                                                                                                    e_14 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                    e_14.grid(row = 3, column = 3)

                                                                                                                                    e_15 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                    e_15.grid(row = 3, column = 4, padx = (0, 30))

                                                                                                                                    e_16 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                    e_16.grid(row = 4, column = 0, padx = (30, 0))

                                                                                                                                    e_17 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                    e_17.grid(row = 4, column = 1)

                                                                                                                                    e_18 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                    e_18.grid(row = 4, column = 2)

                                                                                                                                    e_19 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                    e_19.grid(row = 4, column = 3)

                                                                                                                                    e_20 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                    e_20.grid(row = 4, column = 4, padx = (0, 30))

                                                                                                                                    e_21 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                    e_21.grid(row = 5, column = 0, padx = (30, 0))

                                                                                                                                    e_22 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                    e_22.grid(row = 5, column = 1)

                                                                                                                                    e_23 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                    e_23.grid(row = 5, column = 2)

                                                                                                                                    e_24 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                    e_24.grid(row = 5, column = 3)

                                                                                                                                    e_25 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                    e_25.grid(row = 5, column = 4, padx = (0, 30))

                                                                                                                                    e_26 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                    e_26.grid(row = 6, column = 0, padx = (30, 0))

                                                                                                                                    e_27 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                    e_27.grid(row = 6, column = 1)

                                                                                                                                    e_28 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                    e_28.grid(row = 6, column = 2)

                                                                                                                                    e_29 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                    e_29.grid(row = 6, column = 3)

                                                                                                                                    e_30 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                    e_30.grid(row = 6, column = 4, padx = (0, 30))

                                                                                                                                    e_31 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                    e_31.grid(row = 7, column = 1, pady = (0, 30))

                                                                                                                                    e_32 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                    e_32.grid(row = 7, column = 3, pady = (0, 30))
                                                                                                                                else :

                                                                                                                                    if n_data == 33 :
                                                                                                                                        e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                                                                                                                        e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_2.grid(row = 1, column = 1, pady = (30, 0))

                                                                                                                                        e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_3.grid(row = 1, column = 2, pady = (30, 0))

                                                                                                                                        e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_4.grid(row = 1, column = 3, pady = (30, 0))

                                                                                                                                        e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_5.grid(row = 1, column = 4, pady = (30, 0), padx = (0, 30))

                                                                                                                                        e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_6.grid(row = 2, column = 0, padx = (30, 0))

                                                                                                                                        e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_7.grid(row = 2, column = 1)

                                                                                                                                        e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_8.grid(row = 2, column = 2)
                                                                                                                                    
                                                                                                                                        e_9 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_9.grid(row = 2, column = 3)

                                                                                                                                        e_10 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_10.grid(row = 2, column = 4, padx = (0, 30))

                                                                                                                                        e_11 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_11.grid(row = 3, column = 0, padx = (30, 0))
                                                                                                                                    
                                                                                                                                        e_12 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_12.grid(row = 3, column = 1)

                                                                                                                                        e_13 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_13.grid(row = 3, column = 2)

                                                                                                                                        e_14 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_14.grid(row = 3, column = 3)

                                                                                                                                        e_15 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_15.grid(row = 3, column = 4, padx = (0, 30))

                                                                                                                                        e_16 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_16.grid(row = 4, column = 0, padx = (30, 0))

                                                                                                                                        e_17 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_17.grid(row = 4, column = 1)

                                                                                                                                        e_18 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_18.grid(row = 4, column = 2)

                                                                                                                                        e_19 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_19.grid(row = 4, column = 3)

                                                                                                                                        e_20 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_20.grid(row = 4, column = 4, padx = (0, 30))

                                                                                                                                        e_21 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_21.grid(row = 5, column = 0, padx = (30, 0))

                                                                                                                                        e_22 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_22.grid(row = 5, column = 1)

                                                                                                                                        e_23 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_23.grid(row = 5, column = 2)

                                                                                                                                        e_24 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_24.grid(row = 5, column = 3)

                                                                                                                                        e_25 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_25.grid(row = 5, column = 4, padx = (0, 30))

                                                                                                                                        e_26 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_26.grid(row = 6, column = 0, padx = (30, 0))

                                                                                                                                        e_27 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_27.grid(row = 6, column = 1)

                                                                                                                                        e_28 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_28.grid(row = 6, column = 2)

                                                                                                                                        e_29 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_29.grid(row = 6, column = 3)

                                                                                                                                        e_30 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_30.grid(row = 6, column = 4, padx = (0, 30))

                                                                                                                                        e_31 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_31.grid(row = 7, column = 1, pady = (0, 30))

                                                                                                                                        e_32 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_32.grid(row = 7, column = 2, pady = (0, 30))

                                                                                                                                        e_33 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                        e_33.grid(row = 7, column = 3, pady = (0, 30))
                                                                                                                                    else :

                                                                                                                                        if n_data == 34 :
                                                                                                                                            e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                                                                                                                            e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_2.grid(row = 1, column = 1, pady = (30, 0))

                                                                                                                                            e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_3.grid(row = 1, column = 2, pady = (30, 0))

                                                                                                                                            e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_4.grid(row = 1, column = 3, pady = (30, 0))

                                                                                                                                            e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_5.grid(row = 1, column = 4, pady = (30, 0), padx = (0, 30))

                                                                                                                                            e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_6.grid(row = 2, column = 0, padx = (30, 0))

                                                                                                                                            e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_7.grid(row = 2, column = 1)

                                                                                                                                            e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_8.grid(row = 2, column = 2)
                                                                                                                                        
                                                                                                                                            e_9 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_9.grid(row = 2, column = 3)

                                                                                                                                            e_10 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_10.grid(row = 2, column = 4, padx = (0, 30))

                                                                                                                                            e_11 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_11.grid(row = 3, column = 0, padx = (30, 0))
                                                                                                                                        
                                                                                                                                            e_12 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_12.grid(row = 3, column = 1)

                                                                                                                                            e_13 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_13.grid(row = 3, column = 2)

                                                                                                                                            e_14 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_14.grid(row = 3, column = 3)

                                                                                                                                            e_15 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_15.grid(row = 3, column = 4, padx = (0, 30))

                                                                                                                                            e_16 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_16.grid(row = 4, column = 0, padx = (30, 0))

                                                                                                                                            e_17 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_17.grid(row = 4, column = 1)

                                                                                                                                            e_18 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_18.grid(row = 4, column = 2)

                                                                                                                                            e_19 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_19.grid(row = 4, column = 3)

                                                                                                                                            e_20 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_20.grid(row = 4, column = 4, padx = (0, 30))

                                                                                                                                            e_21 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_21.grid(row = 5, column = 0, padx = (30, 0))

                                                                                                                                            e_22 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_22.grid(row = 5, column = 1)

                                                                                                                                            e_23 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_23.grid(row = 5, column = 2)

                                                                                                                                            e_24 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_24.grid(row = 5, column = 3)

                                                                                                                                            e_25 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_25.grid(row = 5, column = 4, padx = (0, 30))

                                                                                                                                            e_26 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_26.grid(row = 6, column = 0, padx = (30, 0))

                                                                                                                                            e_27 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_27.grid(row = 6, column = 1)

                                                                                                                                            e_28 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_28.grid(row = 6, column = 2)

                                                                                                                                            e_29 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_29.grid(row = 6, column = 3)

                                                                                                                                            e_30 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_30.grid(row = 6, column = 4, padx = (0, 30))

                                                                                                                                            e_31 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_31.grid(row = 7, column = 0, pady = (0, 30), padx = (30, 0))

                                                                                                                                            e_32 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_32.grid(row = 7, column = 1, pady = (0, 30))

                                                                                                                                            e_33 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_33.grid(row = 7, column = 2, pady = (0, 30))    

                                                                                                                                            e_34 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                            e_34.grid(row = 7, column = 3, pady = (0, 30))       
                                                                                                                                        else :

                                                                                                                                            if n_data == 35 :
                                                                                                                                                e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                                                                                                                                e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_2.grid(row = 1, column = 1, pady = (30, 0))

                                                                                                                                                e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_3.grid(row = 1, column = 2, pady = (30, 0))

                                                                                                                                                e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_4.grid(row = 1, column = 3, pady = (30, 0))

                                                                                                                                                e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_5.grid(row = 1, column = 4, pady = (30, 0), padx = (0, 30))

                                                                                                                                                e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_6.grid(row = 2, column = 0, padx = (30, 0))

                                                                                                                                                e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_7.grid(row = 2, column = 1)

                                                                                                                                                e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_8.grid(row = 2, column = 2)
                                                                                                                                            
                                                                                                                                                e_9 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_9.grid(row = 2, column = 3)

                                                                                                                                                e_10 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_10.grid(row = 2, column = 4, padx = (0, 30))

                                                                                                                                                e_11 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_11.grid(row = 3, column = 0, padx = (30, 0))
                                                                                                                                            
                                                                                                                                                e_12 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_12.grid(row = 3, column = 1)

                                                                                                                                                e_13 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_13.grid(row = 3, column = 2)

                                                                                                                                                e_14 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_14.grid(row = 3, column = 3)

                                                                                                                                                e_15 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_15.grid(row = 3, column = 4, padx = (0, 30))

                                                                                                                                                e_16 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_16.grid(row = 4, column = 0, padx = (30, 0))

                                                                                                                                                e_17 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_17.grid(row = 4, column = 1)

                                                                                                                                                e_18 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_18.grid(row = 4, column = 2)

                                                                                                                                                e_19 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_19.grid(row = 4, column = 3)

                                                                                                                                                e_20 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_20.grid(row = 4, column = 4, padx = (0, 30))

                                                                                                                                                e_21 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_21.grid(row = 5, column = 0, padx = (30, 0))

                                                                                                                                                e_22 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_22.grid(row = 5, column = 1)

                                                                                                                                                e_23 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_23.grid(row = 5, column = 2)

                                                                                                                                                e_24 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_24.grid(row = 5, column = 3)

                                                                                                                                                e_25 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_25.grid(row = 5, column = 4, padx = (0, 30))

                                                                                                                                                e_26 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_26.grid(row = 6, column = 0, padx = (30, 0))

                                                                                                                                                e_27 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_27.grid(row = 6, column = 1)

                                                                                                                                                e_28 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_28.grid(row = 6, column = 2)

                                                                                                                                                e_29 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_29.grid(row = 6, column = 3)

                                                                                                                                                e_30 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_30.grid(row = 6, column = 4, padx = (0, 30))

                                                                                                                                                e_31 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_31.grid(row = 7, column = 0, pady = (0, 30), padx = (30, 0))

                                                                                                                                                e_32 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_32.grid(row = 7, column = 1, pady = (0, 30))

                                                                                                                                                e_33 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_33.grid(row = 7, column = 2, pady = (0, 30))    

                                                                                                                                                e_34 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_34.grid(row = 7, column = 3, pady = (0, 30)) 

                                                                                                                                                e_35 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                e_35.grid(row = 7, column = 4, pady = (0, 30), padx = (0, 30))   
                                                                                                                                            else :

                                                                                                                                                if n_data == 36 :
                                                                                                                                                    e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                                                                                                                                    e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_2.grid(row = 1, column = 1, pady = (30, 0))

                                                                                                                                                    e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_3.grid(row = 1, column = 2, pady = (30, 0))

                                                                                                                                                    e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_4.grid(row = 1, column = 3, pady = (30, 0))

                                                                                                                                                    e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_5.grid(row = 1, column = 4, pady = (30, 0), padx = (0, 30))

                                                                                                                                                    e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_6.grid(row = 2, column = 0, padx = (30, 0))

                                                                                                                                                    e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_7.grid(row = 2, column = 1)

                                                                                                                                                    e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_8.grid(row = 2, column = 2)
                                                                                                                                                
                                                                                                                                                    e_9 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_9.grid(row = 2, column = 3)

                                                                                                                                                    e_10 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_10.grid(row = 2, column = 4, padx = (0, 30))

                                                                                                                                                    e_11 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_11.grid(row = 3, column = 0, padx = (30, 0))
                                                                                                                                                
                                                                                                                                                    e_12 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_12.grid(row = 3, column = 1)

                                                                                                                                                    e_13 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_13.grid(row = 3, column = 2)

                                                                                                                                                    e_14 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_14.grid(row = 3, column = 3)

                                                                                                                                                    e_15 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_15.grid(row = 3, column = 4, padx = (0, 30))

                                                                                                                                                    e_16 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_16.grid(row = 4, column = 0, padx = (30, 0))

                                                                                                                                                    e_17 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_17.grid(row = 4, column = 1)

                                                                                                                                                    e_18 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_18.grid(row = 4, column = 2)

                                                                                                                                                    e_19 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_19.grid(row = 4, column = 3)

                                                                                                                                                    e_20 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_20.grid(row = 4, column = 4, padx = (0, 30))

                                                                                                                                                    e_21 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_21.grid(row = 5, column = 0, padx = (30, 0))

                                                                                                                                                    e_22 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_22.grid(row = 5, column = 1)

                                                                                                                                                    e_23 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_23.grid(row = 5, column = 2)

                                                                                                                                                    e_24 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_24.grid(row = 5, column = 3)

                                                                                                                                                    e_25 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_25.grid(row = 5, column = 4, padx = (0, 30))

                                                                                                                                                    e_26 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_26.grid(row = 6, column = 0, padx = (30, 0))

                                                                                                                                                    e_27 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_27.grid(row = 6, column = 1)

                                                                                                                                                    e_28 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_28.grid(row = 6, column = 2)

                                                                                                                                                    e_29 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_29.grid(row = 6, column = 3)

                                                                                                                                                    e_30 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_30.grid(row = 6, column = 4, padx = (0, 30))

                                                                                                                                                    e_31 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_31.grid(row = 7, column = 0, padx = (30, 0))

                                                                                                                                                    e_32 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_32.grid(row = 7, column = 1)

                                                                                                                                                    e_33 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_33.grid(row = 7, column = 2)    

                                                                                                                                                    e_34 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_34.grid(row = 7, column = 3) 

                                                                                                                                                    e_35 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_35.grid(row = 7, column = 4, padx = (0, 30)) 

                                                                                                                                                    e_36 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                    e_36.grid(row = 8, column = 2, pady = (0, 30))
                                                                                                                                                else :

                                                                                                                                                    if n_data == 37 :
                                                                                                                                                        e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                                                                                                                                        e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_2.grid(row = 1, column = 1, pady = (30, 0))

                                                                                                                                                        e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_3.grid(row = 1, column = 2, pady = (30, 0))

                                                                                                                                                        e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_4.grid(row = 1, column = 3, pady = (30, 0))

                                                                                                                                                        e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_5.grid(row = 1, column = 4, pady = (30, 0), padx = (0, 30))

                                                                                                                                                        e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_6.grid(row = 2, column = 0, padx = (30, 0))

                                                                                                                                                        e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_7.grid(row = 2, column = 1)

                                                                                                                                                        e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_8.grid(row = 2, column = 2)
                                                                                                                                                    
                                                                                                                                                        e_9 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_9.grid(row = 2, column = 3)

                                                                                                                                                        e_10 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_10.grid(row = 2, column = 4, padx = (0, 30))

                                                                                                                                                        e_11 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_11.grid(row = 3, column = 0, padx = (30, 0))
                                                                                                                                                    
                                                                                                                                                        e_12 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_12.grid(row = 3, column = 1)

                                                                                                                                                        e_13 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_13.grid(row = 3, column = 2)

                                                                                                                                                        e_14 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_14.grid(row = 3, column = 3)

                                                                                                                                                        e_15 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_15.grid(row = 3, column = 4, padx = (0, 30))

                                                                                                                                                        e_16 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_16.grid(row = 4, column = 0, padx = (30, 0))

                                                                                                                                                        e_17 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_17.grid(row = 4, column = 1)

                                                                                                                                                        e_18 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_18.grid(row = 4, column = 2)

                                                                                                                                                        e_19 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_19.grid(row = 4, column = 3)

                                                                                                                                                        e_20 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_20.grid(row = 4, column = 4, padx = (0, 30))

                                                                                                                                                        e_21 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_21.grid(row = 5, column = 0, padx = (30, 0))

                                                                                                                                                        e_22 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_22.grid(row = 5, column = 1)

                                                                                                                                                        e_23 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_23.grid(row = 5, column = 2)

                                                                                                                                                        e_24 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_24.grid(row = 5, column = 3)

                                                                                                                                                        e_25 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_25.grid(row = 5, column = 4, padx = (0, 30))

                                                                                                                                                        e_26 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_26.grid(row = 6, column = 0, padx = (30, 0))

                                                                                                                                                        e_27 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_27.grid(row = 6, column = 1)

                                                                                                                                                        e_28 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_28.grid(row = 6, column = 2)

                                                                                                                                                        e_29 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_29.grid(row = 6, column = 3)

                                                                                                                                                        e_30 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_30.grid(row = 6, column = 4, padx = (0, 30))

                                                                                                                                                        e_31 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_31.grid(row = 7, column = 0, padx = (30, 0))

                                                                                                                                                        e_32 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_32.grid(row = 7, column = 1)

                                                                                                                                                        e_33 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_33.grid(row = 7, column = 2)    

                                                                                                                                                        e_34 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_34.grid(row = 7, column = 3) 

                                                                                                                                                        e_35 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_35.grid(row = 7, column = 4, padx = (0, 30)) 

                                                                                                                                                        e_36 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_36.grid(row = 8, column = 1, pady = (0, 30))  

                                                                                                                                                        e_37 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                        e_37.grid(row = 8, column = 3, pady = (0, 30))
                                                                                                                                                    else :

                                                                                                                                                        if n_data == 38 :
                                                                                                                                                            e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                                                                                                                                            e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_2.grid(row = 1, column = 1, pady = (30, 0))

                                                                                                                                                            e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_3.grid(row = 1, column = 2, pady = (30, 0))

                                                                                                                                                            e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_4.grid(row = 1, column = 3, pady = (30, 0))

                                                                                                                                                            e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_5.grid(row = 1, column = 4, pady = (30, 0), padx = (0, 30))

                                                                                                                                                            e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_6.grid(row = 2, column = 0, padx = (30, 0))

                                                                                                                                                            e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_7.grid(row = 2, column = 1)

                                                                                                                                                            e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_8.grid(row = 2, column = 2)
                                                                                                                                                        
                                                                                                                                                            e_9 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_9.grid(row = 2, column = 3)

                                                                                                                                                            e_10 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_10.grid(row = 2, column = 4, padx = (0, 30))

                                                                                                                                                            e_11 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_11.grid(row = 3, column = 0, padx = (30, 0))
                                                                                                                                                        
                                                                                                                                                            e_12 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_12.grid(row = 3, column = 1)

                                                                                                                                                            e_13 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_13.grid(row = 3, column = 2)

                                                                                                                                                            e_14 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_14.grid(row = 3, column = 3)

                                                                                                                                                            e_15 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_15.grid(row = 3, column = 4, padx = (0, 30))

                                                                                                                                                            e_16 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_16.grid(row = 4, column = 0, padx = (30, 0))

                                                                                                                                                            e_17 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_17.grid(row = 4, column = 1)

                                                                                                                                                            e_18 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_18.grid(row = 4, column = 2)

                                                                                                                                                            e_19 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_19.grid(row = 4, column = 3)

                                                                                                                                                            e_20 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_20.grid(row = 4, column = 4, padx = (0, 30))

                                                                                                                                                            e_21 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_21.grid(row = 5, column = 0, padx = (30, 0))

                                                                                                                                                            e_22 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_22.grid(row = 5, column = 1)

                                                                                                                                                            e_23 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_23.grid(row = 5, column = 2)

                                                                                                                                                            e_24 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_24.grid(row = 5, column = 3)

                                                                                                                                                            e_25 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_25.grid(row = 5, column = 4, padx = (0, 30))

                                                                                                                                                            e_26 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_26.grid(row = 6, column = 0, padx = (30, 0))

                                                                                                                                                            e_27 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_27.grid(row = 6, column = 1)

                                                                                                                                                            e_28 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_28.grid(row = 6, column = 2)

                                                                                                                                                            e_29 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_29.grid(row = 6, column = 3)

                                                                                                                                                            e_30 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_30.grid(row = 6, column = 4, padx = (0, 30))

                                                                                                                                                            e_31 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_31.grid(row = 7, column = 0, padx = (30, 0))

                                                                                                                                                            e_32 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_32.grid(row = 7, column = 1)

                                                                                                                                                            e_33 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_33.grid(row = 7, column = 2)    

                                                                                                                                                            e_34 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_34.grid(row = 7, column = 3) 

                                                                                                                                                            e_35 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_35.grid(row = 7, column = 4, padx = (0, 30)) 

                                                                                                                                                            e_36 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_36.grid(row = 8, column = 1, pady = (0, 30))  

                                                                                                                                                            e_37 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_37.grid(row = 8, column = 2, pady = (0, 30))

                                                                                                                                                            e_38 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                            e_38.grid(row = 8, column = 3, pady = (0, 30))
                                                                                                                                                        else :

                                                                                                                                                            if n_data == 39 :
                                                                                                                                                                e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                                                                                                                                                e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_2.grid(row = 1, column = 1, pady = (30, 0))

                                                                                                                                                                e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_3.grid(row = 1, column = 2, pady = (30, 0))

                                                                                                                                                                e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_4.grid(row = 1, column = 3, pady = (30, 0))

                                                                                                                                                                e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_5.grid(row = 1, column = 4, pady = (30, 0), padx = (0, 30))

                                                                                                                                                                e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_6.grid(row = 2, column = 0, padx = (30, 0))

                                                                                                                                                                e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_7.grid(row = 2, column = 1)

                                                                                                                                                                e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_8.grid(row = 2, column = 2)
                                                                                                                                                            
                                                                                                                                                                e_9 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_9.grid(row = 2, column = 3)

                                                                                                                                                                e_10 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_10.grid(row = 2, column = 4, padx = (0, 30))

                                                                                                                                                                e_11 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_11.grid(row = 3, column = 0, padx = (30, 0))
                                                                                                                                                            
                                                                                                                                                                e_12 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_12.grid(row = 3, column = 1)

                                                                                                                                                                e_13 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_13.grid(row = 3, column = 2)

                                                                                                                                                                e_14 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_14.grid(row = 3, column = 3)

                                                                                                                                                                e_15 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_15.grid(row = 3, column = 4, padx = (0, 30))

                                                                                                                                                                e_16 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_16.grid(row = 4, column = 0, padx = (30, 0))

                                                                                                                                                                e_17 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_17.grid(row = 4, column = 1)

                                                                                                                                                                e_18 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_18.grid(row = 4, column = 2)

                                                                                                                                                                e_19 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_19.grid(row = 4, column = 3)

                                                                                                                                                                e_20 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_20.grid(row = 4, column = 4, padx = (0, 30))

                                                                                                                                                                e_21 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_21.grid(row = 5, column = 0, padx = (30, 0))

                                                                                                                                                                e_22 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_22.grid(row = 5, column = 1)

                                                                                                                                                                e_23 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_23.grid(row = 5, column = 2)

                                                                                                                                                                e_24 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_24.grid(row = 5, column = 3)

                                                                                                                                                                e_25 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_25.grid(row = 5, column = 4, padx = (0, 30))

                                                                                                                                                                e_26 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_26.grid(row = 6, column = 0, padx = (30, 0))

                                                                                                                                                                e_27 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_27.grid(row = 6, column = 1)

                                                                                                                                                                e_28 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_28.grid(row = 6, column = 2)

                                                                                                                                                                e_29 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_29.grid(row = 6, column = 3)

                                                                                                                                                                e_30 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_30.grid(row = 6, column = 4, padx = (0, 30))

                                                                                                                                                                e_31 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_31.grid(row = 7, column = 0, padx = (30, 0))

                                                                                                                                                                e_32 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_32.grid(row = 7, column = 1)

                                                                                                                                                                e_33 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_33.grid(row = 7, column = 2)    

                                                                                                                                                                e_34 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_34.grid(row = 7, column = 3) 

                                                                                                                                                                e_35 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_35.grid(row = 7, column = 4, padx = (0, 30)) 

                                                                                                                                                                e_36 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_36.grid(row = 8, column = 0, pady = (0, 30), padx = (30, 0))  

                                                                                                                                                                e_37 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_37.grid(row = 8, column = 1, pady = (0, 30))

                                                                                                                                                                e_38 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_38.grid(row = 8, column = 2, pady = (0, 30))

                                                                                                                                                                e_39 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_39.grid(row = 8, column = 3, pady = (0, 30))
                                                                                                                                                            else :

                                                                                                                                                                if n_data == 40 :
                                                                                                                                                                        e_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_1.grid(row = 1, column = 0, pady = (30, 0), padx = (30, 0))

                                                                                                                                                                e_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_2.grid(row = 1, column = 1, pady = (30, 0))

                                                                                                                                                                e_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_3.grid(row = 1, column = 2, pady = (30, 0))

                                                                                                                                                                e_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_4.grid(row = 1, column = 3, pady = (30, 0))

                                                                                                                                                                e_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_5.grid(row = 1, column = 4, pady = (30, 0), padx = (0, 30))

                                                                                                                                                                e_6 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_6.grid(row = 2, column = 0, padx = (30, 0))

                                                                                                                                                                e_7 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_7.grid(row = 2, column = 1)

                                                                                                                                                                e_8 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_8.grid(row = 2, column = 2)
                                                                                                                                                            
                                                                                                                                                                e_9 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_9.grid(row = 2, column = 3)

                                                                                                                                                                e_10 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_10.grid(row = 2, column = 4, padx = (0, 30))

                                                                                                                                                                e_11 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_11.grid(row = 3, column = 0, padx = (30, 0))
                                                                                                                                                            
                                                                                                                                                                e_12 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_12.grid(row = 3, column = 1)

                                                                                                                                                                e_13 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_13.grid(row = 3, column = 2)

                                                                                                                                                                e_14 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_14.grid(row = 3, column = 3)

                                                                                                                                                                e_15 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_15.grid(row = 3, column = 4, padx = (0, 30))

                                                                                                                                                                e_16 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_16.grid(row = 4, column = 0, padx = (30, 0))

                                                                                                                                                                e_17 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_17.grid(row = 4, column = 1)

                                                                                                                                                                e_18 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_18.grid(row = 4, column = 2)

                                                                                                                                                                e_19 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_19.grid(row = 4, column = 3)

                                                                                                                                                                e_20 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_20.grid(row = 4, column = 4, padx = (0, 30))

                                                                                                                                                                e_21 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_21.grid(row = 5, column = 0, padx = (30, 0))

                                                                                                                                                                e_22 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_22.grid(row = 5, column = 1)

                                                                                                                                                                e_23 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_23.grid(row = 5, column = 2)

                                                                                                                                                                e_24 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_24.grid(row = 5, column = 3)

                                                                                                                                                                e_25 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_25.grid(row = 5, column = 4, padx = (0, 30))

                                                                                                                                                                e_26 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_26.grid(row = 6, column = 0, padx = (30, 0))

                                                                                                                                                                e_27 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_27.grid(row = 6, column = 1)

                                                                                                                                                                e_28 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_28.grid(row = 6, column = 2)

                                                                                                                                                                e_29 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_29.grid(row = 6, column = 3)

                                                                                                                                                                e_30 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_30.grid(row = 6, column = 4, padx = (0, 30))

                                                                                                                                                                e_31 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_31.grid(row = 7, column = 0, padx = (30, 0))

                                                                                                                                                                e_32 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_32.grid(row = 7, column = 1)

                                                                                                                                                                e_33 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_33.grid(row = 7, column = 2)    

                                                                                                                                                                e_34 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_34.grid(row = 7, column = 3) 

                                                                                                                                                                e_35 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_35.grid(row = 7, column = 4, padx = (0, 30)) 

                                                                                                                                                                e_36 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_36.grid(row = 8, column = 0, pady = (0, 30), padx = (30, 0))  

                                                                                                                                                                e_37 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_37.grid(row = 8, column = 1, pady = (0, 30))

                                                                                                                                                                e_38 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_38.grid(row = 8, column = 2, pady = (0, 30))

                                                                                                                                                                e_39 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_39.grid(row = 8, column = 3, pady = (0, 30))

                                                                                                                                                                e_40 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                                                                                                                                                e_40.grid(row = 8, column = 4, pady = (0, 30), padx = (0, 30))




# GET STD FUNCTION
def get_std():
    find_std_button.grid_forget()
    
    # GET ARRAY
    if n_data == 1 :
        data = np.array([e_1.get()], dtype = int)
    else :

        if n_data == 2 :
            data = np.array([e_1.get(), e_2.get()], dtype = int)
        else :

            if n_data == 3 :
                data = np.array([e_1.get(), e_2.get(), e_3.get()], dtype = int)
            else :

                if n_data == 4 :
                    data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get()], dtype = int)
                else :

                    if n_data == 5 :
                        data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get()], dtype = int)
                    else :
                        if n_data == 6 :
                            data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get()], dtype = int)
                        else :

                            if n_data == 7 :
                                data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get()], dtype = int)
                            else :

                                if n_data == 8 :
                                    data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get()], dtype = int)
                                else :

                                    if n_data == 9 :
                                        data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get(), e_9.get()], dtype = int)
                                    else :

                                        if n_data == 10 :
                                            data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get(), e_9.get(), e_10.get()], dtype = int)
                                        else :

                                            if n_data == 11 :
                                                data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get(), e_9.get(), e_10.get(), e_11.get()], dtype = int)
                                            else:
                                                
                                                if n_data == 12 :
                                                    data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get(), e_9.get(), e_10.get(), e_11.get(), e_12.get()], dtype = int)
                                                else :

                                                    if n_data == 13 :
                                                        data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get(), e_9.get(), e_10.get(), e_11.get(), e_12.get(), e_13.get()], dtype = int)
                                                    else :

                                                        if n_data == 14 :
                                                            data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get(), e_9.get(), e_10.get(), e_11.get(), e_12.get(), e_13.get(), e_14.get()], dtype = int)
                                                        else:

                                                            if n_data == 15 :
                                                                data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get(), e_9.get(), e_10.get(), e_11.get(), e_12.get(), e_13.get(), e_14.get(), e_15.get()], dtype = int)
                                                            else :

                                                                if n_data == 16 :
                                                                    data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get(), e_9.get(), e_10.get(), e_11.get(), e_12.get(), e_13.get(), e_14.get(), e_15.get(), e_16.get()], dtype = int)
                                                                else :

                                                                    if n_data == 17 :
                                                                        data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get(), e_9.get(), e_10.get(), e_11.get(), e_12.get(), e_13.get(), e_14.get(), e_15.get(), e_16.get(), e_17.get()], dtype = int)
                                                                    else :

                                                                        if n_data == 18 :
                                                                            data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get(), e_9.get(), e_10.get(), e_11.get(), e_12.get(), e_13.get(), e_14.get(), e_15.get(), e_16.get(), e_17.get(), e_18.get()], dtype = int)
                                                                        else :

                                                                            if n_data == 19 :
                                                                                data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get(), e_9.get(), e_10.get(), e_11.get(), e_12.get(), e_13.get(), e_14.get(), e_15.get(), e_16.get(), e_17.get(), e_18.get(), e_19.get()], dtype = int)
                                                                            else :

                                                                                if n_data == 20 :
                                                                                    data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get(), e_9.get(), e_10.get(), e_11.get(), e_12.get(), e_13.get(), e_14.get(), e_15.get(), e_16.get(), e_17.get(), e_18.get(), e_19.get(), e_20.get()], dtype = int)
                                                                                else :

                                                                                    if n_data == 21 :
                                                                                        data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get(), e_9.get(), e_10.get(), e_11.get(), e_12.get(), e_13.get(), e_14.get(), e_15.get(), e_16.get(), e_17.get(), e_18.get(), e_19.get(), e_20.get(), e_21.get()], dtype = int)
                                                                                    else :

                                                                                        if n_data == 22 :
                                                                                            data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get(), e_9.get(), e_10.get(), e_11.get(), e_12.get(), e_13.get(), e_14.get(), e_15.get(), e_16.get(), e_17.get(), e_18.get(), e_19.get(), e_20.get(), e_21.get(), e_22.get()], dtype = int)
                                                                                        else :

                                                                                            if n_data == 23 :
                                                                                                data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get(), e_9.get(), e_10.get(), e_11.get(), e_12.get(), e_13.get(), e_14.get(), e_15.get(), e_16.get(), e_17.get(), e_18.get(), e_19.get(), e_20.get(), e_21.get(), e_22.get(), e_23.get()], dtype = int)
                                                                                            else :

                                                                                                if n_data == 24 :
                                                                                                    data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get(), e_9.get(), e_10.get(), e_11.get(), e_12.get(), e_13.get(), e_14.get(), e_15.get(), e_16.get(), e_17.get(), e_18.get(), e_19.get(), e_20.get(), e_21.get(), e_22.get(), e_23.get(), e_24.get()], dtype = int)
                                                                                                else :

                                                                                                    if n_data == 25 :
                                                                                                        data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get(), e_9.get(), e_10.get(), e_11.get(), e_12.get(), e_13.get(), e_14.get(), e_15.get(), e_16.get(), e_17.get(), e_18.get(), e_19.get(), e_20.get(), e_21.get(), e_22.get(), e_23.get(), e_24.get(), e_25.get()], dtype = int)
                                                                                                    else :

                                                                                                        if n_data == 26 :
                                                                                                            data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get(), e_9.get(), e_10.get(), e_11.get(), e_12.get(), e_13.get(), e_14.get(), e_15.get(), e_16.get(), e_17.get(), e_18.get(), e_19.get(), e_20.get(), e_21.get(), e_22.get(), e_23.get(), e_24.get(), e_25.get(), e_26.get()], dtype = int)
                                                                                                        else :

                                                                                                            if n_data == 27 :
                                                                                                                data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get(), e_9.get(), e_10.get(), e_11.get(), e_12.get(), e_13.get(), e_14.get(), e_15.get(), e_16.get(), e_17.get(), e_18.get(), e_19.get(), e_20.get(), e_21.get(), e_22.get(), e_23.get(), e_24.get(), e_25.get(), e_26.get(), e_27.get()], dtype = int)
                                                                                                            else :

                                                                                                                if n_data == 28 :
                                                                                                                    data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get(), e_9.get(), e_10.get(), e_11.get(), e_12.get(), e_13.get(), e_14.get(), e_15.get(), e_16.get(), e_17.get(), e_18.get(), e_19.get(), e_20.get(), e_21.get(), e_22.get(), e_23.get(), e_24.get(), e_25.get(), e_26.get(), e_27.get(), e_28.get()], dtype = int)
                                                                                                                else :

                                                                                                                    if n_data == 29 :
                                                                                                                        data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get(), e_9.get(), e_10.get(), e_11.get(), e_12.get(), e_13.get(), e_14.get(), e_15.get(), e_16.get(), e_17.get(), e_18.get(), e_19.get(), e_20.get(), e_21.get(), e_22.get(), e_23.get(), e_24.get(), e_25.get(), e_26.get(), e_27.get(), e_28.get(), e_29.get()], dtype = int)
                                                                                                                    else :

                                                                                                                        if n_data == 30 :
                                                                                                                            data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get(), e_9.get(), e_10.get(), e_11.get(), e_12.get(), e_13.get(), e_14.get(), e_15.get(), e_16.get(), e_17.get(), e_18.get(), e_19.get(), e_20.get(), e_21.get(), e_22.get(), e_23.get(), e_24.get(), e_25.get(), e_26.get(), e_27.get(), e_28.get(), e_29.get(), e_30.get()], dtype = int)
                                                                                                                        else :

                                                                                                                            if n_data == 31 :
                                                                                                                                data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get(), e_9.get(), e_10.get(), e_11.get(), e_12.get(), e_13.get(), e_14.get(), e_15.get(), e_16.get(), e_17.get(), e_18.get(), e_19.get(), e_20.get(), e_21.get(), e_22.get(), e_23.get(), e_24.get(), e_25.get(), e_26.get(), e_27.get(), e_28.get(), e_29.get(), e_30.get(), e_31.get()], dtype = int)
                                                                                                                            else :

                                                                                                                                if n_data == 32 :
                                                                                                                                    data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get(), e_9.get(), e_10.get(), e_11.get(), e_12.get(), e_13.get(), e_14.get(), e_15.get(), e_16.get(), e_17.get(), e_18.get(), e_19.get(), e_20.get(), e_21.get(), e_22.get(), e_23.get(), e_24.get(), e_25.get(), e_26.get(), e_27.get(), e_28.get(), e_29.get(), e_30.get(), e_31.get(), e_32.get()], dtype = int)
                                                                                                                                else :

                                                                                                                                    if n_data == 33 :
                                                                                                                                        data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get(), e_9.get(), e_10.get(), e_11.get(), e_12.get(), e_13.get(), e_14.get(), e_15.get(), e_16.get(), e_17.get(), e_18.get(), e_19.get(), e_20.get(), e_21.get(), e_22.get(), e_23.get(), e_24.get(), e_25.get(), e_26.get(), e_27.get(), e_28.get(), e_29.get(), e_30.get(), e_31.get(), e_32.get(), e_33.get()], dtype = int)
                                                                                                                                    else :

                                                                                                                                        if n_data == 34 :
                                                                                                                                            data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get(), e_9.get(), e_10.get(), e_11.get(), e_12.get(), e_13.get(), e_14.get(), e_15.get(), e_16.get(), e_17.get(), e_18.get(), e_19.get(), e_20.get(), e_21.get(), e_22.get(), e_23.get(), e_24.get(), e_25.get(), e_26.get(), e_27.get(), e_28.get(), e_29.get(), e_30.get(), e_31.get(), e_32.get(), e_33.get(), e_34.get()], dtype = int)
                                                                                                                                        else :

                                                                                                                                            if n_data == 35 :
                                                                                                                                                data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get(), e_9.get(), e_10.get(), e_11.get(), e_12.get(), e_13.get(), e_14.get(), e_15.get(), e_16.get(), e_17.get(), e_18.get(), e_19.get(), e_20.get(), e_21.get(), e_22.get(), e_23.get(), e_24.get(), e_25.get(), e_26.get(), e_27.get(), e_28.get(), e_29.get(), e_30.get(), e_31.get(), e_32.get(), e_33.get(), e_34.get(), e_35.get()], dtype = int)
                                                                                                                                            else :

                                                                                                                                                if n_data == 36 :
                                                                                                                                                    data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get(), e_9.get(), e_10.get(), e_11.get(), e_12.get(), e_13.get(), e_14.get(), e_15.get(), e_16.get(), e_17.get(), e_18.get(), e_19.get(), e_20.get(), e_21.get(), e_22.get(), e_23.get(), e_24.get(), e_25.get(), e_26.get(), e_27.get(), e_28.get(), e_29.get(), e_30.get(), e_31.get(), e_32.get(), e_33.get(), e_34.get(), e_35.get(), e_36.get()], dtype = int)
                                                                                                                                                else :

                                                                                                                                                    if n_data == 37 :
                                                                                                                                                        data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get(), e_9.get(), e_10.get(), e_11.get(), e_12.get(), e_13.get(), e_14.get(), e_15.get(), e_16.get(), e_17.get(), e_18.get(), e_19.get(), e_20.get(), e_21.get(), e_22.get(), e_23.get(), e_24.get(), e_25.get(), e_26.get(), e_27.get(), e_28.get(), e_29.get(), e_30.get(), e_31.get(), e_32.get(), e_33.get(), e_34.get(), e_35.get(), e_36.get(), e_37.get()], dtype = int)
                                                                                                                                                    else :

                                                                                                                                                        if n_data == 38 :
                                                                                                                                                            data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get(), e_9.get(), e_10.get(), e_11.get(), e_12.get(), e_13.get(), e_14.get(), e_15.get(), e_16.get(), e_17.get(), e_18.get(), e_19.get(), e_20.get(), e_21.get(), e_22.get(), e_23.get(), e_24.get(), e_25.get(), e_26.get(), e_27.get(), e_28.get(), e_29.get(), e_30.get(), e_31.get(), e_32.get(), e_33.get(), e_34.get(), e_35.get(), e_36.get(), e_37.get(), e_38.get()], dtype = int)
                                                                                                                                                        else :

                                                                                                                                                            if n_data == 39 :
                                                                                                                                                                data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get(), e_9.get(), e_10.get(), e_11.get(), e_12.get(), e_13.get(), e_14.get(), e_15.get(), e_16.get(), e_17.get(), e_18.get(), e_19.get(), e_20.get(), e_21.get(), e_22.get(), e_23.get(), e_24.get(), e_25.get(), e_26.get(), e_27.get(), e_28.get(), e_29.get(), e_30.get(), e_31.get(), e_32.get(), e_33.get(), e_34.get(), e_35.get(), e_36.get(), e_37.get(), e_38.get(), e_39.get()], dtype = int)
                                                                                                                                                            else :

                                                                                                                                                                if n_data == 40 :
                                                                                                                                                                    data = np.array([e_1.get(), e_2.get(), e_3.get(), e_4.get(), e_5.get(), e_6.get(), e_7.get(), e_8.get(), e_9.get(), e_10.get(), e_11.get(), e_12.get(), e_13.get(), e_14.get(), e_15.get(), e_16.get(), e_17.get(), e_18.get(), e_19.get(), e_20.get(), e_21.get(), e_22.get(), e_23.get(), e_24.get(), e_25.get(), e_26.get(), e_27.get(), e_28.get(), e_29.get(), e_30.get(), e_31.get(), e_32.get(), e_33.get(), e_34.get(), e_35.get(), e_36.get(), e_37.get(), e_38.get(), e_39.get(), e_40.get()], dtype = int)
                                                                                                
                                                                                                                                                                
    # GET ANS
    answer = data.std()

    answer = str(answer)

    answer_text = "STD = " + answer

    global answer_label
    answer_label = Label(root, text = answer_text, font = ("Courier New", 20))
    answer_label.grid(row = 9, column = 0, columnspan = 5)
        
                                                                                                                                                                                                                                                      


                                                                                                                        
# CLEAR ENTRY BOXES, ANSWER LABEL AND OPTION MENU
def clear():
    delete_entry_boxes()
    answer_label.destroy()

    n_data_var.set("  0  ")

    # CREATE CANVAS
    canvas = Canvas(root, height = 100, width = 200, bg = "white")
    canvas.grid(row = 1, column = 0, columnspan = 5)

    find_std_button.grid(row = 9, column = 0, columnspan = 5)


# OPTIONMENU
n_data_var = StringVar()
n_data_var.set("  0  ")
get_data = OptionMenu(root, n_data_var, "  1  ", "  2  ", "  3  ", "  4  ", "  5  ", "  6  ", "  7  ", "  8  ", "  9  ", " 10  ", " 11  ", " 12  ", " 13  ", " 14  ",
                        " 15  ", " 16  ", " 17  ", " 18  ", " 19  ", " 20  ", " 21  ", " 22  ", " 23  ", " 24  ", " 25  ", " 26  ", " 27  ", " 28  ", " 29  ", " 30  ",
                        " 31  ", " 32  ", " 33  ", " 34  ", " 35  ", " 36  ", " 37  ", " 38  ", " 39  ", " 40  ", command = get_n_data)
get_data.grid(row = 0, column = 0, columnspan = 5)


# FIND STD BUTTON
find_std_button = Button(root, text = "Find STD", font = ("Courier New", 20), command = get_std)
find_std_button.grid(row = 9, column = 0, columnspan = 5)


# CLEAR BUTTON
clear_button = Button(root, text = "Clear", font = ("Courier New", 20), command = clear)
clear_button.grid(row = 10, column = 0, columnspan = 5)




root.mainloop()