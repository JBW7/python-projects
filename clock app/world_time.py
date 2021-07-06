from tkinter import *
import  world_time_api



root = Tk()
root.title("WORLD CLOCK")
root.geometry("315x300")


# DISPLAY INTIAL TIME
world_time_api.initial_time()


# PICK LOCATION OPTIONMENU
locations = StringVar()
locations.set("Location")

# OPTION MENU
location = OptionMenu(root, locations, "America", "Asia", "Australia", "Europe", command = world_time_api.select)
location.grid(row = 1, column = 0)
'''
# SELECT BUTTON
select_button = Button(root, text = "Select", command = world_time_api.select)
select_button.grid(row = 2, column = 0)
'''

# CHANGE TIME FORMAT
# OPTION MENU
option = StringVar()
option.set("24 Hour")

hour_format = OptionMenu(root, option, "24 Hour", "12 Hour", command = world_time_api.change_formats)
hour_format.grid(row = 1, column = 1)
'''
# SET BUTTON
button = Button(root, text = "Set", command = world_time_api.change_format)
button.grid(row = 2, column = 1)
'''


root.resizable(0, 0)


root.mainloop()