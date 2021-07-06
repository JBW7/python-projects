from tkinter import *
import numpy as np 
from PIL import ImageTk, Image
from tkinter import messagebox


root = Tk()
root.title("Matrix")


# INITAL VARIABLES
rows = 0
columns = 0
equal_no = 0
answer = 0


# INITIAL WIDGETS
# LABEL
answer_label = Label(root)

# ENTRYS
e_1_1 = Entry(root)
e_1_2 = Entry(root)
e_1_3 = Entry(root)
e_1_4 = Entry(root)
e_1_5 = Entry(root)

e_2_1 = Entry(root)
e_2_2 = Entry(root)
e_2_3 = Entry(root)
e_2_4 = Entry(root)
e_2_5 = Entry(root)

e_3_1 = Entry(root)
e_3_2 = Entry(root)
e_3_3 = Entry(root)
e_3_4 = Entry(root)
e_3_5 = Entry(root)

e_4_1 = Entry(root)
e_4_2 = Entry(root)
e_4_3 = Entry(root)
e_4_4 = Entry(root)
e_4_5 = Entry(root)

e_5_1 = Entry(root)
e_5_2 = Entry(root)
e_5_3 = Entry(root)
e_5_4 = Entry(root)
e_5_5 = Entry(root)
    





##################################################################################### ENTRYS
def number_of_entrys():
    global e_1_1
    global e_1_2
    global e_1_3
    global e_1_4
    global e_1_5
    
    global e_2_1
    global e_2_2
    global e_2_3
    global e_2_4
    global e_2_5

    global e_3_1
    global e_3_2
    global e_3_3
    global e_3_4
    global e_3_5

    global e_4_1
    global e_4_2
    global e_4_3
    global e_4_4
    global e_4_5

    global e_5_1
    global e_5_2
    global e_5_3
    global e_5_4
    global e_5_5
    
    
    if rows > 0 and columns > 0 :

        ########################################## COLUMN 1
        if columns == 1 :

            if rows == 1 : 
                e_1_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                e_1_1.grid(row = 3, column = 2, columnspan = 2, padx = (90, 100))
            else:
                
                if rows == 2 :
                    e_1_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_1_1.grid(row = 2, column = 2, columnspan = 2, padx = (90, 100))

                    e_1_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_1_2.grid(row = 3, column = 2, columnspan = 2, padx = (90, 100))
                else :

                    if rows == 3 :
                        e_1_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_1_1.grid(row = 1, column = 2, columnspan = 2, padx = (90, 100), pady = (10, 0))

                        e_1_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_1_2.grid(row = 2, column = 2, columnspan = 2, padx = (90, 100))

                        e_1_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_1_3.grid(row = 3, column = 2, columnspan = 2, padx = (90, 100))
                    else :
                        if rows == 4 :
                            e_1_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_1_1.grid(row = 1, column = 2, columnspan = 2, padx = (90, 100))

                            e_1_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_1_2.grid(row = 2, column = 2, columnspan = 2, padx = (90, 100))

                            e_1_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_1_3.grid(row = 3, column = 2, columnspan = 2, padx = (90, 100))

                            e_1_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_1_4.grid(row = 4, column = 2, columnspan = 2, padx = (90, 100))
                        else :
                            if rows == 5 :
                                e_1_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                e_1_1.grid(row = 1, column = 2, columnspan = 2, padx = (90, 100))
                                
                                e_1_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                e_1_2.grid(row = 2, column = 2, columnspan = 2, padx = (90, 100))
                                
                                e_1_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                e_1_3.grid(row = 3, column = 2, columnspan = 2, padx = (90, 100))

                                e_1_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                e_1_4.grid(row = 4, column = 2, columnspan = 2, padx = (90, 100))

                                e_1_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                                e_1_5.grid(row = 5, column = 2, columnspan = 2, padx = (90, 100))

        
            
    ################################################ COLUMN 2
    if columns == 2 :

        if rows == 1 :
            e_1_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
            e_1_1.grid(row = 3, column = 2)

            
            e_2_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
            e_2_1.grid(row = 3, column = 3)
        else :
            
            if rows == 2 :
                e_1_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                e_1_1.grid(row = 3, column = 2)

                e_1_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                e_1_2.grid(row = 4, column = 2, pady = (0, 20))

                
                e_2_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                e_2_1.grid(row = 3, column = 3)

                e_2_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                e_2_2.grid(row = 4, column = 3, pady = (0, 20))
            else :

                if rows == 3 :
                    e_1_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_1_1.grid(row = 3, column = 2)

                    e_1_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_1_2.grid(row = 4, column = 2)

                    e_1_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_1_3.grid(row = 5, column = 2, pady = (0, 20))

                    
                    e_2_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_2_1.grid(row = 3, column = 3)

                    e_2_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_2_2.grid(row = 4, column = 3)

                    e_2_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_2_3.grid(row = 5, column = 3, pady = (0, 20))

                else :
                    if rows == 4 :
                        e_1_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_1_1.grid(row = 3, column = 2)

                        e_1_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_1_2.grid(row = 4, column = 2)

                        e_1_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_1_3.grid(row = 5, column = 2)

                        e_1_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_1_4.grid(row = 6, column = 2, pady = (0, 20))


                        e_2_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_2_1.grid(row = 3, column = 3)

                        e_2_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_2_2.grid(row = 4, column = 3)

                        e_2_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_2_3.grid(row = 5, column = 3)

                        e_2_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_2_4.grid(row = 6, column = 3, pady = (0, 20))
                    else :
                        if rows == 5 :
                            e_1_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_1_1.grid(row = 1, column = 2, pady = (20, 0))

                            e_1_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_1_2.grid(row = 2, column = 2)

                            e_1_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_1_3.grid(row = 3, column = 2)

                            e_1_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_1_4.grid(row = 4, column = 2)

                            e_1_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_1_5.grid(row = 5, column = 2, pady = (0, 20))


                            e_2_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_2_1.grid(row = 1, column = 3, pady = (20, 0))

                            e_2_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_2_2.grid(row = 2, column = 3)

                            e_2_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_2_3.grid(row = 3, column = 3)

                            e_2_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_2_4.grid(row = 4, column = 3)

                            e_2_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_2_5.grid(row = 5, column = 3, pady = (0, 20))


    
    ################################################ COLUMN 3
    if columns == 3 :

        if rows == 1 :
            e_1_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
            e_1_1.grid(row = 3, column = 1, columnspan = 2)

            
            e_2_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
            e_2_1.grid(row = 3, column = 2, columnspan = 2, padx = (60, 100))

            
            e_3_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
            e_3_1.grid(row = 3, column = 3, columnspan = 2)
        else :

            if rows == 2 :
                e_1_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                e_1_1.grid(row = 3, column = 1, columnspan = 2)

                e_1_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                e_1_2.grid(row = 4, column = 1, columnspan = 2, pady = (0, 20))


                e_2_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                e_2_1.grid(row = 3, column = 2, columnspan = 2, padx = (60, 100))

                e_2_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                e_2_2.grid(row = 4, column = 2, columnspan = 2, padx = (60, 100), pady = (0, 20))

                
                e_3_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                e_3_1.grid(row = 3, column = 3, columnspan = 2)

                e_3_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                e_3_2.grid(row = 4, column = 3, columnspan = 2, pady = (0, 20))
            else :

                if rows == 3 :
                    e_1_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_1_1.grid(row = 3, column = 1, columnspan = 2)

                    e_1_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_1_2.grid(row = 4, column = 1, columnspan = 2)

                    e_1_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_1_3.grid(row = 5, column = 1, pady = (0, 20), columnspan = 2)


                    e_2_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_2_1.grid(row = 3, column = 2, columnspan = 2, padx = (60, 100))

                    e_2_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_2_2.grid(row = 4, column = 2, columnspan = 2, padx = (60, 100))

                    e_2_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_2_3.grid(row = 5, column = 2, pady = (0, 20), columnspan = 2, padx = (60, 100))

                    
                    e_3_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_3_1.grid(row = 3, column = 3, columnspan = 2)

                    e_3_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_3_2.grid(row = 4, column = 3, columnspan = 2)

                    e_3_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_3_3.grid(row = 5, column = 3, pady = (0, 20), columnspan = 2)
                else :

                    if rows == 4 :
                        e_1_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_1_1.grid(row = 3, column = 1, columnspan = 2)

                        e_1_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_1_2.grid(row = 4, column = 1, columnspan = 2)

                        e_1_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_1_3.grid(row = 5, column = 1, columnspan = 2)

                        e_1_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_1_4.grid(row = 6, column = 1, columnspan = 2, pady = (0, 20))


                        e_2_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_2_1.grid(row = 3, column = 2, columnspan = 2, padx = (60, 100))

                        e_2_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_2_2.grid(row = 4, column = 2, columnspan = 2, padx = (60, 100))

                        e_2_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_2_3.grid(row = 5, column = 2, columnspan = 2, padx = (60, 100))

                        e_2_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_2_4.grid(row = 6, column = 2, columnspan = 2, padx = (60, 100), pady = (0, 20))

                        
                        e_3_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_3_1.grid(row = 3, column = 3, columnspan = 2)

                        e_3_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_3_2.grid(row = 4, column = 3, columnspan = 2)

                        e_3_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_3_3.grid(row = 5, column = 3, columnspan = 2)

                        e_3_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_3_4.grid(row = 6, column = 3, pady = (0, 20), columnspan = 2)
                    else :

                        if rows == 5 :
                            e_1_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_1_1.grid(row = 2, column = 1, columnspan = 2, pady = (20, 0))

                            e_1_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_1_2.grid(row = 3, column = 1, columnspan = 2)

                            e_1_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_1_3.grid(row = 4, column = 1, columnspan = 2)

                            e_1_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_1_4.grid(row = 5, column = 1, columnspan = 2)

                            e_1_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_1_5.grid(row = 6, column = 1, columnspan = 2, pady = (0, 20))



                            e_2_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_2_1.grid(row = 2, column = 2, columnspan = 2, padx = (60, 100), pady = (20, 0))

                            e_2_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_2_2.grid(row = 3, column = 2, columnspan = 2, padx = (60, 100))

                            e_2_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_2_3.grid(row = 4, column = 2, columnspan = 2, padx = (60, 100))

                            e_2_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_2_4.grid(row = 5, column = 2, columnspan = 2, padx = (60, 100))

                            e_2_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_2_5.grid(row = 6, column = 2, columnspan = 2, pady = (0, 20), padx = (60, 100))

                            
                            e_3_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_3_1.grid(row = 2, column = 3, columnspan = 2, pady = (20, 0))

                            e_3_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_3_2.grid(row = 3, column = 3, columnspan = 2)

                            e_3_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_3_3.grid(row = 4, column = 3, columnspan = 2)

                            e_3_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_3_4.grid(row = 5, column = 3, columnspan = 2)

                            e_3_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_3_5.grid(row = 6, column = 3, pady = (0, 20), columnspan = 2)



    ################################################ COLUMN 4
    if columns == 4 :

        if rows == 1 :
            e_1_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
            e_1_1.grid(row = 3, column = 1)

            
            e_2_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
            e_2_1.grid(row = 3, column = 2)

            
            e_3_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
            e_3_1.grid(row = 3, column = 3)

            
            e_4_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
            e_4_1.grid(row = 3, column = 4)
        else :

            if rows == 2 :
                e_1_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                e_1_1.grid(row = 2, column = 1)

                e_1_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                e_1_2.grid(row = 3, column = 1)


                e_2_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                e_2_1.grid(row = 2, column = 2)

                e_2_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                e_2_2.grid(row = 3, column = 2)

                
                e_3_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                e_3_1.grid(row = 2, column = 3)

                e_3_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                e_3_2.grid(row = 3, column = 3)

                
                e_4_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                e_4_1.grid(row = 2, column = 4)

                e_4_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                e_4_2.grid(row = 3, column = 4)
            else :

                if rows == 3 :
                    e_1_1 = Entry(root, width = 2, font = ("Courier New", 40))
                    e_1_1.grid(row = 1, column = 1, pady = (20, 0))

                    e_1_2 = Entry(root, width = 2, font = ("Courier New", 40))
                    e_1_2.grid(row = 2, column = 1)

                    e_1_3 = Entry(root, width = 2, font = ("Courier New", 40))
                    e_1_3.grid(row = 3, column = 1)


                    e_2_1 = Entry(root, width = 2, font = ("Courier New", 40))
                    e_2_1.grid(row = 1, column = 2, pady = (20, 0))

                    e_2_2 = Entry(root, width = 2, font = ("Courier New", 40))
                    e_2_2.grid(row = 2, column = 2)

                    e_2_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_2_3.grid(row = 3, column = 2)

                    
                    e_3_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_3_1.grid(row = 1, column = 3, pady = (20, 0))

                    e_3_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_3_2.grid(row = 2, column = 3)

                    e_3_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_3_3.grid(row = 3, column = 3)


                    e_4_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_4_1.grid(row = 1, column = 4, pady = (20, 0))

                    e_4_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_4_2.grid(row = 2, column = 4)

                    e_4_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_4_3.grid(row = 3, column = 4)
                else :
                    
                    if rows == 4 :
                        e_1_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_1_1.grid(row = 1, column = 1, pady = (20, 0))

                        e_1_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_1_2.grid(row = 2, column = 1)

                        e_1_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_1_3.grid(row = 3, column = 1)

                        e_1_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_1_4.grid(row = 4, column = 1)


                        e_2_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_2_1.grid(row = 1, column = 2, pady = (20, 0))

                        e_2_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_2_2.grid(row = 2, column = 2)

                        e_2_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_2_3.grid(row = 3, column = 2)

                        e_2_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_2_4.grid(row = 4, column = 2)

                        
                        e_3_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_3_1.grid(row = 1, column = 3, pady = (20, 0))

                        e_3_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_3_2.grid(row = 2, column = 3)

                        e_3_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_3_3.grid(row = 3, column = 3)

                        e_3_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_3_4.grid(row = 4, column = 3)


                        e_4_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_4_1.grid(row = 1, column = 4, pady = (20, 0))

                        e_4_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_4_2.grid(row = 2, column = 4)

                        e_4_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_4_3.grid(row = 3, column = 4)

                        e_4_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_4_4.grid(row = 4, column = 4)
                    else :

                        if rows == 5 :
                            e_1_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_1_1.grid(row = 1, column = 1, pady = (10, 0))

                            e_1_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_1_2.grid(row = 2, column = 1)

                            e_1_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_1_3.grid(row = 3, column = 1)

                            e_1_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_1_4.grid(row = 4, column = 1)

                            e_1_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_1_5.grid(row = 5, column = 1)


                            e_2_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_2_1.grid(row = 1, column = 2, pady = (10, 0))

                            e_2_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_2_2.grid(row = 2, column = 2)

                            e_2_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_2_3.grid(row = 3, column = 2)

                            e_2_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_2_4.grid(row = 4, column = 2)

                            e_2_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_2_5.grid(row = 5, column = 2)

                            
                            e_3_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_3_1.grid(row = 1, column = 3, pady = (10, 0))

                            e_3_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_3_2.grid(row = 2, column = 3)

                            e_3_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_3_3.grid(row = 3, column = 3)

                            e_3_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_3_4.grid(row = 4, column = 3)

                            e_3_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_3_5.grid(row = 5, column = 3)


                            e_4_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_4_1.grid(row = 1, column = 4, pady = (10, 0))

                            e_4_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_4_2.grid(row = 2, column = 4)

                            e_4_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_4_3.grid(row = 3, column = 4)

                            e_4_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_4_4.grid(row = 4, column = 4)

                            e_4_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_4_5.grid(row = 5, column = 4)

    
    
    ################################################ COLUMN 5
    if columns == 5 :
        
        if rows == 1 :
            e_1_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
            e_1_1.grid(row = 3, column = 0, columnspan = 2)

            
            e_2_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
            e_2_1.grid(row = 3, column = 1, columnspan = 2, padx = (70, 0))

            
            e_3_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
            e_3_1.grid(row = 3, column = 2, columnspan = 2)

            
            e_4_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
            e_4_1.grid(row = 3, column = 3, columnspan = 2, padx = (0, 15))


            e_5_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
            e_5_1.grid(row = 3, column = 4, columnspan = 2)
        else :

            if rows == 2 :
                e_1_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                e_1_1.grid(row = 2, column = 0, columnspan = 2)

                e_1_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                e_1_2.grid(row = 3, column = 0, columnspan = 2)

                
                e_2_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                e_2_1.grid(row = 2, column = 1, columnspan = 2, padx = (70, 0))

                e_2_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                e_2_2.grid(row = 3, column = 1, columnspan = 2, padx = (70, 0))

                
                e_3_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                e_3_1.grid(row = 2, column = 2, columnspan = 2)

                e_3_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                e_3_2.grid(row = 3, column = 2, columnspan = 2)

                
                e_4_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                e_4_1.grid(row = 2, column = 3, columnspan = 2, padx = (0, 15))

                e_4_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                e_4_2.grid(row = 3, column = 3, columnspan = 2, padx = (0, 15))


                e_5_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                e_5_1.grid(row = 2, column = 4, columnspan = 2)

                e_5_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                e_5_2.grid(row = 3, column = 4, columnspan = 2)
            else :

                if rows == 3 :
                    e_1_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_1_1.grid(row = 1, column = 0, columnspan = 2, pady = (20, 0))

                    e_1_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_1_2.grid(row = 2, column = 0, columnspan = 2)

                    e_1_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_1_3.grid(row = 3, column = 0, columnspan = 2, pady = (0, 20))


                    e_2_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_2_1.grid(row = 1, column = 1, columnspan = 2, padx = (70, 0), pady = (20, 0))

                    e_2_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_2_2.grid(row = 2, column = 1, columnspan = 2, padx = (70, 0))

                    e_2_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_2_3.grid(row = 3, column = 1, columnspan = 2, padx = (70, 0), pady = (0, 20))

                    
                    e_3_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_3_1.grid(row = 1, column = 2, columnspan = 2, pady = (20, 0))

                    e_3_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_3_2.grid(row = 2, column = 2, columnspan = 2)

                    e_3_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_3_3.grid(row = 3, column = 2, columnspan = 2, pady = (0, 20))


                    e_4_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_4_1.grid(row = 1, column = 3, columnspan = 2, padx = (0, 15), pady = (20, 0))

                    e_4_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_4_2.grid(row = 2, column = 3, columnspan = 2, padx = (0, 15))

                    e_4_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_4_3.grid(row = 3, column = 3, columnspan = 2, padx = (0, 15), pady = (0, 20))


                    e_5_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_5_1.grid(row = 1, column = 4, columnspan = 2, pady = (20, 0))

                    e_5_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_5_2.grid(row = 2, column = 4, columnspan = 2)

                    e_5_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                    e_5_3.grid(row = 3, column = 4, columnspan = 2, pady = (0, 20))
                else :

                    if rows == 4 :
                        e_1_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_1_1.grid(row = 1, column = 0, columnspan = 2, pady = (20, 0))

                        e_1_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_1_2.grid(row = 2, column = 0, columnspan = 2)

                        e_1_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_1_3.grid(row = 3, column = 0, columnspan = 2)

                        e_1_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_1_4.grid(row = 4, column = 0, columnspan = 2, pady = (0, 20))


                        e_2_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_2_1.grid(row = 1, column = 1, columnspan = 2, padx = (70, 0), pady = (20, 0))

                        e_2_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_2_2.grid(row = 2, column = 1, columnspan = 2, padx = (70, 0))

                        e_2_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_2_3.grid(row = 3, column = 1, columnspan = 2, padx = (70, 0))

                        e_2_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_2_4.grid(row = 4, column = 1, columnspan = 2, padx = (70, 0), pady = (0, 20))

                        
                        e_3_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_3_1.grid(row = 1, column = 2, columnspan = 2, pady = (20, 0))

                        e_3_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_3_2.grid(row = 2, column = 2, columnspan = 2)

                        e_3_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_3_3.grid(row = 3, column = 2, columnspan = 2)

                        e_3_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_3_4.grid(row = 4, column = 2, columnspan = 2, pady = (0, 20))


                        e_4_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_4_1.grid(row = 1, column = 3, columnspan = 2, padx = (0, 15), pady = (20, 0))

                        e_4_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_4_2.grid(row = 2, column = 3, columnspan = 2, padx = (0, 15))

                        e_4_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_4_3.grid(row = 3, column = 3, columnspan = 2, padx = (0, 15))

                        e_4_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_4_4.grid(row = 4, column = 3, columnspan = 2, padx = (0, 15), pady = (0, 20))


                        e_5_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_5_1.grid(row = 1, column = 4, columnspan = 2, pady = (20, 0))

                        e_5_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_5_2.grid(row = 2, column = 4, columnspan = 2)

                        e_5_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_5_3.grid(row = 3, column = 4, columnspan = 2)

                        e_5_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                        e_5_4.grid(row = 4, column = 4, columnspan = 2, pady = (0, 20))
                    else :

                        if rows == 5 :
                            e_1_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_1_1.grid(row = 1, column = 0, columnspan = 2, pady = (20, 0))

                            e_1_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_1_2.grid(row = 2, column = 0, columnspan = 2)

                            e_1_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_1_3.grid(row = 3, column = 0, columnspan = 2)

                            e_1_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_1_4.grid(row = 4, column = 0, columnspan = 2)

                            e_1_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_1_5.grid(row = 5, column = 0, columnspan = 2, pady = (0, 20))


                            e_2_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_2_1.grid(row = 1, column = 1, columnspan = 2, padx = (70, 0), pady = (20, 0))

                            e_2_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_2_2.grid(row = 2, column = 1, columnspan = 2, padx = (70, 0))

                            e_2_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_2_3.grid(row = 3, column = 1, columnspan = 2, padx = (70, 0))

                            e_2_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_2_4.grid(row = 4, column = 1, columnspan = 2, padx = (70, 0))
                            
                            e_2_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_2_5.grid(row = 5, column = 1, columnspan = 2, padx = (70, 0), pady = (0, 20))

                            
                            e_3_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_3_1.grid(row = 1, column = 2, columnspan = 2, pady = (20, 0))

                            e_3_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_3_2.grid(row = 2, column = 2, columnspan = 2)

                            e_3_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_3_3.grid(row = 3, column = 2, columnspan = 2)

                            e_3_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_3_4.grid(row = 4, column = 2, columnspan = 2)

                            e_3_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_3_5.grid(row = 5, column = 2, columnspan = 2, pady = (0, 20))


                            e_4_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_4_1.grid(row = 1, column = 3, columnspan = 2, padx = (0, 15), pady = (20, 0))

                            e_4_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_4_2.grid(row = 2, column = 3, columnspan = 2, padx = (0, 15))

                            e_4_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_4_3.grid(row = 3, column = 3, columnspan = 2, padx = (0, 15))

                            e_4_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_4_4.grid(row = 4, column = 3, columnspan = 2, padx = (0, 15))

                            e_4_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_4_5.grid(row = 5, column = 3, columnspan = 2, padx = (0, 15), pady = (0, 20))


                            e_5_1 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_5_1.grid(row = 1, column = 4, columnspan = 2, pady = (20, 0))

                            e_5_2 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_5_2.grid(row = 2, column = 4, columnspan = 2)

                            e_5_3 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_5_3.grid(row = 3, column = 4, columnspan = 2)

                            e_5_4 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_5_4.grid(row = 4, column = 4, columnspan = 2)
                            
                            e_5_5 = Entry(root, width = 2, font = ("Courier New", 40), justify = CENTER)
                            e_5_5.grid(row = 5, column = 4, columnspan = 2, pady = (0, 20))

