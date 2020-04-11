from tkinter import *  


screen= Tk()
entry = Entry(screen, width=60, borderwidth=5)
entry.grid(row=0, column=0, columnspan=2

def button_mm():
    number = entry.get





button_mm=Button(screen, text="mm", padx=40, pady=20, command= button_mm) 
button_cm=Button(screen, text="cm", padx=40, pady=20, command= button_cm) 

button_mm.grid(row=1, column=0 )
button_cm.grid(row=1, column=1 )














screen.mainloop()