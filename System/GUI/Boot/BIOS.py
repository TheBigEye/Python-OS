from System.Utils.Colormap import High_blue
from tkinter import Label, PhotoImage

__author__ = 'TheBigEye'
__version__ = '1.5'

def BIOS(master):  # Display the Bios window

    global Bios_Advanced_GUI

    master.configure(background=High_blue)  # Sets the background to Blue

    Bios_Advanced_GUI = PhotoImage(file="Assets/GUI/BIOS_Advanced_GUI.png")
    Bios_GUI = Label(master, image=Bios_Advanced_GUI, borderwidth=0.1)
    Bios_GUI.place(x=0, y=0)