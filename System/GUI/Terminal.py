import os
from tkinter import Entry, Label, Button, PhotoImage, Text, Tk
from tkinter.constants import END, INSERT
import time
import random

from System.GUI.Attributes.Draggable import make_draggable
from System.Programs.Command import CMD

__author__ = "TheBigEye"
__version__ = "1.8"


def Display_Terminal(master, draggable=False):
    """
    Summary:
    -------
        This function creates a terminal window.

    Parameters:
    ----------
        master: Tkinter.Tk()
            The main window.

        draggable: bool
            If the window is draggable.

    Returns:
    -------
        None

    Example:
    -------
        Display_Terminal(master, True)

    """

    global Terminal_GUI_Image, Close_Terminal_image, Maximize_Terminal_image, Minimize_Terminal_image
    global Terminal, Terminal_screen, Terminal_entry, Close_Terminal_Button, Maximize_Terminal_Button, Minimize_Terminal_Button
    global Close_Terminal, cmd

    Terminal_GUI_Image = PhotoImage(file="Assets/GUI/Terminal/Terminal.png")  # Terminal image base
    Close_Terminal_image = PhotoImage(file="Assets/GUI/Terminal/Close_Terminal_Button.png")  # Terminal close button
    Maximize_Terminal_image = PhotoImage(file="Assets/GUI/Terminal/Maximize_Terminal_Button.png")  # Terminal close button
    Minimize_Terminal_image = PhotoImage(file="Assets/GUI/Terminal/Minimize_Terminal_Button.png")  # Terminal close button

    def Command_handler(event):
        """Execute the commands"""

        CMD(Terminal, Terminal_entry, Terminal_screen)

    Terminal = Label(
        master,
        bg="#CCCCCC",
        image=Terminal_GUI_Image,
        borderwidth="0",
    )

    Terminal_screen = Text(
        Terminal,
        bd=2,
        relief="flat",
        font=("Consolas", 10),
        undo=True,
        wrap="word",
    )

    Terminal_screen.config(width=75, height=20, bg="#000000", fg="#dfdfdf", state="normal", insertbackground="#dfdfdf")
    Terminal_screen.insert(INSERT, "Welcome to the terminal ──────────────────────────────────────────────────" + "\n\n" + ">/" + "\n\n")
    Terminal_screen.focus()

    def Close_Terminal():
        """Close the Terminal"""

        Terminal.place_forget()

    Close_Terminal_Button = Button(
        Terminal,
        width=8,
        height=8,
        bg="#CCCCCC",
        image=Close_Terminal_image,
        borderwidth="0",
        command=Close_Terminal,
    )

    Maximize_Terminal_Button = Button(
        Terminal,
        width=8,
        height=8,
        bg="#CCCCCC",
        image=Maximize_Terminal_image,
        borderwidth="0",
        command=Close_Terminal,
    )

    Minimize_Terminal_Button = Button(
        Terminal,
        width=8,
        height=8,
        bg="#CCCCCC",
        image=Minimize_Terminal_image,
        borderwidth="0",
        command=Close_Terminal,
    )

    Terminal_entry = Entry(
        Terminal,
        width=75,
        # height=4,
        borderwidth="0",
        fg="white",
        bg="#000000",
        font=("Consolas", 10),
    )

    Terminal_entry.config(insertbackground="white")
    Terminal_entry.bind("<Return>", Command_handler)
    Terminal_entry.focus_set()

    if draggable == True:

        make_draggable(Terminal)
    Terminal.place(x=225, y=148)
    Terminal_screen.place(x=3.5, y=25.5)

    Close_Terminal_Button.place(x=520, y=8)
    Maximize_Terminal_Button.place(x=490, y=8)
    Minimize_Terminal_Button.place(x=460, y=8)
    Terminal_entry.place(x=5.5, y=330)
