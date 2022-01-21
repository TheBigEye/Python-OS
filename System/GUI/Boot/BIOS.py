from System.Utils.Colormap import High_blue
from tkinter import Label, Misc, PhotoImage
from System.Utils.Utils import get_asset

__author__ = 'TheBigEye'
__version__ = '1.5'

def BIOS(master: Misc | None = ...):  # Display the Bios window

    global Bios_Advanced_GUI

    master.configure(background=High_blue)  # Establece el fondo en azul

    Bios_Advanced_GUI = get_asset("Assets/GUI/BIOS_Advanced_GUI.png")
    Bios_GUI = Label(master, image=Bios_Advanced_GUI, borderwidth=0.1)
    Bios_GUI.place(x=0, y=0)