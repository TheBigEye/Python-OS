from tkinter import Button, Entry, Frame, Label, Text
from tkinter.constants import INSERT

from System.Core.TaskSystem import add_task, stop_task, update_task
from System.GUI.Attributes.Draggable import drag_n_drop
from System.Programs.Command import CMD
from System.Utils.Utils import get_asset

__author__ = "TheBigEye"
__version__ = "1.8"

class Terminal(Frame):
    """
    Clase Terminal
    """

    def __init__(self, master, draggable: bool = True):
        """
        Constructor de la clase Terminal
        """

        Frame.__init__(self, master)

        self.master = master
        self.draggable = draggable

        # se crea el proceso
        add_task("Terminal", 5, 0.5, 0.1, 0, "normal", "running")

        self.Terminal_GUI_Image = get_asset("Assets/GUI/Terminal/Terminal.png")  # Terminal image base

        def Command_handler(event):
            """Execute the commands"""

            self.Terminal_screen.config(state="normal")
            CMD(self.Terminal, self.Terminal_entry, self.Terminal_screen)
            self.Terminal_screen.config(state="disabled")

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

        self.Terminal_screen.config(width=75, height=20, bg="#000000", fg="#dfdfdf", state="normal", insertbackground="#dfdfdf")
        self.Terminal_screen.insert(INSERT, "═════════════════════════ Welcome to the terminal ═════════════════════════" + "\n\n" + ">/ Type a command, or use help for get commands" + "\n\n")
        self.Terminal_screen.config(state="disabled")

        self.Terminal.place(x=225, y=148)
        self.Terminal_screen.place(x=3.5, y=24)


        # ----------------------------------------------------------------- [Boton de cerrar terminal] -------------------------------------------------------------------------

        self.Close_Terminal_image = get_asset("Assets/GUI/Terminal/Close_Terminal_Button.png")  # Terminal close button
        self.Close_Terminal_Red_image = get_asset("Assets/GUI/Terminal/Close_Terminal_Button_Red.png")  # Terminal close red button

        def Close_Terminal():
            """Close the Terminal"""

            # Termina el  proceso
            stop_task("Terminal")

            self.Terminal.place_forget()


        self.Close_Terminal_Button = Button(
            self.Terminal,
            width=13,
            height=13,
            bg="#2E2E2E",
            image=self.Close_Terminal_image,
            borderwidth=0,
            command=Close_Terminal
        )

        self.Close_Terminal_Button.bind("<Enter>", lambda event: self.Close_Terminal_Button.config(image = self.Close_Terminal_Red_image))
        self.Close_Terminal_Button.bind("<Leave>", lambda event: self.Close_Terminal_Button.config(image = self.Close_Terminal_image))

        self.Close_Terminal_Button.place(x=520, y=4)


        # ----------------------------------------------------------------- [Boton de maximizar terminal] ----------------------------------------------------------------------

        self.Maximize_Terminal_image = get_asset("Assets/GUI/Terminal/Maximize_Terminal_Button.png")  # Terminal maximize button
        self.Maximize_Terminal_light_image = get_asset("Assets/GUI/Terminal/Maximize_Terminal_Button_light.png")  # Terminal maximize button light

        def Maximize_Terminal():
            """Maximize the Terminal"""

            self.Terminal.place(x=0, y=0)
            self.Terminal.config(image=self.Terminal_GUI_Image)

        self.Maximize_Terminal_Button = Button(
            self.Terminal,
            width=13,
            height=13,
            bg="#2E2E2E",
            image=self.Maximize_Terminal_image,
            borderwidth=0,
            command=Maximize_Terminal,
        )

        self.Maximize_Terminal_Button.bind("<Enter>", lambda event: self.Maximize_Terminal_Button.config(image = self.Maximize_Terminal_light_image))
        self.Maximize_Terminal_Button.bind("<Leave>", lambda event: self.Maximize_Terminal_Button.config(image = self.Maximize_Terminal_image))

        self.Maximize_Terminal_Button.place(x=502, y=4)


        # ----------------------------------------------------------------- [Boton de minimizar terminal] ----------------------------------------------------------------------

        self.Minimize_Terminal_image = get_asset("Assets/GUI/Terminal/Minimize_Terminal_Button.png")  # Terminal minimize button
        self.Minimize_Terminal_light_image = get_asset("Assets/GUI/Terminal/Minimize_Terminal_Button_light.png")  # Terminal minimize button light

        def Minimize_Terminal():
            """Minimize the Terminal"""

            self.Terminal.place(x=0, y=0)
            self.Terminal.config(image=self.Terminal_GUI_Image)

        self.Minimize_Terminal_Button = Button(
            self.Terminal,
            width=13,
            height=13,
            bg="#2E2E2E",
            image=self.Minimize_Terminal_image,
            borderwidth="0",
            command=Minimize_Terminal,
        )

        self.Minimize_Terminal_Button.bind("<Enter>", lambda event: self.Minimize_Terminal_Button.config(image = self.Minimize_Terminal_light_image))
        self.Minimize_Terminal_Button.bind("<Leave>", lambda event: self.Minimize_Terminal_Button.config(image = self.Minimize_Terminal_image))

        self.Minimize_Terminal_Button.place(x=484, y=4)


        # ---------------------------------------------------------------------- [Entry de terminal] ---------------------------------------------------------------------------

        self.Terminal_entry = Entry(
            self.Terminal,
            width=75,
            borderwidth="0",
            fg="white",
            bg="#000000",
            font=("Consolas", 10)
        )

        self.Terminal_entry.config(insertbackground="white")
        self.Terminal_entry.bind("<Return>", Command_handler)
        self.Terminal_entry.focus()

        self.Terminal_entry.place(x=5.5, y=330)


        # --------------------------------------------------------------------------- [Final] ----------------------------------------------------------------------------------

        if (draggable == True):

            drag_n_drop(self.Terminal)
