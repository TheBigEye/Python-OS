from System.Utils.Colormap import Black
from tkinter import Button, Entry, Label, PhotoImage
import time

from System.Utils.Utils import print_log

__author__ = 'TheBigEye'
__version__ = '2.0'


def Desktop(master):

 # Documentation ---------------------------------------------------------------------------------------------------------------

    """
    This function is used to create the desktop.

    Parameters
    ----------
    master : str
        The Tkinter object which is the parent of all widgets.

    Returns
    -------
        None
    """

  # ------------------------------------------------------[ Desktop ]----------------------------------------------------------------

    print_log("Desktop: Loaded desktop functions and running")    

    global Wallpaper, Desktop_wallpaper


    master.configure(background = Black)  # Sets the background to Blue

    Wallpaper = PhotoImage(file = "Assets/Wallpapers/BlissHill.png")
    Desktop_wallpaper = Label(master, image= Wallpaper, borderwidth="0.1")
    Desktop_wallpaper.place(x=0, y=0)


 # ------------------------------------------------------[ Taskbar ]----------------------------------------------------------------

    global Taskbar_GUI_Image, Taskbar

    Taskbar_GUI_Image = PhotoImage(file = "Assets/GUI/Taskbar.png") 

    Taskbar = Label(
        master,
        width = 1024,
        height = 29,
        borderwidth = "0",
        image = Taskbar_GUI_Image,
        background = "black",
        foreground = "gray",
        relief = "raised",
    )

    Taskbar.place(x= 0, y= 571)


 # -----------------------------------------------------[ Clockbar ]----------------------------------------------------------------

    global Clockbar

    Clockbar = Label(
        Taskbar,
        width=70,
        height=28,
        borderwidth="0",
        relief="raised",
        bg="#080D11",
    )

    Clockbar.place(x=950, y=1)


    def times():

        current_time = time.strftime("%H: %M")
        clock.config(bg="#080D11", text=current_time, fg="white", font=("Segou UI", 9))
        clock.after(1, times)


    clock = Label(Taskbar, borderwidth="0", relief="raised")
    clock.after(1, times)
    clock.place(x=965, y=6)  



    

