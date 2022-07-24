from tkinter import Button, Entry, Frame, Label, Text
from tkinter.constants import INSERT

from Libs.pyImage.Image import setImage
from Libs.pyUtils.pyData import JSON
from System.Programs.Terminal.Commands import CMD
from System.Shell.Attributes.Draggable import drag_it

__author__ = "TheBigEye"
__version__ = "1.8"

#font = ("Cascadia Code", 9)
font = ("Consolas", 10)

def set_foreground(color):

    """Set the foreground color of the terminal"""

    JSON.set("Assets/Data/Terminal data/Terminal.json", "Foreground", color)

def get_foreground():

    """Get the foreground color of the terminal"""

    return JSON.get("Assets/Data/Terminal data/Terminal.json", "Foreground")

def set_background(color):

    """Set the background color of the terminal"""

    JSON.set("Assets/Data/Terminal data/Terminal.json", "Background", color)

def get_background():

    return JSON.get("Assets/Data/Terminal data/Terminal.json", "Background")


class Terminal(Frame):

    """
    Terminal
    """

    def __init__(self, master, draggable: bool):
        """
        Terminal constructor
        """

        Frame.__init__(self, master)

        self.master = master
        self.draggable = draggable

        # Load the values from the registry
        Foreground_color = get_foreground()
        Background_color = get_background()

        self.foreground = Foreground_color
        self.background = Background_color

        def Command_handler(event):
            """Execute the commands"""

            self.Terminal_screen.config(state="normal")
            CMD(self.Terminal, self.Terminal_entry, self.Terminal_screen)
            self.Terminal_screen.config(state="disabled")

        self.Terminal_image = setImage("Assets/Shell/Programs/Terminal/Window.png", None, "#ff00ff", self.background)  # Terminal image base
        self.Terminal_fullheight_image = setImage("Assets/Shell/Programs/Terminal/Fullheight.png", None, "#ff00ff", self.background)  # Terminal left image

        self.Splash_logo_image = setImage("Assets/Shell/Programs/Terminal/Terminal_icon.png", (112, 112), "#ff00ff", "#002C4F")  # Splash image
        self.Splash_image = setImage("Assets/Shell/Programs/Terminal/Splash.png")  # Splash image


        self.Terminal = Label(
            self.master,
            bg="#CCCCCC",
            image=self.Terminal_image,
            borderwidth="0",
        )

        self.Terminal_screen = Text(
            self.Terminal,
            bd=2,
            relief="flat",
            font=font,
            undo=True,
            wrap="word"
        )

        self.Terminal_screen.config(width=75, height=22, bg=self.background, fg=self.foreground, state="normal", insertbackground="#dfdfdf")
        self.Terminal_screen.insert(INSERT, " Welcome to the terminal"                                                    + "\n")
        self.Terminal_screen.insert(INSERT, "                                                                                \n")
        self.Terminal_screen.insert(INSERT, ">/ Type a command, or use help for get commands"                             + "\n")
        self.Terminal_screen.insert(INSERT, "                                                                                \n")

        self.Terminal_screen.config(state="disabled")

        self.Terminal.place(relx=.5, y=132)
        self.Terminal.place(x= int(self.Terminal.winfo_x() - 275))
        self.Terminal_screen.place(x=3.5, y=3.5)


# ---------------------------------------------------------------------- [Terminal input entry] ---------------------------------------------------------------------------

        self.Terminal_entry = Entry(
            self.Terminal,
            width=75,
            borderwidth="0",
            fg=self.foreground,
            bg=self.background,
            font=font
        )

        self.Terminal_entry.config(insertbackground=self.foreground)
        self.Terminal_entry.bind("<Return>", Command_handler)
        self.Terminal_entry.focus()

        self.Terminal_entry.place(x=5.5, y=324)


        def Splash_screen(time):
            """Splash screen"""

            self.Splash = Label(
                self.Terminal,
                bg="#002C4F",
                image=self.Splash_image,
                borderwidth="0",
            )

            self.Splash.place(x=0, y=0)

            self.Splash_logo = Label(
                self.Splash,
                image=self.Splash_logo_image,
                borderwidth="0",
            )

            # Put the logo in the middle of the window, .5 is the center of the window
            self.Splash_logo.place(relx=.5, y=170, anchor="center")

            self.Splash.after(time, self.Splash.destroy)

        Splash_screen(5000)

        # If the user press alt + q, the terminal will close
        self.Terminal_entry.bind("<Alt-q>", lambda event: self.Terminal.destroy())

# ---------------------------------------------------------------------- [Left and rigth move] ---------------------------------------------------------------------------

        def update_to_right():
            self.Terminal.place(x=6, y=12)
            self.Terminal.config(image=self.Terminal_fullheight_image)
            self.Terminal_screen.config(width=68, height=34, bg=self.background, fg=self.foreground)
            self.Terminal_entry.config(width=68)
            self.Terminal_entry.place(y=524)

        # If the user press alt + ->, the terminal will be placed on the right
        self.Terminal_entry.bind("<Alt-Right>", lambda event: update_to_right())

        def update_to_left():
            self.Terminal.place(x=-500, y=12)
            self.Terminal.config(image=self.Terminal_fullheight_image)
            self.Terminal_screen.config(width=68, height=34, bg=self.background, fg=self.foreground)
            self.Terminal_entry.config(width=68)
            self.Terminal_entry.place(y=524)

        # If the user press alt + <-, the terminal will be placed on the left
        self.Terminal_entry.bind("<Alt-Left>", lambda event: update_to_left())

        #  if right click on terminal_entry or terminal_screen, the terminal will be lifted
        self.Terminal_entry.bind("<Button-3>", lambda event: self.Terminal.lift())
        self.Terminal_screen.bind("<Button-3>", lambda event: self.Terminal.lift())

        # if click on terminal_screen, focus on terminal_entry
        self.Terminal_screen.bind("<Button-1>", lambda event: self.Terminal_entry.focus())

# --------------------------------------------------------------------------- [End] ----------------------------------------------------------------------------------

        # draggable terminal window
        if self.draggable:
            # drag n drop using tkinter.dnd module
            #drag_it(self.Terminal)
            pass
