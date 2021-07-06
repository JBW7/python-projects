from tkinter import *
from tkinter import ttk
import time
import start_timer

root = Tk()
root.geometry("315x300")
root.title("TIMER")


    
##################################################################### ENTRYS + :
# SECONDS ENTRY
set_seconds = Entry(root, width = 2, font = ("times 20", 50), justify = CENTER)
set_seconds.insert(0, "0")
set_seconds.grid(row = 0, column = 4, pady = (60, 20))

# LABEL_:
label = Label(root, text = ":", font = ("times 20", 50))
label.grid(row = 0, column = 3, pady = (60, 20))

# MINUTES ENTRY
set_minutes = Entry(root, width = 2, font = ("times 20", 50), justify = CENTER)
set_minutes.insert(0, "0")
set_minutes.grid(row = 0, column = 2, pady = (60, 20))

# LABEL_:
label = Label(root, text = ":", font = ("times 20", 50))
label.grid(row = 0, column = 1, pady = (60, 20))
    
# HOURS ENTRY
set_hours = Entry(root, width = 2, font = ("times 20", 50), justify = CENTER)
set_hours.insert(0, "0")
set_hours.grid(row = 0, column = 0, pady = (60, 20), padx = (10, 0))
    

# START BUTTON
start_button = Button(root, text = "Start", font = ("times 20", 30), command = start_timer.convert_to_seconds)
start_button.grid(row = 1, column = 2)


# PROGRESS BAR
progress_bar = ttk.Progressbar(root, orient = "horizontal", length = 286, mode = 'determinate')
progress_bar.grid(row = 2, column = 0, columnspan = 5, pady = 20, padx = 5)


# PAUSE BUTTON
pause_button = Button(root, text = "Pause", font = ("times 20", 20), command = start_timer.pause_timer)


# RESUME BUTTON
resume_button = Button(root, text = "Resume", font = ("times 20", 20), command = start_timer.resume_timer)


# CANCEL BUTTON
cancel_button = Button(root, text = "Cancel", font = ("times 20", 20), command = start_timer.cancel_timer)


root.resizable(0, 0)


root.mainloop()