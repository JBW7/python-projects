from tkinter import *
import pygame


root = Tk()
root.geometry("400x400")


pygame.mixer.init()


def play():
    pygame.mixer.music.load("python_pics/test_music_2.mp3")
    pygame.mixer.music.play(loops = 1)


button = Button(root, text = "Play Music", command = play)
button.pack()




root.mainloop()  