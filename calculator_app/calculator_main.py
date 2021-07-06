from tkinter import *   
import math
import locale
from subprocess import call


root = Tk()
root.title("calculator")



# ENTRY
entry = Entry(root, width = 14, borderwidth = 5, font = ("Courier New", 40))
entry.grid(row = 0, column = 0, columnspan = 5)


# KEYPAD
def button_click(number):
    current = entry.get()
    entry.delete(0,END)
    current_n = str(current) + str(number)

    if len(current_n) > 3 :
        current_n = current_n.replace(",", "")

    current_n = int(current_n)

    locale.setlocale(locale.LC_ALL, '')
        
    current_n = f'{current_n:n}'
    entry.insert(0,current_n)


# OPERATION BUTTONS
def button_clear():
    entry.delete(0,END)

def button_add():
    first_number = entry.get()
    
    if len(first_number) > 3 :
        first_number = first_number.replace(",", "")

    global f_numb
    global action
    action = "add"
    f_numb = float(first_number)
    entry.delete(0, END)
    
def button_substract():
    first_number = entry.get()
    
    if len(first_number) > 3 :
        first_number = first_number.replace(",", "")
    
    global f_numb
    global action
    action = "substract"
    f_numb = float(first_number)
    entry.delete(0, END)

def button_multiply():
    first_number = entry.get()
    
    if len(first_number) > 3 :
        first_number = first_number.replace(",", "")
    
    global f_numb
    global action
    action = "multiply"
    f_numb = float(first_number)
    entry.delete(0, END)

def button_divide():
    first_number = entry.get()
    
    if len(first_number) > 3 :
        first_number = first_number.replace(",", "")
    
    global f_numb
    global action
    action ="divide"
    f_numb = float(first_number)
    entry.delete(0, END)

def button_sqrt():
    first_number = entry.get()
    
    if len(first_number) > 3 :
        first_number = first_number.replace(",", "")
    
    global f_numb
    global action
    action = "sqrt"
    f_numb = float(first_number)
    
def button_power_to():
    first_number = entry.get()
    
    if len(first_number) > 3 :
        first_number = first_number.replace(",", "")
    
    global f_numb
    global action
    action = "power_to"
    f_numb = float(first_number)
    entry.delete(0, END)

def button_percent():
    first_number = entry.get()
    
    if len(first_number) > 3 :
        first_number = first_number.replace(",", "")
    
    global f_numb
    global action
    action = "percent"
    f_numb = float(first_number)
    entry.delete(0, END)

def button_pi():
    first_number = entry.get()
    
    if len(first_number) > 3 :
        first_number = first_number.replace(",", "")
    
    global f_numb
    global action
    action ="pi"
    f_numb = float(first_number)
    
def button_comma():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0,str(current) + "." )

def button_cuberoot():
    first_number = entry.get()
    
    if len(first_number) > 3 :
        first_number = first_number.replace(",", "")
    
    global f_numb
    global action
    action = "cuberoot"
    f_numb = float(first_number)

def button_power_2():
    first_number = entry.get()
    
    if len(first_number) > 3 :
        first_number = first_number.replace(",", "")
    
    global f_numb
    global action
    action = "power_2"
    f_numb = float(first_number)

def button_power_3():
    first_number = entry.get()
    
    if len(first_number) > 3 :
        first_number = first_number.replace(",", "")
    
    global f_numb
    global action
    action = "power_3"
    f_numb = float(first_number)

def button_10_power():
    first_number = entry.get()
    
    if len(first_number) > 3 :
        first_number = first_number.replace(",", "")
    
    global f_numb
    global action
    action = "10_power"
    f_numb = float(first_number)
    entry.delete(0, END)

def button_sin():
    first_number = entry.get()
    
    if len(first_number) > 3 :
        first_number = first_number.replace(",", "")
    
    global f_numb
    global action
    action = "sin"
    f_numb = float(first_number)

def button_cos():
    first_number = entry.get()
    
    if len(first_number) > 3 :
        first_number = first_number.replace(",", "")
    
    global f_numb
    global action
    action = "cos"
    f_numb = float(first_number)

def button_tan():
    first_number = entry.get()
    
    if len(first_number) > 3 :
        first_number = first_number.replace(",", "")
    
    global f_numb
    global action
    action = "tan"
    f_numb = float(first_number)

