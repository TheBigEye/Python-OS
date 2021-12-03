from System.Utils.Colormap import High_red
from tkinter import Label

from System.Utils.Utils import get_asset

__author__ = 'TheBigEye'
__version__ = '2.1'

def RSOD(master):  # Display the Red screen of death

    global Red_screen_of_death_GUI

    master.configure(background=High_red)  # Sets the background to Red

    Red_screen_of_death_GUI = get_asset("Assets/GUI/RSOD.png")
    Red_screen_of_death = Label(master, image = Red_screen_of_death_GUI, borderwidth = 0.1)
    Red_screen_of_death.place(x = 0, y = 0)