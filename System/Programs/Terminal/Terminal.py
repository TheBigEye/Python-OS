from tkinter import Button, Entry, Frame, Label, Text
from tkinter.constants import INSERT

from System.Core.KeysSystem import add_key, get_value
from System.Programs.Terminal.Command import CMD
from System.UI.Attributes.Draggable import drag_n_drop
from System.Utils.Utils import Asset

__author__ = "TheBigEye"
__version__ = "1.8"

buttons_size = (13, 13)

def set_foreground(color):

    """Set the foreground color of the terminal"""

    # save the color in the registry
    add_key("HKEY_CURRENT_USER", "Software", "Terminal", "Foreground", color, "str")


class Terminal(Frame):

    """
    Clase Terminal
    """

    def __init__(self, master, draggable: bool):
        """
        Constructor de la clase Terminal
        """

        Frame.__init__(self, master)

        # Load the values from the registry
        Foreground = get_value("HKEY_CURRENT_USER", "Software", "Terminal", "Foreground")

        self.master = master
        self.draggable = draggable
        self.foreground = Foreground

        def Command_handler(event):
            """Execute the commands"""

            self.Terminal_screen.config(state="normal")
            CMD(self.Terminal, self.Terminal_entry, self.Terminal_screen)
            self.Terminal_screen.config(state="disabled")


        self.Terminal_GUI_Image = Asset("Terminal.png")  # Terminal image base

        self.Terminal = Label(
            self.master,
            bg="#CCCCCC",
            image=self.Terminal_GUI_Image,
            borderwidth="0",
        )

        self.Terminal_screen = Text(
            self.Terminal,
            bd=2,
            relief="flat",
            font=("Consolas", 10),
            undo=True,
            wrap="word"
        )

        self.Terminal_screen.config(width=75, height=20, bg="#000000", fg=self.foreground, state="normal", insertbackground="#dfdfdf")
        self.Terminal_screen.insert(INSERT, "═════════════════════════ Welcome to the terminal ═════════════════════════")
        self.Terminal_screen.insert(INSERT, "\n\n")
        self.Terminal_screen.insert(INSERT, ">/ Type a command, or use help for get commands")
        self.Terminal_screen.insert(INSERT, "\n\n")
        self.Terminal_screen.config(state="disabled")

        self.Terminal.place(x=260, y=148)
        self.Terminal_screen.place(x=3.5, y=24)


        # ----------------------------------------------------------------- [Boton de cerrar terminal] -------------------------------------------------------------------------

        self.Close_button_image = Asset("Close_button.png")  # Terminal close button
        self.Close_button_red_image = Asset("Close_button_red.png")  # Terminal close red button

        def Close_Terminal():
            """Close the Terminal"""

            self.Terminal.place_forget()


        self.Close_button = Button(
            self.Terminal,
            width=buttons_size[0],
            height=buttons_size[1],
            bg="#2E2E2E",
            image=self.Close_button_image,
            borderwidth=0,
            command=Close_Terminal
        )

        self.Close_button.bind("<Enter>", lambda event: self.Close_button.config(image = self.Close_button_red_image))
        self.Close_button.bind("<Leave>", lambda event: self.Close_button.config(image = self.Close_button_image))

        self.Close_button.place(x=520, y=4)


        # ----------------------------------------------------------------- [Boton de maximizar terminal] ----------------------------------------------------------------------

        self.Maximize_button_image = Asset("Maximize_button.png")  # Terminal maximize button
        self.Maximize_button_light_image = Asset("Maximize_button_light.png")  # Terminal maximize button light

        def Maximize_Terminal():
            """Maximize the Terminal"""

            self.Terminal.place(x=0, y=0)
            self.Terminal.config(image=self.Terminal_GUI_Image)

        self.Maximize_button = Button(
            self.Terminal,
            width=buttons_size[0],
            height=buttons_size[1],
            bg="#2E2E2E",
            image=self.Maximize_button_image,
            borderwidth=0,
            command=Maximize_Terminal,
        )

        self.Maximize_button.bind("<Enter>", lambda event: self.Maximize_button.config(image = self.Maximize_button_light_image))
        self.Maximize_button.bind("<Leave>", lambda event: self.Maximize_button.config(image = self.Maximize_button_image))

        self.Maximize_button.place(x=502, y=4)


        # ----------------------------------------------------------------- [Boton de minimizar terminal] ----------------------------------------------------------------------

        self.Minimize_button_image = Asset("Minimize_button.png")  # Terminal minimize button
        self.Minimize_button_light_image = Asset("Minimize_button_light.png")  # Terminal minimize button light

        def Minimize_Terminal():
            """Minimize the Terminal"""

            self.Terminal.place(x=0, y=0)
            self.Terminal.config(image=self.Terminal_GUI_Image)

        self.Minimize_button = Button(
            self.Terminal,
            width=buttons_size[0],
            height=buttons_size[1],
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
            bg="#000000",
            font=("Consolas", 10)
        )

        self.Terminal_entry.config(insertbackground="white")
        self.Terminal_entry.bind("<Return>", Command_handler)
        self.Terminal_entry.focus()

        self.Terminal_entry.place(x=5.5, y=330)


        # --------------------------------------------------------------------------- [Final] ----------------------------------------------------------------------------------

        # draggable terminal window
        if (draggable):

            drag_n_drop(self.Terminal)
