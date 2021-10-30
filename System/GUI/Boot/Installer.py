from tkinter import Label, PhotoImage
from System.Utils.Colormap import Low_blue

__author__ = 'TheBigEye'
__version__ = '1.5'

def Os_Installer(master):  # Display the Post-Bios window (coming soon the OOBE)

    global Post_Bios_GUI

    master.configure(background=Low_blue)  # Sets the background to Blue

    Post_Bios_GUI = PhotoImage(file="Assets/GUI/Post_BIOS.png")
    Post_Bios = Label(master, image=Post_Bios_GUI, borderwidth=0.1)
    Post_Bios.place(x=0, y=0)