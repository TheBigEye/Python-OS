from tkinter import Label, Misc

from Libs.pyImage.Image import Image

__author__ = 'TheBigEye'
__version__ = '1.5'

def BIOS(master: Misc):  # Display the Bios window

    global Bios_Advanced_GUI

    master.configure(background="#0000ff")  # Set the background color to blue

    Bios_Advanced_GUI = Image.setImage("Assets/Shell/Boot/BIOS/BIOS.png")
    Bios_GUI = Label(master, image=Bios_Advanced_GUI, borderwidth=0.1)
    Bios_GUI.place(x=0, y=0)
