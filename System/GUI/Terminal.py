from tkinter import Entry, Label, Button, PhotoImage, Text
from tkinter.constants import INSERT
from System.Utils.Charmap import TRIPLE_PROMPT_ICON
from System.GUI.Attributes.Draggable import make_draggable

__author__ = 'TheBigEye'
__version__ = '1.0'


def Display_Terminal(master, draggable = False):


    global Terminal_GUI_Image, Close_Terminal_image, Maximize_Terminal_image, Minimize_Terminal_image
    global Terminal, Terminal_screen, Terminal_entry, Close_Terminal_Button, Maximize_Terminal_Button, Minimize_Terminal_Button
    global Close_Terminal

    Terminal_GUI_Image = PhotoImage(file = "Assets/GUI/Terminal/Terminal.png") # Terminal image base
    Close_Terminal_image = PhotoImage(file = "Assets/GUI/Terminal/Close_Terminal_Button.png") # Terminal close button
    Maximize_Terminal_image = PhotoImage(file = "Assets/GUI/Terminal/Maximize_Terminal_Button.png") # Terminal close button
    Minimize_Terminal_image = PhotoImage(file = "Assets/GUI/Terminal/Minimize_Terminal_Button.png") # Terminal close button

    Terminal = Label(
        master,
        bg= "#CCCCCC",
        image=Terminal_GUI_Image,
        borderwidth="0",
    )

    Terminal_screen = Text(
        Terminal,
        bd=2,
        relief='flat',
        font=('Consolas', 11),
        undo=True,
        wrap='word',
    )

    Terminal_screen.config(width=66, height=18, bg="#000000", fg= "#ffffff", state= 'normal', insertbackground='#FFFFFF')
    Terminal_screen.insert(INSERT , TRIPLE_PROMPT_ICON)
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



    #Terminal_entry = Entry(
    #    Terminal,
    #    width=68,
    #    #height=4,
    #    borderwidth = "0",
    #    fg='green',
    #    bg = "#000000",
    #    font=('Consolas', 11),
    #)

    #Terminal_entry.config(insertbackground='Green')



    if (draggable == True):

        make_draggable(Terminal)

    Terminal.place(x= 225, y= 148)
    Terminal_screen.place(x=2.5, y=27)

    Close_Terminal_Button.place(x=520, y=8)
    Maximize_Terminal_Button.place(x=490, y=8)
    Minimize_Terminal_Button.place(x=460, y=8)
    #Terminal_entry.place(x=2, y=22)