##################################################################################### ENTRYS



###################################################################################################################################################### CANVAS
def create_canvas():
    global canvas
    ################################################################################################### COLUMN 0
    if columns == 0 :

        if rows == 0:
            # CREATE CANVAS
            canvas = Canvas(root, height = 200, width = 200, bg = "white")
            
            canvas.grid(row = 1, column = 1, rowspan = 5, columnspan = 5, pady = (5, 0))
        
    
    ################################################################################################### COLUMN 1
    if columns == 1 :

        if rows == 1 :
            # CREATE CANVAS
            canvas = Canvas(root, height = 100, width = 125, bg = "white")

            # CREATE LINES
            line = canvas.create_line(25,15, 50,15,   25,15, 25,90,    25,90, 50,90, width = 5, fill = "black")
            line = canvas.create_line(112,15, 87,15,   112,15, 112,90,    112,90, 87,90, width = 5, fill = "black")
            
            canvas.grid(row = 2, column = 1, rowspan = 3, columnspan = 4)
        else :

            if rows == 2 :
                # CREATE CANVAS
                canvas = Canvas(root, height = 165, width = 125, bg = "white")

                # CREATE LINES
                line = canvas.create_line(25,8, 50,8,   25,8, 25,160,    25,160, 50,160, width = 5, fill = "black")
                line = canvas.create_line(112,8, 87,8,   112,8, 112,160,    112,160, 87,160, width = 5, fill = "black")
            
                canvas.grid(row = 1, column = 1, rowspan = 4, columnspan = 4)
            else :

                if rows == 3 :
                    # CREATE CANVAS
                    canvas = Canvas(root, height = 230, width = 125, bg = "white")

                    # CREATE LINES
                    line = canvas.create_line(25,8, 50,8,   25,8, 25,225,    25,225, 50,225, width = 5, fill = "black")
                    line = canvas.create_line(112,8, 87,8,   112,8, 112,225,    112,225, 87,225, width = 5, fill = "black")
                
                    canvas.grid(row = 1, column = 1, rowspan = 4, columnspan = 4)
                else : 
                    
                    if rows == 4 :
                        # CREATE CANVAS
                        canvas = Canvas(root, height = 355, width = 125, bg = "white")

                        # CREATE LINES
                        line = canvas.create_line(25,8, 50,8,   25,8, 25,352,    25,352, 50,352, width = 5, fill = "black")
                        line = canvas.create_line(112,8, 87,8,   112,8, 112,352,    112,352, 87,352, width = 5, fill = "black")
                    
                        canvas.grid(row = 1, column = 1, rowspan = 4, columnspan = 4)
                    else : 
                    
                        if rows == 5 :
                            # CREATE CANVAS
                            canvas = Canvas(root, height = 450, width = 125, bg = "white")

                            # CREATE LINES
                            line = canvas.create_line(25,8, 50,8,   25,8, 25,445,    25,445, 50,445, width = 5, fill = "black")
                            line = canvas.create_line(112,8, 87,8,   112,8, 112,445,    112,445, 87,445, width = 5, fill = "black")
                        
                            canvas.grid(row = 1, column = 1, rowspan = 5, columnspan = 4)


    
    ################################################################################################### COLUMN 2
    if columns == 2 :

        if rows == 1 :
            # CREATE CANVAS
            canvas = Canvas(root, height = 100, width = 250, bg = "white")

            # CREATE LINES
            line = canvas.create_line(25,15, 50,15,   25,15, 25,90,    25,90, 50,90, width = 5, fill = "black")
            line = canvas.create_line(220,15, 195,15,   220,15, 220,90,    220,90, 195,90, width = 5, fill = "black")
        
            canvas.grid(row = 1, column = 1, rowspan = 5, columnspan = 4)
        else :
            
            if rows == 2 :
                # CREATE CANVAS
                canvas = Canvas(root, height = 165, width = 250, bg = "white")

                # CREATE LINES
                line = canvas.create_line(25,8, 50,8,   25,8, 25,160,    25,160, 50,160, width = 5, fill = "black")
                line = canvas.create_line(220,8, 195,8,   220,8, 220,160,    220,160, 195,160, width = 5, fill = "black")
            
                canvas.grid(row = 1, column = 1, rowspan = 5, columnspan = 4)
            else :

                if rows == 3 :
                    # CREATE CANVAS
                    canvas = Canvas(root, height = 230, width = 250, bg = "white")

                    # CREATE LINES
                    line = canvas.create_line(25,8, 50,8,   25,8, 25,225,    25,225, 50,225, width = 5, fill = "black")
                    line = canvas.create_line(220,8, 195,8,   220,8, 220,225,    220,225, 195,225, width = 5, fill = "black")
                
                    canvas.grid(row = 1, column = 1, rowspan = 5, columnspan = 4)
                else :

                    if rows == 4 :
                        # CREATE CANVAS
                        canvas = Canvas(root, height = 320, width = 250, bg = "white")

                        # CREATE LINES
                        line = canvas.create_line(25,15, 50,15,   25,15, 25,315,    25,315, 50,315, width = 5, fill = "black")
                        line = canvas.create_line(220,15, 195,15,   220,15, 220,315,    220,315, 195,315, width = 5, fill = "black")
                    
                        canvas.grid(row = 1, column = 1, rowspan = 6, columnspan = 4)
                    else :

                        if rows == 5 :
                            # CREATE CANVAS
                            canvas = Canvas(root, height = 375, width = 250, bg = "white")

                            # CREATE LINES
                            line = canvas.create_line(25,15, 50,15,   25,15, 25,365,    25,365, 50,365, width = 5, fill = "black")
                            line = canvas.create_line(220,15, 195,15,   220,15, 220,365,    220,365, 195,365, width = 5, fill = "black")
                        
                            canvas.grid(row = 1, column = 1, rowspan = 5, columnspan = 4)



    ################################################################################################### COLUMN 3
    if columns == 3 :
        
        if rows == 1 :
            # CREATE CANVAS
            canvas = Canvas(root, height = 100, width = 350, bg = "white")

            # CREATE LINES
            line = canvas.create_line(25,15, 50,15,   25,15, 25,90,    25,90, 50,90, width = 5, fill = "black")
            line = canvas.create_line(310,15, 285,15,   310,15, 310,90,    310,90, 285,90, width = 5, fill = "black")
        
            canvas.grid(row = 1, column = 1, rowspan = 5, columnspan = 4)
        else :

            if rows == 2 :
                # CREATE CANVAS
                canvas = Canvas(root, height = 165, width = 350, bg = "white")

                # CREATE LINES
                line = canvas.create_line(25,8, 50,8,   25,8, 25,160,    25,160, 50,160, width = 5, fill = "black")
                line = canvas.create_line(310,8, 285,8,   310,8, 310,160,    310,160, 285,160, width = 5, fill = "black")
            
                canvas.grid(row = 1, column = 1, rowspan = 5, columnspan = 4)
            else :

                if rows == 3 :
                    # CREATE CANVAS
                    canvas = Canvas(root, height = 230, width = 350, bg = "white")

                    # CREATE LINES
                    line = canvas.create_line(25,8, 50,8,   25,8, 25,225,    25,225, 50,225, width = 5, fill = "black")
                    line = canvas.create_line(310,8, 285,8,   310,8, 310,225,    310,225, 285,225, width = 5, fill = "black")
                
                    canvas.grid(row = 1, column = 1, rowspan = 5, columnspan = 4)
                else :

                    if rows == 4 :
                        # CREATE CANVAS
                        canvas = Canvas(root, height = 320, width = 350, bg = "white")

                        # CREATE LINES
                        line = canvas.create_line(25,15, 50,15,   25,15, 25,315,    25,315, 50,315, width = 5, fill = "black")
                        line = canvas.create_line(310,15, 285,15,   310,15, 310,315,    310,315, 285,315, width = 5, fill = "black")
                    
                        canvas.grid(row = 1, column = 1, rowspan = 6, columnspan = 4)
                    else :

                        if rows == 5 :
                            # CREATE CANVAS
                            canvas = Canvas(root, height = 375, width = 350, bg = "white")

                            # CREATE LINES
                            line = canvas.create_line(25,15, 50,15,   25,15, 25,365,    25,365, 50,365, width = 5, fill = "black")
                            line = canvas.create_line(310,15, 285,15,   310,15, 310,365,    310,365, 285,365, width = 5, fill = "black")
                        
                            canvas.grid(row = 1, column = 1, rowspan = 6, columnspan = 4)



    ################################################################################################### COLUMN 4
    if columns == 4 :
        
        if rows == 1 :
            # CREATE CANVAS
            canvas = Canvas(root, height = 100, width = 450, bg = "white")

            # CREATE LINES
            line = canvas.create_line(10,15, 35,15,   10,15, 10,90,    10,90, 35,90, width = 5, fill = "black")
            line = canvas.create_line(450,15, 425,15,   450,15, 450,90,    450,90, 425,90, width = 5, fill = "black")
        
            canvas.grid(row = 1, column = 1, rowspan = 5, columnspan = 4)
        else :

            if rows == 2 :
                # CREATE CANVAS
                canvas = Canvas(root, height = 190, width = 450, bg = "white")

                # CREATE LINES
                line = canvas.create_line(10,10, 35,10,   10,10, 10,163,    10,163, 35,163, width = 5, fill = "black")
                line = canvas.create_line(450,10, 425,10,   450,10, 450,163,    450,163, 425,163, width = 5, fill = "black")
            
                canvas.grid(row = 1, column = 1, rowspan = 5, columnspan = 4)
            else :

                if rows == 3 :
                    # CREATE CANVAS
                    canvas = Canvas(root, height = 250, width = 450, bg = "white")

                    # CREATE LINES
                    line = canvas.create_line(10,10, 35,10,   10,10, 10,240,    10,240, 35,240, width = 5, fill = "black")
                    line = canvas.create_line(440,10, 415,10,   440,10, 440,240,    440,240, 415,240, width = 5, fill = "black")
                
                    canvas.grid(row = 1, column = 1, rowspan = 4, columnspan = 5, pady = (5, 0))
                else :

                    if rows == 4 :
                        # CREATE CANVAS
                        canvas = Canvas(root, height = 400, width = 450, bg = "white")

                        # CREATE LINES
                        line = canvas.create_line(10,20, 35,20,   10,20, 10,380,   10,380, 35,380, width = 5, fill = "black")
                        line = canvas.create_line(440,20, 415,20,   440,20, 440,380,   440,380, 415,380, width = 5, fill = "black")

                        canvas.grid(row = 1, column = 1, rowspan = 5, columnspan = 5, pady = (5, 0))
                    else :

                        if rows == 5 :
                            # CREATE CANVAS
                            canvas = Canvas(root, height = 480, width = 450, bg = "white")

                            # CREATE LINES
                            line = canvas.create_line(10,12, 35,12,   10,12, 10,475,   10,475, 35,475, width = 5, fill = "black")
                            line = canvas.create_line(440,12, 415,12,   440,12, 440,475,   440,475, 415,475, width = 5, fill = "black")

                            canvas.grid(row = 1, column = 1, rowspan = 5, columnspan = 5, pady = (5, 0))




    ################################################################################################### COLUMN 0
    if columns == 5 :
        
        if rows == 1 :
            # CREATE CANVAS
            canvas = Canvas(root, height = 100, width = 500, bg = "white")

            # CREATE LINES
            line = canvas.create_line(10,15, 35,15,   10,15, 10,90,    10,90, 35,90, width = 5, fill = "black")
            line = canvas.create_line(490,15, 465,15,   490,15, 490,90,    490,90, 465,90, width = 5, fill = "black")
        
            canvas.grid(row = 1, column = 1, rowspan = 5, columnspan = 5)
        else :
            
            if rows == 2 :
                # CREATE CANVAS
                canvas = Canvas(root, height = 190, width = 500, bg = "white")

                # CREATE LINES
                line = canvas.create_line(10,10, 35,10,   10,10, 10,163,    10,163, 35,163, width = 5, fill = "black")
                line = canvas.create_line(490,10, 465,10,   490,10, 490,163,    490,163, 465,163, width = 5, fill = "black")
            
                canvas.grid(row = 1, column = 1, rowspan = 5, columnspan = 5)
            else :

                if rows == 3 :
                    # CREATE CANVAS
                    canvas = Canvas(root, height = 250, width = 500, bg = "white")

                    # CREATE LINES
                    line = canvas.create_line(10,10, 35,10,   10,10, 10,225,    10,225, 35,225, width = 5, fill = "black")
                    line = canvas.create_line(490,10, 465,10,   490,10, 490,225,    490,225, 465,225, width = 5, fill = "black")
                
                    canvas.grid(row = 1, column = 1, rowspan = 5, columnspan = 5)
                else :

                    if rows == 4 :
                        # CREATE CANVAS
                        canvas = Canvas(root, height = 325, width = 500, bg = "white")

                        # CREATE LINES
                        line = canvas.create_line(10,10, 35,10,   10,10, 10,305,    10,305, 35,305, width = 5, fill = "black")
                        line = canvas.create_line(490,10, 465,10,   490,10, 490,305,    490,305, 465,305, width = 5, fill = "black")
                    
                        canvas.grid(row = 1, column = 1, rowspan = 5, columnspan = 5)
                    else :

                        if rows == 5 :
                            # CREATE CANVAS
                            canvas = Canvas(root, height = 400, width = 500, bg = "white")

                            # CREATE LINES
                            line = canvas.create_line(10,10, 35,10,   10,10, 10,390,    10,390, 35,390, width = 5, fill = "black")
                            line = canvas.create_line(490,10, 465,10,   490,10, 490,390,    490,390, 465,390, width = 5, fill = "black")
                        
                            canvas.grid(row = 1, column = 1, rowspan = 5, columnspan = 5)

                