def button_equal():
    second_number = entry.get()
    
    if len(second_number) > 3 :
        second_number = second_number.replace(",", "")
    
    entry.delete(0, END)
    
    if action == "add" :
        answer = f_numb + float(second_number)
    else :

        if action == "substract" :
            answer = f_numb - float(second_number)
        else :

            if action == "multiply" :
                answer = f_numb * float(second_number)
            else :

                if action == "divide" :
                    answer = f_numb / float(second_number)
                else :

                    if action == "sqrt" :
                        answer = math.sqrt(f_numb)
                    else :

                        if action == "power_to" :
                            answer = f_numb ** float(second_number)
                        else :

                            if action == "percent" :
                                answer = f_numb / 100
                            else :

                                if action == "pi" :
                                    answer = f_numb * 22/7
                                else :

                                    if action == "cuberoot" :
                                        answer = round(f_numb ** (1/3.), 2)
                                    else :

                                        if action == "power_2" :
                                            answer = f_numb ** 2
                                        else :

                                            if action == "power_3" :
                                                answer = f_numb ** 3
                                            else :

                                                if action == "10_power":
                                                    answer = f_numb * 10 ** float(second_number)
                                                else :

                                                    if action == "sin" :
                                                        answer = math.sin(math.radians(f_numb))
                                                    else :

                                                        if action == "cos" :
                                                            answer = math.cos(math.radians(f_numb))
                                                        else :

                                                            if action == "tan" :
                                                                if f_numb == 90 :
                                                                    answer = "UNDEF"
                                                                else :
                                                                    answer = math.tan(math.radians(f_numb))
    
    # CHECK IF ANS IS INT OR FLOAT
    answer_s = (answer).is_integer()

    # IF ANS IS INT
    if answer_s == True :
        answer = str(answer)
        answer_l = len(answer)

        answer_ = answer_l - 2

        answer = answer.replace(answer[answer_:], "")

        locale.setlocale(locale.LC_ALL, '')

        answer = int(answer)
        
        answer = f'{answer:n}'

        entry.insert(0, answer)
    else :
        
        # IF ANS IS FLOAT
        if answer_s == False :
            
            locale.setlocale(locale.LC_ALL, '')
        
            answer = f'{answer:n}'
            
            entry.insert(0, answer)

# MORE BUTTONS FUNCTION
def more_buttons():
    # RESIZE THE ENTRY
    entry = Entry(root, width = 22, borderwidth = 5, font = ("Courier New", 40))
    entry.grid(row = 0, column = 0, columnspan = 6)
    
    # BUTTONS
    global button_power_to
    button_power_to = Button(root, text = "^", padx = 35, pady = 24, font = ("Courier New", 30), command=button_power_to)
    button_power_to.grid(row = 1, column = 4)
    
    global button_power_2
    button_power_2 = Button(root, text = "x²" , padx = 26, pady = 24, font = ("Courier New", 30), command = button_power_2)
    button_power_2.grid(row = 2, column = 4)

    global button_power_3
    button_power_3 = Button(root, text = "x³" , padx = 26, pady = 24, font = ("Courier New", 30), command = button_power_3)
    button_power_3.grid(row = 3, column = 4)

    global button_sqrt
    button_sqrt = Button(root, text = "√", padx = 35, pady = 24, font = ("Courier New", 30), command = button_sqrt)
    button_sqrt.grid(row = 4, column = 4)

    global button_cuberoot
    button_cuberoot = Button(root, text = "∛" , padx = 35, pady = 24, font = ("Courier New", 30), command = button_cuberoot)
    button_cuberoot.grid(row = 5, column = 4)

    global button_pi
    button_pi = Button(root, text = "π", padx = 35, pady = 24, font = ("Courier New", 30), command = button_pi)
    button_pi.grid(row = 1, column = 5)

    global button_10_power
    button_10_power = Button(root, text = "10^x", padx = 8, pady = 24, font = ("Courier New", 30), command = button_10_power)
    button_10_power.grid(row = 2, column = 5)

    global button_sin
    button_sin = Button(root, text = "Sin", padx = 17, pady = 24, font = ("Courier New", 30), command = button_sin)
    button_sin.grid(row = 3, column = 5)

    global button_cos
    button_cos = Button(root, text = "Cos", padx = 17, pady = 24, font = ("Courier New", 30), command = button_cos)
    button_cos.grid(row = 4, column = 5)

    global button_tan
    button_sin = Button(root, text = "Tan", padx = 17, pady = 24, font = ("Courier New", 30), command = button_tan)
    button_sin.grid(row = 5, column = 5)


    
