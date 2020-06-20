from tkinter import *
import pyttsx3


root = Tk()
root.geometry("400x210")



def speak():
    phrase = text.get()
    
    engine = pyttsx3.init()
    engine.say(phrase)

    engine.runAndWait()

    phrase.delete(0, END)

text = Entry(root, width = 13, font = ("Courier New", 40))
text.pack(pady = (20, 0))


speaker_ico = PhotoImage(file = "/Users/jonathan/Desktop/python/python_pics/speaker_ico.png")

speak_button = Button(root, image = speaker_ico, borderwidth = 0, command = speak)
speak_button.pack(pady = (20, 0))










root.mainloop()