# INITAL CANVAS                
create_canvas()

###################################################################################################################################################### CANVAS



# DESTROY ALL ENTRYS
def delete():
    if rows > 0 and columns > 0 :
    
        e_1_1.destroy()
        e_1_2.destroy()
        e_1_3.destroy()
        e_1_4.destroy()
        e_1_5.destroy()

        e_2_1.destroy()
        e_2_2.destroy()
        e_2_3.destroy()
        e_2_4.destroy()
        e_2_5.destroy()

        e_3_1.destroy()
        e_3_2.destroy()
        e_3_3.destroy()
        e_3_4.destroy()
        e_3_5.destroy()

        e_4_1.destroy()
        e_4_2.destroy()
        e_4_3.destroy()
        e_4_4.destroy()
        e_4_5.destroy()

        e_5_1.destroy()
        e_5_2.destroy()
        e_5_3.destroy()
        e_5_4.destroy()
        e_5_5.destroy()


# DESTROY ALL CANVAS
def delete_canvas():
    if rows > 0 and columns > 0 :
        canvas.grid_forget()


#################################################################################################################################### GET FIRST MATRIX
def get_first_matrix():
    global first_matrix

    try : 
        if equal_no == 0 :
        
            ################################################ COLUMN 1
            if columns == 1 :

                if rows == 1 :
                    first_matrix = np.array([e_1_1.get()], dtype = int)
                    
                    e_1_1.delete(0, END)
                else :

                    if rows == 2 :
                        first_matrix = np.array([[e_1_1.get()], 
                                                [e_1_2.get()]], dtype = int)
                        
                        e_1_1.delete(0, END)
                        e_1_2.delete(0, END)
                    else :

                        if rows == 3 :
                            first_matrix = np.array([[e_1_1.get()], 
                                                    [e_1_2.get()],
                                                    [e_1_3.get()]], dtype = int)

                            e_1_1.delete(0, END)
                            e_1_2.delete(0, END)
                            e_1_3.delete(0, END)
                        else : 

                            if rows == 4 :
                                first_matrix = np.array([[e_1_1.get()], 
                                                        [e_1_2.get()],
                                                        [e_1_3.get()],
                                                        [e_1_4.get()]], dtype = int)

                                e_1_1.delete(0, END)
                                e_1_2.delete(0, END)
                                e_1_3.delete(0, END)
                                e_1_4.delete(0, END)
                            else :
                                
                                if rows == 5 :
                                    first_matrix = np.array([[e_1_1.get()], 
                                                            [e_1_2.get()],
                                                            [e_1_3.get()],
                                                            [e_1_4.get()],
                                                            [e_1_5.get()]], dtype = int)

                                e_1_1.delete(0, END)
                                e_1_2.delete(0, END)
                                e_1_3.delete(0, END)
                                e_1_4.delete(0, END)
                                e_1_5.delete(0, END)

            
            
            ################################################ COLUMN 2
            if columns == 2 :

                if rows == 1 :
                    first_matrix = np.array([e_1_1.get(), e_2_1.get()], dtype = int)

                    e_1_1.delete(0, END)
                    e_2_1.delete(0, END)
                else :
                    
                    if rows == 2 :
                        first_matrix = np.array([[e_1_1.get(), e_2_1.get()], 
                                                [e_1_2.get(), e_2_2.get()]], dtype = int)

                        e_1_1.delete(0, END)
                        e_2_1.delete(0, END)
                        e_1_2.delete(0, END)
                        e_2_2.delete(0, END)
                    else :
                        
                        if rows == 3 :
                            first_matrix = np.array([[e_1_1.get(), e_2_1.get()], 
                                                    [e_1_2.get(), e_2_2.get()],
                                                    [e_1_3.get(), e_2_3.get()]], dtype = int)

                            e_1_1.delete(0, END)
                            e_1_2.delete(0, END)
                            e_2_1.delete(0, END)
                            e_2_2.delete(0, END)
                            e_1_3.delete(0, END)
                            e_2_3.delete(0, END)
                        else :
                            
                            if rows == 4 :
                                first_matrix = np.array([[e_1_1.get(), e_2_1.get()], 
                                                        [e_1_2.get(), e_2_2.get()],
                                                        [e_1_3.get(), e_2_3.get()],
                                                        [e_1_4.get(), e_2_4.get()]], dtype = int)

                                e_1_1.delete(0, END)
                                e_1_2.delete(0, END)
                                e_2_1.delete(0, END)
                                e_2_2.delete(0, END)
                                e_1_3.delete(0, END)
                                e_2_3.delete(0, END)
                                e_1_4.delete(0, END)
                                e_2_4.delete(0, END)
                            else :

                                if rows == 5 :
                                    first_matrix = np.array([[e_1_1.get(), e_2_1.get()], 
                                                            [e_1_2.get(), e_2_2.get()],
                                                            [e_1_3.get(), e_2_3.get()],
                                                            [e_1_4.get(), e_2_4.get()],
                                                            [e_1_5.get(), e_2_5.get()]], dtype = int)

                                e_1_1.delete(0, END)
                                e_1_2.delete(0, END)
                                e_2_1.delete(0, END)
                                e_2_2.delete(0, END)
                                e_1_3.delete(0, END)
                                e_2_3.delete(0, END)
                                e_1_4.delete(0, END)
                                e_2_4.delete(0, END)
                                e_1_5.delete(0, END)
                                e_2_5.delete(0, END)



            ################################################ COLUMN 3
            if columns == 3 :

                if rows == 1 :
                    first_matrix = np.array([e_1_1.get(), e_2_1.get(), e_3_1.get()], dtype = int)

                    e_1_1.delete(0, END)
                    e_2_1.delete(0, END)
                    e_3_1.delete(0, END)
                else :
                    
                    if rows == 2 :
                        first_matrix = np.array([[e_1_1.get(), e_2_1.get(), e_3_1.get()], 
                                                [e_1_2.get(), e_2_2.get(), e_3_2.get()]], dtype = int)
                    
                        e_1_1.delete(0, END)
                        e_2_1.delete(0, END)
                        e_3_1.delete(0, END)
                        e_1_2.delete(0, END)
                        e_2_2.delete(0, END)
                        e_3_2.delete(0, END)
                    else :
                        
                        if rows == 3 :
                            first_matrix = np.array([[e_1_1.get(), e_2_1.get(), e_3_1.get()], 
                                                    [e_1_2.get(), e_2_2.get(), e_3_2.get()],
                                                    [e_1_3.get(), e_2_3.get(), e_3_3.get()]], dtype = int)

                            e_1_1.delete(0, END)
                            e_2_1.delete(0, END)
                            e_3_1.delete(0, END)
                            e_1_2.delete(0, END)
                            e_2_2.delete(0, END)
                            e_3_2.delete(0, END)
                            e_1_3.delete(0, END)
                            e_2_3.delete(0, END)
                            e_3_3.delete(0, END)
                        else :
                            
                            if rows == 4 :
                                first_matrix = np.array([[e_1_1.get(), e_2_1.get(), e_3_1.get()], 
                                                        [e_1_2.get(), e_2_2.get(), e_3_2.get()],
                                                        [e_1_3.get(), e_2_3.get(), e_3_3.get()],
                                                        [e_1_4.get(), e_2_4.get(), e_3_4.get()]], dtype = int)

                                e_1_1.delete(0, END)
                                e_2_1.delete(0, END)
                                e_3_1.delete(0, END)
                                e_1_2.delete(0, END)
                                e_2_2.delete(0, END)
                                e_3_2.delete(0, END)
                                e_1_3.delete(0, END)
                                e_2_3.delete(0, END)
                                e_3_3.delete(0, END)
                                e_1_4.delete(0, END)
                                e_2_4.delete(0, END)
                                e_3_4.delete(0, END)
                            else :

                                if rows == 5 :
                                    first_matrix = np.array([[e_1_1.get(), e_2_1.get(), e_3_1.get()], 
                                                            [e_1_2.get(), e_2_2.get(), e_3_1.get()],
                                                            [e_1_3.get(), e_2_3.get(), e_3_3.get()],
                                                            [e_1_4.get(), e_2_4.get(), e_3_4.get()],
                                                            [e_1_5.get(), e_2_5.get(), e_3_5.get()]], dtype = int)

                                    e_1_1.delete(0, END)
                                    e_2_1.delete(0, END)
                                    e_3_1.delete(0, END)
                                    e_1_2.delete(0, END)
                                    e_2_2.delete(0, END)
                                    e_3_2.delete(0, END)
                                    e_1_3.delete(0, END)
                                    e_2_3.delete(0, END)
                                    e_3_3.delete(0, END)
                                    e_1_4.delete(0, END)
                                    e_2_4.delete(0, END)
                                    e_3_4.delete(0, END)
                                    e_1_5.delete(0, END)
                                    e_2_5.delete(0, END)
                                    e_3_5.delete(0, END)


            
            ################################################ COLUMN 4
            if columns == 4 :

                if rows == 1 :
                    first_matrix = np.array([e_1_1.get(), e_2_1.get(), e_3_1.get(), e_4_1.get()], dtype = int)

                    e_1_1.delete(0, END)
                    e_2_1.delete(0, END)
                    e_3_1.delete(0, END)
                    e_4_1.delete(0, END)
                else :
                    
                    if rows == 2 :
                        first_matrix = np.array([[e_1_1.get(), e_2_1.get(), e_3_1.get(), e_4_1.get()], 
                                                [e_1_2.get(), e_2_2.get(), e_3_2.get(), e_4_2.get()]], dtype = int)

                        e_1_1.delete(0, END)
                        e_2_1.delete(0, END)
                        e_3_1.delete(0, END)
                        e_4_1.delete(0, END)
                        e_1_2.delete(0, END)
                        e_2_2.delete(0, END)
                        e_3_2.delete(0, END)
                        e_4_2.delete(0, END)
                    else :
                        
                        if rows == 3 :
                            first_matrix = np.array([[e_1_1.get(), e_2_1.get(), e_3_1.get(), e_4_1.get()], 
                                                    [e_1_2.get(), e_2_2.get(), e_3_2.get(), e_4_2.get()],
                                                    [e_1_3.get(), e_2_3.get(), e_3_3.get(), e_4_3.get()]], dtype = int)

                            e_1_1.delete(0, END)
                            e_2_1.delete(0, END)
                            e_3_1.delete(0, END)
                            e_4_1.delete(0, END)
                            e_1_2.delete(0, END)
                            e_2_2.delete(0, END)
                            e_3_2.delete(0, END)
                            e_4_2.delete(0, END)
                            e_1_3.delete(0, END)
                            e_2_3.delete(0, END)
                            e_3_3.delete(0, END)
                            e_4_3.delete(0, END)
                        else :
                            
                            if rows == 4 :
                                first_matrix = np.array([[e_1_1.get(), e_2_1.get(), e_3_1.get(), e_4_1.get()], 
                                                        [e_1_2.get(), e_2_2.get(), e_3_2.get(), e_4_2.get()],
                                                        [e_1_3.get(), e_2_3.get(), e_3_3.get(), e_4_3.get()],
                                                        [e_1_4.get(), e_2_4.get(), e_3_4.get(), e_4_4.get()]], dtype = int)

                                e_1_1.delete(0, END)
                                e_2_1.delete(0, END)
                                e_3_1.delete(0, END)
                                e_4_1.delete(0, END)
                                e_1_2.delete(0, END)
                                e_2_2.delete(0, END)
                                e_3_2.delete(0, END)
                                e_4_2.delete(0, END)
                                e_1_3.delete(0, END)
                                e_2_3.delete(0, END)
                                e_3_3.delete(0, END)
                                e_4_3.delete(0, END)
                                e_1_4.delete(0, END)
                                e_2_4.delete(0, END)
                                e_3_4.delete(0, END)
                                e_4_4.delete(0, END)
                            else :

                                if rows == 5 :
                                    first_matrix = np.array([[e_1_1.get(), e_2_1.get(), e_3_1.get(), e_4_1.get()], 
                                                            [e_1_2.get(), e_2_2.get(), e_3_1.get(), e_4_2.get()],
                                                            [e_1_3.get(), e_2_3.get(), e_3_3.get(), e_4_3.get()],
                                                            [e_1_4.get(), e_2_4.get(), e_3_4.get(), e_4_4.get()],
                                                            [e_1_5.get(), e_2_5.get(), e_3_5.get(), e_4_5.get()]], dtype = int)

                                    e_1_1.delete(0, END)
                                    e_2_1.delete(0, END)
                                    e_3_1.delete(0, END)
                                    e_4_1.delete(0, END)
                                    e_1_2.delete(0, END)
                                    e_2_2.delete(0, END)
                                    e_3_2.delete(0, END)
                                    e_4_2.delete(0, END)
                                    e_1_3.delete(0, END)
                                    e_2_3.delete(0, END)
                                    e_3_3.delete(0, END)
                                    e_4_3.delete(0, END)
                                    e_1_4.delete(0, END)
                                    e_2_4.delete(0, END)
                                    e_3_4.delete(0, END)
                                    e_4_4.delete(0, END)
                                    e_1_5.delete(0, END)
                                    e_2_5.delete(0, END)
                                    e_3_5.delete(0, END)
                                    e_4_5.delete(0, END)



            ################################################ COLUMN 5
            if columns == 5 :

                if rows == 1 :
                    first_matrix = np.array([e_1_1.get(), e_2_1.get(), e_3_1.get(), e_4_1.get(), e_5_1.get()], dtype = int)

                    e_1_1.delete(0, END)
                    e_2_1.delete(0, END)
                    e_3_1.delete(0, END)
                    e_4_1.delete(0, END)
                    e_5_1.delete(0, END)
                else :
                    
                    if rows == 2 :
                        first_matrix = np.array([[e_1_1.get(), e_2_1.get(), e_3_1.get(), e_4_1.get(), e_5_1.get()], 
                                                [e_1_2.get(), e_2_2.get(), e_3_2.get(), e_4_2.get(), e_5_2.get()]], dtype = int)

                        e_1_1.delete(0, END)
                        e_2_1.delete(0, END)
                        e_3_1.delete(0, END)
                        e_4_1.delete(0, END)
                        e_5_1.delete(0, END)
                        e_1_2.delete(0, END)
                        e_2_2.delete(0, END)
                        e_3_2.delete(0, END)
                        e_4_2.delete(0, END)
                        e_5_2.delete(0, END)
                    else :
                        
                        if rows == 3 :
                            first_matrix = np.array([[e_1_1.get(), e_2_1.get(), e_3_1.get(), e_4_1.get(), e_5_1.get()], 
                                                    [e_1_2.get(), e_2_2.get(), e_3_2.get(), e_4_2.get(), e_5_2.get()],
                                                    [e_1_3.get(), e_2_3.get(), e_3_3.get(), e_4_3.get(), e_5_3.get()]], dtype = int)

                            e_1_1.delete(0, END)
                            e_2_1.delete(0, END)
                            e_3_1.delete(0, END)
                            e_4_1.delete(0, END)
                            e_5_1.delete(0, END)
                            e_1_2.delete(0, END)
                            e_2_2.delete(0, END)
                            e_3_2.delete(0, END)
                            e_4_2.delete(0, END)
                            e_5_2.delete(0, END)
                            e_1_3.delete(0, END)
                            e_2_3.delete(0, END)
                            e_3_3.delete(0, END)
                            e_4_3.delete(0, END)
                            e_5_3.delete(0, END)
                        else :
                            
                            if rows == 4 :
                                first_matrix = np.array([[e_1_1.get(), e_2_1.get(), e_3_1.get(), e_4_1.get(), e_5_1.get()], 
                                                        [e_1_2.get(), e_2_2.get(), e_3_2.get(), e_4_2.get(), e_5_2.get()],
                                                        [e_1_3.get(), e_2_3.get(), e_3_3.get(), e_4_3.get(), e_5_3.get()],
                                                        [e_1_4.get(), e_2_4.get(), e_3_4.get(), e_4_4.get(), e_5_4.get()]], dtype = int)

                                e_1_1.delete(0, END)
                                e_2_1.delete(0, END)
                                e_3_1.delete(0, END)
                                e_4_1.delete(0, END)
                                e_5_1.delete(0, END)
                                e_1_2.delete(0, END)
                                e_2_2.delete(0, END)
                                e_3_2.delete(0, END)
                                e_4_2.delete(0, END)
                                e_5_2.delete(0, END)
                                e_1_3.delete(0, END)
                                e_2_3.delete(0, END)
                                e_3_3.delete(0, END)
                                e_4_3.delete(0, END)
                                e_5_3.delete(0, END)
                                e_1_4.delete(0, END)
                                e_2_4.delete(0, END)
                                e_3_4.delete(0, END)
                                e_4_4.delete(0, END)
                                e_5_4.delete(0, END)
                            else :

                                if rows == 5 :
                                    first_matrix = np.array([[e_1_1.get(), e_2_1.get(), e_3_1.get(), e_4_1.get(), e_5_1.get()], 
                                                            [e_1_2.get(), e_2_2.get(), e_3_1.get(), e_4_2.get(), e_5_2.get()],
                                                            [e_1_3.get(), e_2_3.get(), e_3_3.get(), e_4_3.get(), e_5_3.get()],
                                                            [e_1_4.get(), e_2_4.get(), e_3_4.get(), e_4_4.get(), e_5_4.get()],
                                                            [e_1_5.get(), e_2_5.get(), e_3_5.get(), e_4_5.get(), e_5_5.get()]], dtype = int)

                                    e_1_1.delete(0, END)
                                    e_2_1.delete(0, END)
                                    e_3_1.delete(0, END)
                                    e_4_1.delete(0, END)
                                    e_5_1.delete(0, END)
                                    e_1_2.delete(0, END)
                                    e_2_2.delete(0, END)
                                    e_3_2.delete(0, END)
                                    e_4_2.delete(0, END)
                                    e_5_2.delete(0, END)
                                    e_1_3.delete(0, END)
                                    e_2_3.delete(0, END)
                                    e_3_3.delete(0, END)
                                    e_4_3.delete(0, END)
                                    e_5_3.delete(0, END)
                                    e_1_4.delete(0, END)
                                    e_2_4.delete(0, END)
                                    e_3_4.delete(0, END)
                                    e_4_4.delete(0, END)
                                    e_5_4.delete(0, END)
                                    e_1_5.delete(0, END)
                                    e_2_5.delete(0, END)
                                    e_3_5.delete(0, END)
                                    e_4_5.delete(0, END)
                                    e_5_5.delete(0, END)
        if equal_no > 0 :
            first_matrix = answer

            
            ################################################ COLUMN 1
            if columns == 1 :

                if rows == 1 :
                    e_1_1.delete(0, END)
                else :

                    if rows == 2 :
                        e_1_1.delete(0, END)
                        e_1_2.delete(0, END)
                    else :

                        if rows == 3 :
                            e_1_1.delete(0, END)
                            e_1_2.delete(0, END)
                            e_1_3.delete(0, END)
                        else:

                            if rows == 4 :

                                e_1_1.delete(0, END)
                                e_1_2.delete(0, END)
                                e_1_3.delete(0, END)
                                e_1_4.delete(0, END)
                            else:

                                if rows == 5 :
                                    e_1_1.delete(0, END)
                                    e_1_2.delete(0, END)
                                    e_1_3.delete(0, END)
                                    e_1_4.delete(0, END)
                                    e_1_5.delete(0, END)
                                

                                    
            ################################################ COLUMN 2
            if columns == 2 :

                if rows == 1 :
                    e_1_1.delete(0, END)
                    e_1_2.delete(0, END)
                else:

                    if rows == 2 :
                        e_1_1.delete(0, END)
                        e_2_1.delete(0, END)
                        e_1_2.delete(0, END)
                        e_2_2.delete(0, END)
                    else :

                        if rows == 3 :
                            e_1_1.delete(0, END)
                            e_1_2.delete(0, END)
                            e_1_2.delete(0, END)
                            e_2_2.delete(0, END)
                            e_1_3.delete(0, END)
                            e_2_3.delete(0, END)
                        else :

                            if rows == 4 :
                                e_1_1.delete(0, END)
                                e_1_2.delete(0, END)
                                e_1_2.delete(0, END)
                                e_2_2.delete(0, END)
                                e_1_3.delete(0, END)
                                e_2_3.delete(0, END)
                                e_1_4.delete(0, END)
                                e_2_4.delete(0, END)
                            else:

                                if rows == 5 :
                                    e_1_1.delete(0, END)
                                    e_1_2.delete(0, END)
                                    e_1_2.delete(0, END)
                                    e_2_2.delete(0, END)
                                    e_1_3.delete(0, END)
                                    e_2_3.delete(0, END)
                                    e_1_4.delete(0, END)
                                    e_2_4.delete(0, END)
                                    e_1_5.delete(0, END)
                                    e_2_5.delete(0, END)



            ################################################ COLUMN 3
            if columns == 3 :

                if rows == 1 :
                    e_1_1.delete(0, END)
                    e_2_1.delete(0, END)
                    e_3_1.delete(0, END)
                else :

                    if rows == 2 :
                        e_1_1.delete(0, END)
                        e_2_1.delete(0, END)
                        e_3_1.delete(0, END)
                        e_1_2.delete(0, END)
                        e_2_2.delete(0, END)
                        e_3_2.delete(0, END)
                    else :

                        if rows == 3 :
                            e_1_1.delete(0, END)
                            e_2_1.delete(0, END)
                            e_3_1.delete(0, END)
                            e_1_2.delete(0, END)
                            e_2_2.delete(0, END)
                            e_3_2.delete(0, END)
                            e_1_3.delete(0, END)
                            e_2_3.delete(0, END)
                            e_3_3.delete(0, END)
                        else :

                            if rows == 4 :
                                e_1_1.delete(0, END)
                                e_2_1.delete(0, END)
                                e_3_1.delete(0, END)
                                e_1_2.delete(0, END)
                                e_2_2.delete(0, END)
                                e_3_2.delete(0, END)
                                e_1_3.delete(0, END)
                                e_2_3.delete(0, END)
                                e_3_3.delete(0, END)
                                e_1_4.delete(0, END)
                                e_2_4.delete(0, END)
                                e_3_4.delete(0, END)
                            else :
                                if rows == 5 : 
                                    e_1_1.delete(0, END)
                                    e_2_1.delete(0, END)
                                    e_3_1.delete(0, END)
                                    e_1_2.delete(0, END)
                                    e_2_2.delete(0, END)
                                    e_3_2.delete(0, END)
                                    e_1_3.delete(0, END)
                                    e_2_3.delete(0, END)
                                    e_3_3.delete(0, END)
                                    e_1_4.delete(0, END)
                                    e_2_4.delete(0, END)
                                    e_3_4.delete(0, END)
                                    e_1_5.delete(0, END)
                                    e_2_5.delete(0, END)
                                    e_3_5.delete(0, END)

                

            ################################################ COLUMN 4
            if columns == 4 :

                if rows == 1 :
                    e_1_1.delete(0, END)
                    e_2_1.delete(0, END)
                    e_3_1.delete(0, END)
                    e_4_1.delete(0, END)
                else:

                    if rows == 2 :
                        e_1_1.delete(0, END)
                        e_2_1.delete(0, END)
                        e_3_1.delete(0, END)
                        e_4_1.delete(0, END)
                        e_1_2.delete(0, END)
                        e_2_2.delete(0, END)
                        e_3_2.delete(0, END)
                        e_4_2.delete(0, END)
                    else :

                        if rows == 3 :
                            e_1_1.delete(0, END)
                            e_2_1.delete(0, END)
                            e_3_1.delete(0, END)
                            e_4_1.delete(0, END)
                            e_1_2.delete(0, END)
                            e_2_2.delete(0, END)
                            e_3_2.delete(0, END)
                            e_4_2.delete(0, END)
                            e_1_3.delete(0, END)
                            e_2_3.delete(0, END)
                            e_3_3.delete(0, END)
                            e_4_3.delete(0, END)
                        else :

                            if rows == 4 :
                                e_1_1.delete(0, END)
                                e_2_1.delete(0, END)
                                e_3_1.delete(0, END)
                                e_4_1.delete(0, END)
                                e_1_2.delete(0, END)
                                e_2_2.delete(0, END)
                                e_3_2.delete(0, END)
                                e_4_2.delete(0, END)
                                e_1_3.delete(0, END)
                                e_2_3.delete(0, END)
                                e_3_3.delete(0, END)
                                e_4_3.delete(0, END)
                                e_1_4.delete(0, END)
                                e_2_4.delete(0, END)
                                e_3_4.delete(0, END)
                                e_4_4.delete(0, END)
                            else :

                                if rows == 5 :
                                    e_1_1.delete(0, END)
                                    e_2_1.delete(0, END)
                                    e_3_1.delete(0, END)
                                    e_4_1.delete(0, END)
                                    e_1_2.delete(0, END)
                                    e_2_2.delete(0, END)
                                    e_3_2.delete(0, END)
                                    e_4_2.delete(0, END)
                                    e_1_3.delete(0, END)
                                    e_2_3.delete(0, END)
                                    e_3_3.delete(0, END)
                                    e_4_3.delete(0, END)
                                    e_1_4.delete(0, END)
                                    e_2_4.delete(0, END)
                                    e_3_4.delete(0, END)
                                    e_4_4.delete(0, END)
                                    e_1_5.delete(0, END)
                                    e_2_5.delete(0, END)
                                    e_3_5.delete(0, END)
                                    e_4_5.delete(0, END)



            ################################################ COLUMN 5
            if columns == 5 :

                if rows == 1 :
                    e_1_1.delete(0, END)
                    e_2_1.delete(0, END)
                    e_3_1.delete(0, END)
                    e_4_1.delete(0, END)
                    e_5_1.delete(0, END)
                else :

                    if rows == 2 :
                        e_1_1.delete(0, END)
                        e_2_1.delete(0, END)
                        e_3_1.delete(0, END)
                        e_4_1.delete(0, END)
                        e_5_1.delete(0, END)
                        e_1_2.delete(0, END)
                        e_2_2.delete(0, END)
                        e_3_2.delete(0, END)
                        e_4_2.delete(0, END)
                        e_5_2.delete(0, END)
                    else :
                        if rows == 3 :

                            e_1_1.delete(0, END)
                            e_2_1.delete(0, END)
                            e_3_1.delete(0, END)
                            e_4_1.delete(0, END)
                            e_5_1.delete(0, END)
                            e_1_2.delete(0, END)
                            e_2_2.delete(0, END)
                            e_3_2.delete(0, END)
                            e_4_2.delete(0, END)
                            e_5_2.delete(0, END)
                            e_1_3.delete(0, END)
                            e_2_3.delete(0, END)
                            e_3_3.delete(0, END)
                            e_4_3.delete(0, END)
                            e_5_3.delete(0, END)
                        else :

                            if rows == 4 :
                                e_1_1.delete(0, END)
                                e_2_1.delete(0, END)
                                e_3_1.delete(0, END)
                                e_4_1.delete(0, END)
                                e_5_1.delete(0, END)
                                e_1_2.delete(0, END)
                                e_2_2.delete(0, END)
                                e_3_2.delete(0, END)
                                e_4_2.delete(0, END)
                                e_5_2.delete(0, END)
                                e_1_3.delete(0, END)
                                e_2_3.delete(0, END)
                                e_3_3.delete(0, END)
                                e_4_3.delete(0, END)
                                e_5_3.delete(0, END)
                                e_1_4.delete(0, END)
                                e_2_4.delete(0, END)
                                e_3_4.delete(0, END)
                                e_4_4.delete(0, END)
                                e_5_4.delete(0, END)
                            else :

                                if rows == 5 :
                                    e_1_1.delete(0, END)
                                    e_2_1.delete(0, END)
                                    e_3_1.delete(0, END)
                                    e_4_1.delete(0, END)
                                    e_5_1.delete(0, END)
                                    e_1_2.delete(0, END)
                                    e_2_2.delete(0, END)
                                    e_3_2.delete(0, END)
                                    e_4_2.delete(0, END)
                                    e_5_2.delete(0, END)
                                    e_1_3.delete(0, END)
                                    e_2_3.delete(0, END)
                                    e_3_3.delete(0, END)
                                    e_4_3.delete(0, END)
                                    e_5_3.delete(0, END)
                                    e_1_4.delete(0, END)
                                    e_2_4.delete(0, END)
                                    e_3_4.delete(0, END)
                                    e_4_4.delete(0, END)
                                    e_5_4.delete(0, END)
                                    e_1_5.delete(0, END)
                                    e_2_5.delete(0, END)
                                    e_3_5.delete(0, END)
                                    e_4_5.delete(0, END)
                                    e_5_5.delete(0, END)

    except :
        # ERROR MESSAGE BOX
        messagebox.showerror(" ERROR ", "INPUT MUST BE A INTEGER")
    
