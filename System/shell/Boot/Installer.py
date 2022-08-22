from tkinter import Entry, Label, Text
from tkinter.constants import INSERT, NORMAL

from System.programs.Terminal.Commands import CMD
from System.shell.Components.UITextbox import UITextbox

__author__ = 'TheBigEye'
__version__ = '1.5'

def Os_Installer(master):  # Display the Post-Bios window (coming soon the OOBE)

    global Terminal, Terminal_screen

    master.configure(background="#000000")  # Sets the background to Blue

    def Command_handler(event):
        """Execute the commands"""

        CMD(Terminal, Terminal_entry, Terminal_screen)

    Terminal = Label(master, width=1024, height=600 ,bg="#000000", borderwidth=0.1)
    Terminal.place(x=0, y=0)


    Terminal_screen = UITextbox(
        Terminal,
        bd=2,
        relief="flat",
        font=("Consolas", 10),
        undo=True,
        wrap="word",
    )

    Terminal_screen.config(width=145, height=38, bg="#000000", fg="#dfdfdf", state=NORMAL, insertbackground="#dfdfdf")
    Terminal_screen.insert(INSERT, "──────────────────────────────────────────────────────────── Welcome to the terminal ────────────────────────────────────────────────────────────" + "\n\n" + ">/" + "\n\n")

    Terminal_screen.place(x=1, y=1)

    Terminal_entry = Entry(
        Terminal,
        width=145,
        # height=4,
        borderwidth="0",
        fg="white",
        bg="#000000",
        font=("Consolas", 10),
    )

    Terminal_entry.config(insertbackground="white")
    Terminal_entry.bind("<Return>", Command_handler)
    Terminal_entry.focus()

    Terminal_entry.place(x=2.0, y=580)
