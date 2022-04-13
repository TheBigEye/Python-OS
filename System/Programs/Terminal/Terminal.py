from tkinter import Button, Entry, Frame, Label, Text
from tkinter.constants import INSERT

from System.Programs.Terminal.Commands import CMD
from System.UI.Attributes.Draggable import drag_n_drop
from System.Utils.Utils import Asset, Asset_color, Data_get, Data_set

__author__ = "TheBigEye"
__version__ = "1.8"

#font = ("Cascadia Code", 9)
font = ("Consolas", 10)


def set_foreground(color):

    """Set the foreground color of the terminal"""

    # Save the json in Assets/GUI/Desktop/Terminal/Data/Terminal.json
    Data_set("Terminal data", "Terminal.json", "Foreground", color)


def get_foreground():

    """Get the foreground color of the terminal"""

    return Data_get("Terminal data", "Terminal.json", "Foreground")


def set_background(color):

    """Set the background color of the terminal"""

    # Save the json in Assets/GUI/Desktop/Terminal/Data/Terminal.json
    Data_set("Terminal data", "Terminal.json", "Background", color)


def get_background():

    return Data_get("Terminal data", "Terminal.json", "Background")


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

        self.Terminal_image = Asset_color("Terminal", "Window.png", "null", "#ff00ff", self.background)  # Terminal image base

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

        self.Terminal_screen.config(width=75, height=20, bg=self.background, fg=self.foreground, state="normal", insertbackground="#dfdfdf")
        self.Terminal_screen.insert(INSERT, "═════════════════════════ Welcome to the terminal ═════════════════════════" + "\n")
        self.Terminal_screen.insert(INSERT, "                                                                                \n")
        self.Terminal_screen.insert(INSERT, ">/ Type a command, or use help for get commands"                             + "\n")
        self.Terminal_screen.insert(INSERT, "                                                                                \n")

        self.Terminal_screen.config(state="disabled")

        self.Terminal.place(x=260, y=148)
        self.Terminal_screen.place(x=3.5, y=24)


        # ----------------------------------------------------------------- [Close terminal button] -------------------------------------------------------------------------

        self.Close_button_image = Asset("Window", "Close_button.png")  # Terminal close button
        self.Close_button_red_image = Asset("Window", "Close_button_red.png")  # Terminal close red button

        def Close_Terminal():
            """Close the Terminal"""

            # get the widgets from the widget and destroy them
            for widget in self.Terminal.winfo_children():
                widget.destroy()

            self.Terminal.after(512, self.Terminal.destroy)


        self.Close_button = Button(
            self.Terminal,
            width=13,
            height=13,
            bg="#2E2E2E",
            image=self.Close_button_image,
            borderwidth=0,
            command=Close_Terminal
        )

        self.Close_button.bind("<Enter>", lambda event: self.Close_button.config(image = self.Close_button_red_image))
        self.Close_button.bind("<Leave>", lambda event: self.Close_button.config(image = self.Close_button_image))

        self.Close_button.place(x=520, y=4)


        # ----------------------------------------------------------------- [Maximize terminal button] ----------------------------------------------------------------------

        self.Maximize_button_image = Asset("Window", "Maximize_button.png")  # Terminal maximize button
        self.Maximize_button_light_image = Asset("Window", "Maximize_button_light.png")  # Terminal maximize button light

        def Maximize_Terminal():
            """Maximize the Terminal"""

            self.Terminal.place(x=0, y=0)
            self.Terminal.config(image=self.Terminal_image)

        self.Maximize_button = Button(
            self.Terminal,
            width=13,
            height=13,
            bg="#2E2E2E",
            image=self.Maximize_button_image,
            borderwidth=0,
            command=Maximize_Terminal,
        )

        self.Maximize_button.bind("<Enter>", lambda event: self.Maximize_button.config(image = self.Maximize_button_light_image))
        self.Maximize_button.bind("<Leave>", lambda event: self.Maximize_button.config(image = self.Maximize_button_image))

        self.Maximize_button.place(x=502, y=4)


        # ----------------------------------------------------------------- [Minimize terminal button] ----------------------------------------------------------------------

        self.Minimize_button_image = Asset("Window", "Minimize_button.png")  # Terminal minimize button
        self.Minimize_button_light_image = Asset("Window", "Minimize_button_light.png")  # Terminal minimize button light

        def Minimize_Terminal():
            """Minimize the Terminal"""

            self.Terminal.place(x=0, y=0)
            self.Terminal.config(image=self.Terminal_image)

        self.Minimize_button = Button(
            self.Terminal,
            width=13,
            height=13,
            bg="#2E2E2E",
            image=self.Minimize_button_image,
            borderwidth="0",
            command=Minimize_Terminal,
        )

        self.Minimize_button.bind("<Enter>", lambda event: self.Minimize_button.config(image = self.Minimize_button_light_image))
        self.Minimize_button.bind("<Leave>", lambda event: self.Minimize_button.config(image = self.Minimize_button_image))

        self.Minimize_button.place(x=484, y=4)


        # ---------------------------------------------------------------------- [Entry de terminal] ---------------------------------------------------------------------------

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

        self.Terminal_entry.place(x=5.5, y=330)

        self.Terminal_screen.bind("<Button-1>", lambda event: self.Terminal.lift())
        self.Terminal_entry.bind("<Button-1>", lambda event: self.Terminal.lift())
        # --------------------------------------------------------------------------- [Final] ----------------------------------------------------------------------------------

        # draggable terminal window
        if draggable:
            drag_n_drop(self.Terminal)