#################################################################################################################################### GET FIRST MATRIX



######################################################################### OPERATION FUNCTIONS
### PLUS
def plus():
    global action
    
    action = "addition"

    get_first_matrix()

    
### MINUS
def minus():
    global action

    action = "substraction"

    get_first_matrix()


### MULTIPLY
def multiply():
    global action
    action = "multiplication"

    get_first_matrix()


########################################################################## OPERATION FUNCTIONS



####################################################################################################################### EQUAL
def equal():
    try :
        ################################################ COLUMN 1
        if columns == 1 :

            if rows == 1 :
                second_matrix = np.array([e_1_1.get()], dtype = int)
            else :

                if rows == 2 :
                    second_matrix = np.array([[e_1_1.get()], 
                                            [e_1_2.get()]], dtype = int)
                else :

                    if rows == 3 :
                        second_matrix = np.array([[e_1_1.get()], 
                                                [e_1_2.get()],
                                                [e_1_3.get()]], dtype = int)
                    else : 

                        if rows == 4 :
                            second_matrix = np.array([[e_1_1.get()], 
                                                    [e_1_2.get()],
                                                    [e_1_3.get()],
                                                    [e_1_4.get()]], dtype = int)
                        else :
                            
                            if rows == 5 :
                                second_matrix = np.array([[e_1_1.get()], 
                                                        [e_1_2.get()],
                                                        [e_1_3.get()],
                                                        [e_1_4.get()],
                                                        [e_1_5.get()]], dtype = int)

        
        
        ################################################ COLUMN 2
        if columns == 2 :

            if rows == 1 :
                second_matrix = np.array([e_1_1.get(), e_2_1.get()], dtype = int)
            else :
                
                if rows == 2 :
                    second_matrix = np.array([[e_1_1.get(), e_2_1.get()], 
                                            [e_1_2.get(), e_2_2.get()]], dtype = int)
                else :
                    
                    if rows == 3 :
                        second_matrix = np.array([[e_1_1.get(), e_2_1.get()], 
                                                [e_1_2.get(), e_2_2.get()],
                                                [e_1_3.get(), e_2_3.get()]], dtype = int)
                    else :
                        
                        if rows == 4 :
                            second_matrix = np.array([[e_1_1.get(), e_2_1.get()], 
                                                    [e_1_2.get(), e_2_2.get()],
                                                    [e_1_3.get(), e_2_3.get()],
                                                    [e_1_4.get(), e_1_4.get()]], dtype = int)
                        else :

                            if rows == 5 :
                                second_matrix = np.array([[e_1_1.get(), e_2_1.get()], 
                                                        [e_1_2.get(), e_2_2.get()],
                                                        [e_1_3.get(), e_2_3.get()],
                                                        [e_1_4.get(), e_2_4.get()],
                                                        [e_1_5.get(), e_2_5.get()]], dtype = int)



        ################################################ COLUMN 3
        if columns == 3 :

            if rows == 1 :
                second_matrix = np.array([e_1_1.get(), e_2_1.get(), e_3_1.get()], dtype = int)
            else :
                
                if rows == 2 :
                    second_matrix = np.array([[e_1_1.get(), e_2_1.get(), e_3_1.get()], 
                                            [e_1_2.get(), e_2_2.get(), e_3_2.get()]], dtype = int)
                else :
                    
                    if rows == 3 :
                        second_matrix = np.array([[e_1_1.get(), e_2_1.get(), e_3_1.get()], 
                                                [e_1_2.get(), e_2_2.get(), e_3_2.get()],
                                                [e_1_3.get(), e_2_3.get(), e_3_3.get()]], dtype = int)
                    else :
                        
                        if rows == 4 :
                            second_matrix = np.array([[e_1_1.get(), e_2_1.get(), e_3_1.get()], 
                                                    [e_1_2.get(), e_2_2.get(), e_3_2.get()],
                                                    [e_1_3.get(), e_2_3.get(), e_3_3.get()],
                                                    [e_1_4.get(), e_2_4.get(), e_3_4.get()]], dtype = int)
                        else :

                            if rows == 5 :
                                second_matrix = np.array([[e_1_1.get(), e_2_1.get(), e_3_1.get()], 
                                                        [e_1_2.get(), e_2_2.get(), e_3_1.get()],
                                                        [e_1_3.get(), e_2_3.get(), e_3_3.get()],
                                                        [e_1_4.get(), e_2_4.get(), e_3_4.get()],
                                                        [e_1_5.get(), e_2_5.get(), e_3_5.get()]], dtype = int)



        ################################################ COLUMN 4
        if columns == 4 :

            if rows == 1 :
                second_matrix = np.array([e_1_1.get(), e_2_1.get(), e_3_1.get(), e_4_1.get()], dtype = int)
            else :
                
                if rows == 2 :
                    second_matrix = np.array([[e_1_1.get(), e_2_1.get(), e_3_1.get(), e_4_1.get()], 
                                            [e_1_2.get(), e_2_2.get(), e_3_2.get(), e_4_2.get()]], dtype = int)
                else :
                    
                    if rows == 3 :
                        second_matrix = np.array([[e_1_1.get(), e_2_1.get(), e_3_1.get(), e_4_1.get()], 
                                                [e_1_2.get(), e_2_2.get(), e_3_2.get(), e_4_2.get()],
                                                [e_1_3.get(), e_2_3.get(), e_3_3.get(), e_4_3.get()]], dtype = int)
                    else :
                        
                        if rows == 4 :
                            second_matrix = np.array([[e_1_1.get(), e_2_1.get(), e_3_1.get(), e_4_1.get()], 
                                                    [e_1_2.get(), e_2_2.get(), e_3_2.get(), e_4_2.get()],
                                                    [e_1_3.get(), e_2_3.get(), e_3_3.get(), e_4_3.get()],
                                                    [e_1_4.get(), e_2_4.get(), e_3_4.get(), e_4_4.get()]], dtype = int)
                        else :

                            if rows == 5 :
                                second_matrix = np.array([[e_1_1.get(), e_2_1.get(), e_3_1.get(), e_4_1.get()], 
                                                        [e_1_2.get(), e_2_2.get(), e_3_1.get(), e_4_2.get()],
                                                        [e_1_3.get(), e_2_3.get(), e_3_3.get(), e_4_3.get()],
                                                        [e_1_4.get(), e_2_4.get(), e_3_4.get(), e_4_4.get()],
                                                        [e_1_5.get(), e_2_5.get(), e_3_5.get(), e_4_5.get()]], dtype = int)



        ################################################ COLUMN 5
        if columns == 5 :

            if rows == 1 :
                second_matrix = np.array([e_1_1.get(), e_2_1.get(), e_3_1.get(), e_4_1.get(), e_5_1.get()], dtype = int)
            else :
                
                if rows == 2 :
                    second_matrix = np.array([[e_1_1.get(), e_2_1.get(), e_3_1.get(), e_4_1.get(), e_5_1.get()], 
                                            [e_1_2.get(), e_2_2.get(), e_3_2.get(), e_4_2.get(), e_5_2.get()]], dtype = int)
                else :
                    
                    if rows == 3 :
                        second_matrix = np.array([[e_1_1.get(), e_2_1.get(), e_3_1.get(), e_4_1.get(), e_5_1.get()], 
                                                [e_1_2.get(), e_2_2.get(), e_3_2.get(), e_4_2.get(), e_5_2.get()],
                                                [e_1_3.get(), e_2_3.get(), e_3_3.get(), e_4_3.get(), e_5_3.get()]], dtype = int)
                    else :
                        
                        if rows == 4 :
                            second_matrix = np.array([[e_1_1.get(), e_2_1.get(), e_3_1.get(), e_4_1.get(), e_5_1.get()], 
                                                    [e_1_2.get(), e_2_2.get(), e_3_2.get(), e_4_2.get(), e_5_2.get()],
                                                    [e_1_3.get(), e_2_3.get(), e_3_3.get(), e_4_3.get(), e_5_3.get()],
                                                    [e_1_4.get(), e_2_4.get(), e_3_4.get(), e_4_4.get(), e_5_4.get()]], dtype = int)
                        else :

                            if rows == 5 :
                                second_matrix = np.array([[e_1_1.get(), e_2_1.get(), e_3_1.get(), e_4_1.get(), e_5_1.get()], 
                                                        [e_1_2.get(), e_2_2.get(), e_3_1.get(), e_4_2.get(), e_5_2.get()],
                                                        [e_1_3.get(), e_2_3.get(), e_3_3.get(), e_4_3.get(), e_5_3.get()],
                                                        [e_1_4.get(), e_2_4.get(), e_3_4.get(), e_4_4.get(), e_5_4.get()],
                                                        [e_1_5.get(), e_2_5.get(), e_3_5.get(), e_4_5.get(), e_5_5.get()]], dtype = int)


    except : 
        # ERROR MESSAGE BOX
        messagebox.showerror(" ERROR ", "INPUT MUST BE A INTEGER")
        
        
    global equal_no
    equal_no =+ 1

    global answer

    global answer_label

    delete()
    
    answer_label.destroy()
    

    if action == "addition" :
        answer = first_matrix + second_matrix
        
        answer = str(answer)
        
        answer = answer.replace("[", "")
        answer = answer.replace("]", "")
        
        answer_label = Label(root, text = answer, font = ("Courier New", 40))
        answer_label.grid(row = 3, column = 2, columnspan = 2, padx = (90, 100))

        


    else :
        
        if action == "substraction" :
            answer = first_matrix - second_matrix
            answer = str(answer)
        
            answer = answer.replace("[", "")
            answer = answer.replace("]", "")
            

            answer_label = Label(root, text = answer, font = ("Courier New", 40))
            answer_label.grid(row = 3, column = 2, columnspan = 2, padx = (90, 100))
        else :

            if action == "multiplication" : 
                try :
                    answer = first_matrix.dot(second_matrix)
                    answer = str(answer)
        
                    answer = answer.replace("[", "")
                    answer = answer.replace("]", "")
                    

                    answer_label = Label(root, text = answer, font = ("Courier New", 40))
                    answer_label.grid(row = 3, column = 2, columnspan = 2, padx = (90, 100))

                except  :
                    # ERROR MESSAGE BOX
                    messagebox.showerror(" ERROR ", "INVALID DIMENSION FOR MULTIPLICATION")

                    answer_label.destroy()

                    ################################################ COLUMN 1
                    if columns == 1 :

                        if rows == 1 :
                            e_1_1.delete(0, END)
                        else :

                            if rows == 2 :
                                e_1_1.delete(0, END)
                                e_1_2.delete(0, END)
                            else :

                                if rows == 3 :
                                    e_1_1.delete(0, END)
                                    e_1_2.delete(0, END)
                                    e_1_3.delete(0, END)
                                else:

                                    if rows == 4 :

                                        e_1_1.delete(0, END)
                                        e_1_2.delete(0, END)
                                        e_1_3.delete(0, END)
                                        e_1_4.delete(0, END)
                                    else:

                                        if rows == 5 :
                                            e_1_1.delete(0, END)
                                            e_1_2.delete(0, END)
                                            e_1_3.delete(0, END)
                                            e_1_4.delete(0, END)
                                            e_1_5.delete(0, END)
                                        

                                            
                    ################################################ COLUMN 2
                    if columns == 2 :

                        if rows == 1 :
                            e_1_1.delete(0, END)
                            e_1_2.delete(0, END)
                        else:

                            if rows == 2 :
                                e_1_1.delete(0, END)
                                e_2_1.delete(0, END)
                                e_1_2.delete(0, END)
                                e_2_2.delete(0, END)
                            else :

                                if rows == 3 :
                                    e_1_1.delete(0, END)
                                    e_1_2.delete(0, END)
                                    e_1_2.delete(0, END)
                                    e_2_2.delete(0, END)
                                    e_1_3.delete(0, END)
                                    e_2_3.delete(0, END)
                                else :

                                    if rows == 4 :
                                        e_1_1.delete(0, END)
                                        e_1_2.delete(0, END)
                                        e_1_2.delete(0, END)
                                        e_2_2.delete(0, END)
                                        e_1_3.delete(0, END)
                                        e_2_3.delete(0, END)
                                        e_1_4.delete(0, END)
                                        e_2_4.delete(0, END)
                                    else:

                                        if rows == 5 :
                                            e_1_1.delete(0, END)
                                            e_1_2.delete(0, END)
                                            e_1_2.delete(0, END)
                                            e_2_2.delete(0, END)
                                            e_1_3.delete(0, END)
                                            e_2_3.delete(0, END)
                                            e_1_4.delete(0, END)
                                            e_2_4.delete(0, END)
                                            e_1_5.delete(0, END)
                                            e_2_5.delete(0, END)



                    ################################################ COLUMN 3
                    if columns == 3 :

                        if rows == 1 :
                            e_1_1.delete(0, END)
                            e_2_1.delete(0, END)
                            e_3_1.delete(0, END)
                        else :

                            if rows == 2 :
                                e_1_1.delete(0, END)
                                e_2_1.delete(0, END)
                                e_3_1.delete(0, END)
                                e_1_2.delete(0, END)
                                e_2_2.delete(0, END)
                                e_3_2.delete(0, END)
                            else :

                                if rows == 3 :
                                    e_1_1.delete(0, END)
                                    e_2_1.delete(0, END)
                                    e_3_1.delete(0, END)
                                    e_1_2.delete(0, END)
                                    e_2_2.delete(0, END)
                                    e_3_2.delete(0, END)
                                    e_1_3.delete(0, END)
                                    e_2_3.delete(0, END)
                                    e_3_3.delete(0, END)
                                else :

                                    if rows == 4 :
                                        e_1_1.delete(0, END)
                                        e_2_1.delete(0, END)
                                        e_3_1.delete(0, END)
                                        e_1_2.delete(0, END)
                                        e_2_2.delete(0, END)
                                        e_3_2.delete(0, END)
                                        e_1_3.delete(0, END)
                                        e_2_3.delete(0, END)
                                        e_3_3.delete(0, END)
                                        e_1_4.delete(0, END)
                                        e_2_4.delete(0, END)
                                        e_3_4.delete(0, END)
                                    else :
                                        if rows == 5 : 
                                            e_1_1.delete(0, END)
                                            e_2_1.delete(0, END)
                                            e_3_1.delete(0, END)
                                            e_1_2.delete(0, END)
                                            e_2_2.delete(0, END)
                                            e_3_2.delete(0, END)
                                            e_1_3.delete(0, END)
                                            e_2_3.delete(0, END)
                                            e_3_3.delete(0, END)
                                            e_1_4.delete(0, END)
                                            e_2_4.delete(0, END)
                                            e_3_4.delete(0, END)
                                            e_1_5.delete(0, END)
                                            e_2_5.delete(0, END)
                                            e_3_5.delete(0, END)

                        

                    ################################################ COLUMN 4
                    if columns == 4 :

                        if rows == 1 :
                            e_1_1.delete(0, END)
                            e_2_1.delete(0, END)
                            e_3_1.delete(0, END)
                            e_4_1.delete(0, END)
                        else:

                            if rows == 2 :
                                e_1_1.delete(0, END)
                                e_2_1.delete(0, END)
                                e_3_1.delete(0, END)
                                e_4_1.delete(0, END)
                                e_1_2.delete(0, END)
                                e_2_2.delete(0, END)
                                e_3_2.delete(0, END)
                                e_4_2.delete(0, END)
                            else :

                                if rows == 3 :
                                    e_1_1.delete(0, END)
                                    e_2_1.delete(0, END)
                                    e_3_1.delete(0, END)
                                    e_4_1.delete(0, END)
                                    e_1_2.delete(0, END)
                                    e_2_2.delete(0, END)
                                    e_3_2.delete(0, END)
                                    e_4_2.delete(0, END)
                                    e_1_3.delete(0, END)
                                    e_2_3.delete(0, END)
                                    e_3_3.delete(0, END)
                                    e_4_3.delete(0, END)
                                else :

                                    if rows == 4 :
                                        e_1_1.delete(0, END)
                                        e_2_1.delete(0, END)
                                        e_3_1.delete(0, END)
                                        e_4_1.delete(0, END)
                                        e_1_2.delete(0, END)
                                        e_2_2.delete(0, END)
                                        e_3_2.delete(0, END)
                                        e_4_2.delete(0, END)
                                        e_1_3.delete(0, END)
                                        e_2_3.delete(0, END)
                                        e_3_3.delete(0, END)
                                        e_4_3.delete(0, END)
                                        e_1_4.delete(0, END)
                                        e_2_4.delete(0, END)
                                        e_3_4.delete(0, END)
                                        e_4_4.delete(0, END)
                                    else :

                                        if rows == 5 :
                                            e_1_1.delete(0, END)
                                            e_2_1.delete(0, END)
                                            e_3_1.delete(0, END)
                                            e_4_1.delete(0, END)
                                            e_1_2.delete(0, END)
                                            e_2_2.delete(0, END)
                                            e_3_2.delete(0, END)
                                            e_4_2.delete(0, END)
                                            e_1_3.delete(0, END)
                                            e_2_3.delete(0, END)
                                            e_3_3.delete(0, END)
                                            e_4_3.delete(0, END)
                                            e_1_4.delete(0, END)
                                            e_2_4.delete(0, END)
                                            e_3_4.delete(0, END)
                                            e_4_4.delete(0, END)
                                            e_1_5.delete(0, END)
                                            e_2_5.delete(0, END)
                                            e_3_5.delete(0, END)
                                            e_4_5.delete(0, END)



                    ################################################ COLUMN 5
                    if columns == 5 :

                        if rows == 1 :
                            e_1_1.delete(0, END)
                            e_2_1.delete(0, END)
                            e_3_1.delete(0, END)
                            e_4_1.delete(0, END)
                            e_5_1.delete(0, END)
                        else :

                            if rows == 2 :
                                e_1_1.delete(0, END)
                                e_2_1.delete(0, END)
                                e_3_1.delete(0, END)
                                e_4_1.delete(0, END)
                                e_5_1.delete(0, END)
                                e_1_2.delete(0, END)
                                e_2_2.delete(0, END)
                                e_3_2.delete(0, END)
                                e_4_2.delete(0, END)
                                e_5_2.delete(0, END)
                            else :
                                if rows == 3 :

                                    e_1_1.delete(0, END)
                                    e_2_1.delete(0, END)
                                    e_3_1.delete(0, END)
                                    e_4_1.delete(0, END)
                                    e_5_1.delete(0, END)
                                    e_1_2.delete(0, END)
                                    e_2_2.delete(0, END)
                                    e_3_2.delete(0, END)
                                    e_4_2.delete(0, END)
                                    e_5_2.delete(0, END)
                                    e_1_3.delete(0, END)
                                    e_2_3.delete(0, END)
                                    e_3_3.delete(0, END)
                                    e_4_3.delete(0, END)
                                    e_5_3.delete(0, END)
                                else :

                                    if rows == 4 :
                                        e_1_1.delete(0, END)
                                        e_2_1.delete(0, END)
                                        e_3_1.delete(0, END)
                                        e_4_1.delete(0, END)
                                        e_5_1.delete(0, END)
                                        e_1_2.delete(0, END)
                                        e_2_2.delete(0, END)
                                        e_3_2.delete(0, END)
                                        e_4_2.delete(0, END)
                                        e_5_2.delete(0, END)
                                        e_1_3.delete(0, END)
                                        e_2_3.delete(0, END)
                                        e_3_3.delete(0, END)
                                        e_4_3.delete(0, END)
                                        e_5_3.delete(0, END)
                                        e_1_4.delete(0, END)
                                        e_2_4.delete(0, END)
                                        e_3_4.delete(0, END)
                                        e_4_4.delete(0, END)
                                        e_5_4.delete(0, END)
                                    else :

                                        if rows == 5 :
                                            e_1_1.delete(0, END)
                                            e_2_1.delete(0, END)
                                            e_3_1.delete(0, END)
                                            e_4_1.delete(0, END)
                                            e_5_1.delete(0, END)
                                            e_1_2.delete(0, END)
                                            e_2_2.delete(0, END)
                                            e_3_2.delete(0, END)
                                            e_4_2.delete(0, END)
                                            e_5_2.delete(0, END)
                                            e_1_3.delete(0, END)
                                            e_2_3.delete(0, END)
                                            e_3_3.delete(0, END)
                                            e_4_3.delete(0, END)
                                            e_5_3.delete(0, END)
                                            e_1_4.delete(0, END)
                                            e_2_4.delete(0, END)
                                            e_3_4.delete(0, END)
                                            e_4_4.delete(0, END)
                                            e_5_4.delete(0, END)
                                            e_1_5.delete(0, END)
                                            e_2_5.delete(0, END)
                                            e_3_5.delete(0, END)
                                            e_4_5.delete(0, END)
                                            e_5_5.delete(0, END)


    
    

    
    
    
    