# BUTTONS
# NUMBER BUTTONS
button_1 = Button(root, text = "1", padx = 35, pady = 24, font = ("Courier New", 30), command = lambda: button_click(1))
button_1.grid(row = 4, column = 0)

button_2=Button(root, text= "2", padx = 35, pady = 24, font = ("Courier New", 30), command = lambda: button_click(2))
button_2.grid(row = 4, column = 1)

button_3 = Button(root, text = "3", padx = 35, pady = 24, font = ("Courier New", 30), command = lambda: button_click(3))
button_3.grid(row = 4, column = 2)

button_4 = Button(root, text = "4", padx = 35, pady = 24, font = ("Courier New", 30), command = lambda: button_click(4))
button_4.grid(row = 3, column = 0)

button_5 = Button(root, text = "5", padx = 35, pady = 24, font = ("Courier New", 30), command = lambda: button_click(5))
button_5.grid(row = 3, column = 1)

button_6 = Button(root, text = "6", padx = 35, pady = 24, font = ("Courier New", 30), command = lambda: button_click(6))
button_6.grid(row= 3, column = 2)
root
button_7 = Button(root, text = "7", padx = 35, pady = 24, font = ("Courier New", 30), command = lambda: button_click(7))
button_7.grid(row = 2, column = 0)

button_8 = Button(root, text = "8", padx = 35, pady = 24, font = ("Courier New", 30), command = lambda: button_click(8))
button_8.grid(row = 2, column = 1)

button_9=Button(root, text = "9", padx = 35, pady = 24, font = ("Courier New", 30), command = lambda: button_click(9))
button_9.grid(row = 2, column = 2)

button_0=Button(root, text = "0", padx = 82, pady = 24, font = ("Courier New", 30), command = lambda: button_click(0))
button_0.grid(row = 5, column = 0, columnspan = 2)

# OPERATION BUTTONS
button_add = Button(root, text = "+", padx = 35, pady = 24, font = ("Courier New", 30), command = button_add)
button_add.grid(row = 4, column = 3)

button_substract = Button(root, text = "-", padx = 35, pady = 24, font = ("Courier New", 30), command = button_substract)
button_substract.grid(row = 3, column = 3)

button_multiply = Button(root, text = "X", padx = 35, pady = 24, font = ("Courier New", 30), command = button_multiply)
button_multiply.grid(row = 2, column = 3)

button_divide = Button(root, text = "÷", padx = 35, pady = 24, font = ("Courier New", 30), command = button_divide)
button_divide.grid(row = 1, column = 3)

button_equal = Button(root, text = "=", padx = 35, pady = 24, font = ("Courier New", 30), command = button_equal)
button_equal.grid(row = 5, column = 3)

button_clear = Button(root, text="C", padx = 35, pady = 24, font = ("Courier New", 30), command = button_clear)
button_clear.grid(row = 1, column = 0)

button_comma = Button(root, text = ".", padx = 35, pady = 24, font = ("Courier New", 30), command = button_comma)
button_comma.grid(row = 5, column = 2)

button_percent = Button(root, text = "%", padx = 35, pady = 24, font = ("Courier New", 30), command = button_percent)
button_percent.grid(row = 1, column = 2)

# MORE BUTTON
more_button = Button(root, text = "M", padx = 35, pady = 24, font = ("Courier New", 30), command = more_buttons)
more_button.grid(row = 1, column = 1)


############################################################################ MENU BAR
def open_matrix():
    class CallPy(object):

        def __init__(self, path = "/Users/jonathan/Desktop/python/calculator_app/matrix.py") :
            self.path= path

        def call_python_file(self):
            call(["Python3", "{}".format(self.path)])



    if __name__== "__main__" :
        c = CallPy()
        c.call_python_file()

