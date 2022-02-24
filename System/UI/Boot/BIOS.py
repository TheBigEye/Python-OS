from tkinter import Label, Misc

from System.Utils.Colormap import High_blue
from System.Utils.Utils import Asset

__author__ = 'TheBigEye'
__version__ = '1.5'

def BIOS(master: Misc | None = ...):  # Display the Bios window

    global Bios_Advanced_GUI

    master.configure(background=High_blue)  # Set the background color to blue

    Bios_Advanced_GUI = Asset("BIOS_Advanced_GUI.png")
    Bios_GUI = Label(master, image=Bios_Advanced_GUI, borderwidth=0.1)
    Bios_GUI.place(x=0, y=0)
