from tkinter import *   
import math


screen = Tk()
screen.title("calculator")
screen.geometry("473x457")


#entry
entry = Entry(screen, width=50, borderwidth=5)
entry.grid(row=0, column=0, columnspan=5)


#button function
def button_click(number):
    current= entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current) + str(number))

def button_clear():
    entry.delete(0,END)

def button_add():
    first_number = entry.get()
    global f_numb
    global action
    action="add"
    f_numb= float(first_number)
    entry.delete(0, END)
    
def button_substract():
    first_number = entry.get()
    global f_numb
    global action
    action="substract"
    f_numb= float(first_number)
    entry.delete(0, END)

def button_multiply():
    first_number = entry.get()
    global f_numb
    global action
    action="multiply"
    f_numb= float(first_number)
    entry.delete(0, END)

def button_divide():
    first_number = entry.get()
    global f_numb
    global action
    action="divide"
    f_numb= float(first_number)
    entry.delete(0, END)

def button_sqrt():
    first_number = entry.get()
    global f_numb
    global action
    action="sqrt"
    f_numb= float(first_number)
    
def button_power_to():
    first_number = entry.get()
    global f_numb
    global action
    action="power_to"
    f_numb= float(first_number)
    entry.delete(0, END)

def button_percent():
    first_number = entry.get()
    global f_numb
    global action
    action="percent"
    f_numb= float(first_number)
    entry.delete(0, END)

def button_pi():
    first_number = entry.get()
    global f_numb
    global action
    action="pi"
    f_numb= float(first_number)
    
def button_comma():
    current= entry.get()
    entry.delete(0, END)
    entry.insert(0,str(current) + "." )

def button_cuberoot():
    first_number = entry.get()
    global f_numb
    global action
    action="cuberoot"
    f_numb= float(first_number)

def button_power_2():
    first_number = entry.get()
    global f_numb
    global action
    action="power_2"
    f_numb= float(first_number)

def button_10_power():
    first_number = entry.get()
    global f_numb
    global action
    action="10_power"
    f_numb= float(first_number)
    entry.delete(0, END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, END)
    if action== "add":
        entry.insert(0,f_numb + float(second_number))
    if action== "substract":
        entry.insert(0,f_numb - float(second_number))
    if action== "multiply":
        entry.insert(0,f_numb * float(second_number))
    if action== "divide":
        entry.insert(0,f_numb / float(second_number))
    if action== "sqrt":
        entry.insert(0, math.sqrt(f_numb))
    if action== "power_to":
        entry.insert(0,f_numb ** float(second_number))
    if action== "percent":
        entry.insert(0,f_numb / 100)
    if action== "pi":
        entry.insert(0, f_numb * 22/7)
    if action == "cuberoot":
        entry.insert(0,round(f_numb ** (1/3.), 2))
    if action == "power_2" :
        entry.insert(0,f_numb ** 2)
    if action == "10_power":
        entry.insert (0, f_numb * 10 ** float(second_number))
  
   
#button
button_1=Button(screen, text="1", height = 5, width = 10, command=lambda: button_click(1))
button_2=Button(screen, text="2", height = 5, width = 10, command=lambda: button_click(2))
button_3=Button(screen, text="3", height = 5, width = 10, command=lambda: button_click(3))
button_4=Button(screen, text="4", height = 5, width = 10, command=lambda: button_click(4))
button_5=Button(screen, text="5", height = 5, width = 10, command=lambda: button_click(5))
button_6=Button(screen, text="6", height = 5, width = 10, command=lambda: button_click(6))
button_7=Button(screen, text="7", height = 5, width = 10, command=lambda: button_click(7))
button_8=Button(screen, text="8", height = 5, width = 10, command=lambda: button_click(8))
button_9=Button(screen, text="9", height = 5, width = 10, command=lambda: button_click(9))
button_0=Button(screen, text="0", height = 5, width = 10, command=lambda: button_click(0))
button_add=Button(screen, text="+", height = 5, width = 10, command=button_add)
button_substract=Button(screen, text="-", height = 5, width = 10, command=button_substract)
button_multiply=Button(screen, text="X", height = 5, width = 10, command=button_multiply)
button_divide=Button(screen, text="/", height = 5, width = 10, command=button_divide)
button_equal=Button(screen, text="=", height = 5, width = 10, command=button_equal)
button_clear=Button(screen, text="C", height = 5, width = 10, command=button_clear)
button_sqrt=Button(screen, text="√", height = 5, width = 10, command=button_sqrt)
button_power_to=Button(screen, text="^", height = 5, width = 10, command=button_power_to)
button_percent=Button(screen, text="%", height = 5, width = 10, command=button_percent)
button_pi=Button(screen, text="π", height = 5, width = 10, command=button_pi)
button_comma = Button(screen, text = ".", height = 5, width = 10, command = button_comma)
button_cuberoot = Button(screen, text = "∛" , height = 5, width = 10, command = button_cuberoot)
button_power_2 = Button(screen, text = "X^2" , height = 5, width = 10, command = button_power_2)
button_10_power = Button(screen, text = "10^x" , height = 5, width = 10, command = button_10_power)
button_quit = Button(screen, text = "EXIT" , height = 5, width = 10, command = screen.quit)


button_7.grid(row=1, column=0 )
button_8.grid(row=1, column=1 )
button_9.grid(row=1, column=2 )
button_add.grid(row=1, column=3)
button_sqrt.grid(row=1, column=4)

button_4.grid(row=2, column=0 )
button_5.grid(row=2, column=1 )
button_6.grid(row=2, column=2 )
button_substract.grid(row=2, column=3)
button_cuberoot.grid(row = 2, column = 4)

button_1.grid(row=3, column=0 )
button_2.grid(row=3, column=1 )
button_3.grid(row=3, column=2 )
button_multiply.grid(row=3, column=3)
button_power_2.grid(row = 3, column = 4)

button_0.grid(row=4, column=1 )
button_clear.grid(row=4, column=0)
button_equal.grid(row=4, column=2)
button_divide.grid(row=4, column=3)
button_10_power.grid(row = 4, column = 4)

button_comma.grid(row=5, column=0)
button_power_to.grid(row=5, column=1)
button_percent.grid(row=5, column=2)
button_pi.grid(row=5, column=3)
button_quit.grid(row = 5, column = 4)
 

screen.mainloop()
