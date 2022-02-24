from tkinter import Label

from System.Utils.Colormap import Black
from System.Utils.Utils import Asset

__author__ = 'TheBigEye'
__version__ = '2.1'

def BSOD(master):  # Display the Black screen of death

    global Black_screen_of_death_GUI

    master.configure(background=Black)  # Sets the background to Black

    Black_screen_of_death_GUI = Asset("BSOD.png")
    Black_screen_of_death = Label(master, image = Black_screen_of_death_GUI, borderwidth = 0.1)
    Black_screen_of_death.place(x = 0, y = 0)
