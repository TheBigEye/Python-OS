from tkinter import Entry, Label, Text
from tkinter.constants import DISABLED, INSERT, NORMAL
from System.Programs.Command import CMD
from System.Utils.Colormap import Black

__author__ = 'Nahuel senek'
__version__ = '1.5'

def Os_Installer(master):  # Display the Post-Bios window (coming soon the OOBE)

    global Terminal, Terminal_screen

    master.configure(background=Black)  # Sets the background to Blue


    def Command_handler(event):
        """Execute the commands"""

        CMD(Terminal, Terminal_entry, Terminal_screen)

    #Post_Bios_GUI = PhotoImage(file="Assets/GUI/Post_BIOS.png")
    #Post_Bios = Label(master, image=Post_Bios_GUI, borderwidth=0.1)
    #Post_Bios.place(x=0, y=0)

    #Terminal = Label(master, text="Post-BIOS", font=("Arial", 20), bg=Low_blue, fg="white", borderwidth=0.1)
    Terminal = Label(master, width=1024, height=600 ,bg=Black, borderwidth=0.1)
    Terminal.place(x=0, y=0)


    Terminal_screen = Text(
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