################################################################################################################################ EQUAL








##################################################################################### OPERATION BUTTONS
### PLUS BUTTON
# PLUS BUTTON SIGN
plus_sign = ImageTk.PhotoImage(Image.open("/Users/jonathan/Desktop/python/python_pics/plus_sign.png"))

# BUTTON
plus_button = Button(root, image = plus_sign, command = plus)
plus_button.grid(row = 7, column = 1)


### MINUS BUTTON
# MINUS BUTTON SIGN
minus_sign = ImageTk.PhotoImage(Image.open("/Users/jonathan/Desktop/python/python_pics/minus_sign.png"))

# BUTTON
minus_button = Button(root, image = minus_sign, command = minus)
minus_button.grid(row = 7, column = 2)


### MINUS BUTTON
# MINUS BUTTON SIGN
multiply_sign = ImageTk.PhotoImage(Image.open("/Users/jonathan/Desktop/python/python_pics/multiply_sign.png"))

# BUTTON
minus_button = Button(root, image = multiply_sign, command = multiply)
minus_button.grid(row = 7, column = 3)


### EQUAL BUTTON
# EQUAL BUTTON SIGN
equal_sign = ImageTk.PhotoImage(Image.open("/Users/jonathan/Desktop/python/python_pics/equal_sign.png"))