def open_arithmetic():
    class CallPy(object):

        def __init__(self, path = "/Users/jonathan/Desktop/python/calculator_app/arithmetic.py") :
            self.path= path

        def call_python_file(self):
            call(["Python3", "{}".format(self.path)])



    if __name__== "__main__" :
        c = CallPy()
        c.call_python_file()

def open_geometric_sequence():
    class CallPy(object):

        def __init__(self, path = "/Users/jonathan/Desktop/python/calculator_app/geometric_sequence.py") :
            self.path= path

        def call_python_file(self):
            call(["Python3", "{}".format(self.path)])



    if __name__== "__main__" :
        c = CallPy()
        c.call_python_file()

def open_statistics():
    class CallPy(object):

        def __init__(self, path = "/Users/jonathan/Desktop/python/calculator_app/mean_median_mode_range.py") :
            self.path= path

        def call_python_file(self):
            call(["Python3", "{}".format(self.path)])



    if __name__== "__main__" :
        c = CallPy()
        c.call_python_file()

def open_standard_deviation():
    class CallPy(object):

        def __init__(self, path = "/Users/jonathan/Desktop/python/calculator_app/standard_deviation.py") :
            self.path= path

        def call_python_file(self):
            call(["Python3", "{}".format(self.path)])



    if __name__== "__main__" :
        c = CallPy()
        c.call_python_file()

def open_pythagoras():
    class CallPy(object):

        def __init__(self, path = "/Users/jonathan/Desktop/python/calculator_app/pythagoras.py") :
            self.path= path

        def call_python_file(self):
            call(["Python3", "{}".format(self.path)])



    if __name__== "__main__" :
        c = CallPy()
        c.call_python_file()

def open_simple_interest():
    class CallPy(object):

        def __init__(self, path = "/Users/jonathan/Desktop/python/calculator_app/simple_interest.py") :
            self.path= path

        def call_python_file(self):
            call(["Python3", "{}".format(self.path)])



    if __name__== "__main__" :
        c = CallPy()
        c.call_python_file()

def open_compound_interest():
    class CallPy(object):

        def __init__(self, path = "/Users/jonathan/Desktop/python/calculator_app/compound_interest.py") :
            self.path= path

        def call_python_file(self):
            call(["Python3", "{}".format(self.path)])



    if __name__== "__main__" :
        c = CallPy()
        c.call_python_file()

def open_stock_intrinsic_value():
    class CallPy(object):

        def __init__(self, path = "/Users/jonathan/Desktop/python/calculator_app/stock_intrinsic_value.py") :
            self.path= path

        def call_python_file(self):
            call(["Python3", "{}".format(self.path)])



    if __name__== "__main__" :
        c = CallPy()
        c.call_python_file()

def open_factorize():
    class CallPy(object):

        def __init__(self, path = "/Users/jonathan/Desktop/python/calculator_app/factorize.py") :
            self.path= path

        def call_python_file(self):
            call(["Python3", "{}".format(self.path)])



    if __name__== "__main__" :
        c = CallPy()
        c.call_python_file()





# CREATE MENU BAR
menu_bar = Menu(root)
root.config(menu = menu_bar)

# ADD ITEMS TO MENU BAR
more = Menu(menu_bar)
menu_bar.add_cascade(label = "More", menu = more)

# ADD ITEMS TO OPTION MENU BAR
# MATRIX APP
more.add_command(label = "Matrix", command = open_matrix)

# ARITHMETIC APP
more.add_command(label = "Arithmetic", command = open_arithmetic)

# GEOMETRIC SEQUENCE APP
more.add_command(label = "Geometric Sequence", command = open_geometric_sequence)

# STATISTICS APP
more.add_command(label = "Statistics", command = open_statistics)

# STANDARD DEVIATION APP
more.add_command(label = "Standard Deviation", command = open_standard_deviation)

# PYTHAGORAS APP
more.add_command(label = "Pythagoras", command = open_pythagoras)

# SIMPLE INTEREST APP
more.add_command(label = "Simple Interest", command = open_simple_interest)

# COMPOUND INTEREST APP
more.add_command(label = "Simple Interest", command = open_compound_interest)

# STOCK INTRINSIC VALUE APP
more.add_command(label = "Stock Intrinsic Value", command = open_stock_intrinsic_value)

# FACTORIZE APP
more.add_command(label = "Factorize", command = open_factorize)

############################################################################ MENU BAR





 

root.mainloop()