# BUTTON
equal_button = Button(root, image = equal_sign, command = equal)
equal_button.grid(row = 7, column = 4)



##################################################################################### OPERATION BUTTONS





############################################################################################### OPTION MENU
# GET DIMENSIONS
#### GET ROWS
# DEF GET ROWS
def get_rows(event):
    global rows
    rows = rows_var.get()
    rows = int(rows)
    
    
    delete()
    delete_canvas()
    # PUT CANVAS ON SCREEN
    create_canvas()
    
    # PUT ENTRYS ON THE SCREEN
    number_of_entrys()

    
   

    
# ROWS OPTIONMENU
rows_var = StringVar()
rows_var.set("  0  ")
get_rows = OptionMenu(root, rows_var, "  1  ", "  2  ", "  3  ", "  4  ", "  5  ", command = get_rows)
get_rows.grid(row = 0, column = 2)

# ROWS LABEL
rows_label = Label(root, text = "Rows : ", font = ("Courier New", 20))
rows_label.grid(row = 0, column = 1)

#### GET COLUMNS
# DEF GET COLUMNS
def get_columns(event):
    global columns
    columns = columns_var.get()
    columns = int(columns)
   
    delete()
    delete_canvas()
    # PUT CANVAS ON SCREEN
    create_canvas()
    
    # PUT ENTRYS ON THE SCREEN
    number_of_entrys()

    


# COLUMNS OPTIONMENU
columns_var = StringVar()
columns_var.set("  0  ")
get_columns = OptionMenu(root, columns_var, "  1  ", "  2  ", "  3  ", "  4  ", "  5  ", command = get_columns)
get_columns.grid(row = 0, column = 4)

# COLUMNS LABEL
columns_label = Label(root, text = "Columns : ", font = ("Courier New", 20))
columns_label.grid(row = 0, column = 3)

############################################################################################### OPTION MENU




root.mainloop()
