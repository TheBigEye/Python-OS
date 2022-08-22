from tkinter import Button, Entry, Frame, Label, Text
from tkinter.constants import INSERT

from Libs.pyImage.Image import Image
from Libs.pyUtils.pyData import JSON
from System.programs.Terminal.Commands import CMD
from System.shell.Attributes.Draggable import drag_it
from System.shell.Components.UITextbox import UITextbox

__author__ = "TheBigEye"
__version__ = "1.8"

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


# -----------------------------------------------------------------[ WINDOW MANAGER VERSION ]----------------------------------------------------------------------- #
WM_Terminal_icon = Image.setImage("Assets/Shell/Programs/Terminal/Terminal_icon.png", (112, 112), "#ff00ff", "#002C4F")

WM_Terminal_image = Image.setImage("Assets/Shell/Programs/Terminal/WM_Window.png", None, "#ff00ff", get_background())
WM_Terminal_fullheight_image = Image.setImage("Assets/Shell/Programs/Terminal/WM_Window_fullheight.png", None, "#ff00ff", get_background())
WM_Splash_image = Image.setImage("Assets/Shell/Programs/Terminal/WM_Splash.png")

class WM_Terminal(Frame):
    def __init__(self, master, draggable: bool):
        Frame.__init__(self, master)

        self.master = master
        self.draggable = draggable

        self.foreground = get_foreground()
        self.background = get_background()

        def Command_handler(event):
            """Execute the commands"""

            self.Terminal_screen.config(state="normal")
            CMD(self.Terminal, self.Terminal_entry, self.Terminal_screen)
            self.Terminal_screen.config(state="disabled")

        self.Terminal = Label(
            self.master,
            bg="#CCCCCC",
            image=WM_Terminal_image,
            borderwidth="0",
        )

        self.Terminal_screen = UITextbox(
            self.Terminal,
            bd=2,
            relief="flat",
            font=font,
            undo=True,
            wrap="word"
        )

        self.Terminal_screen.config(width=75, height=22, bg=self.background, fg=self.foreground, state="normal", insertbackground="#dfdfdf")
        self.Terminal_screen.insert_colored(" Welcome to the terminal"                                                    + "\n", "#B8BA37")
        self.Terminal_screen.insert(INSERT, "                                                                                \n")
        self.Terminal_screen.insert_color_word("- Type a command, or use help for get commands"                             + "\n", [("help", "#B8BA37")])
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
            relief="flat",
            insertwidth = 5,
            font=font
        )

        self.Terminal_entry.config(insertbackground=self.foreground)
        self.Terminal_entry.bind("<Return>", Command_handler)
        self.Terminal_entry.focus()

        self.Terminal_entry.place(x=5.5, y=328)


        def Splash_screen(time):
            """Splash screen"""

            self.Splash = Label(
                self.Terminal,
                bg="#002C4F",
                image=WM_Splash_image,
                borderwidth="0",
            )

            self.Splash.place(x=0, y=0)

            self.Splash_icon = Label(
                self.Splash,
                image=WM_Terminal_icon,
                borderwidth="0",
            )

            # Put the icon in the middle of the window, .5 is the center of the window
            self.Splash_icon.place(relx=.5, y=170, anchor="center")

            self.Splash.after(time, self.Splash.destroy)

        Splash_screen(5000)

        # If the user press alt + q, the terminal will close
        self.Terminal_entry.bind("<Alt-q>", lambda event: self.Terminal.destroy())

# ---------------------------------------------------------------------- [Left and rigth move] ---------------------------------------------------------------------------

        def update_to_right():
            self.Terminal.place(x=6, y=12)
            self.Terminal.config(image=WM_Terminal_fullheight_image)
            self.Terminal_screen.config(width=68, height=34, bg=self.background, fg=self.foreground)
            self.Terminal_entry.config(width=68)
            self.Terminal_entry.place(y=524)

        # If the user press alt + ->, the terminal will be placed on the right
        self.Terminal_entry.bind("<Alt-Right>", lambda event: update_to_right())

        def update_to_left():
            self.Terminal.place(x=-500, y=12)
            self.Terminal.config(image=WM_Terminal_fullheight_image)
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


# ----------------------------------------------------------------- [DESKTOP ENVIROMENT VERSION] ---------------------------------------------------------------------
DE_Terminal_icon = Image.setImage("Assets/Shell/Programs/Terminal/Terminal_icon.png", (112, 112), "#ff00ff", "#002C4F")

DE_Terminal_image = Image.setImage("Assets/Shell/Programs/Terminal/DE_Window.png", None, "#ff00ff", get_background())
DE_Splash_image = Image.setImage("Assets/Shell/Programs/Terminal/DE_Splash.png")

class DE_Terminal(Frame):
    def __init__(self, master, draggable: bool):
        Frame.__init__(self, master)

        self.master = master
        self.draggable = draggable

        self.foreground = get_foreground()
        self.background = get_background()

        def Command_handler(event):
            """Execute the commands"""

            self.Terminal_screen.config(state="normal")
            CMD(self.Terminal, self.Terminal_entry, self.Terminal_screen)
            self.Terminal_screen.config(state="disabled")

        self.Terminal = Label(
            self.master,
            bg="#CCCCCC",
            image=DE_Terminal_image,
            borderwidth="0",
        )

        self.Terminal_screen = UITextbox(
            self.Terminal,
            bd=2,
            relief="flat",
            font=font,
            undo=True,
            wrap="word"
        )

        self.Terminal_screen.config(width=75, height=20, bg=self.background, fg=self.foreground, state="normal", insertbackground="#dfdfdf")
        self.Terminal_screen.insert_colored(" Welcome to the terminal"                                                    + "\n", "#B8BA37")
        self.Terminal_screen.insert(INSERT, "                                                                                \n")
        self.Terminal_screen.insert_color_word("- Type a command, or use help for get commands"                             + "\n", [("help", "#B8BA37")])
        self.Terminal_screen.insert(INSERT, "                                                                                \n")

        self.Terminal_screen.config(state="disabled")

        self.Terminal.place(relx=.2, y=132)
        self.Terminal_screen.place(x=3.5, y=24)


# ----------------------------------------------------------------- [Close terminal button] -------------------------------------------------------------------------

        self.Close_button_image = Image.setImage("Assets/Shell/Window/Close_button.png")  # Terminal close button
        self.Close_button_red_image = Image.setImage("Assets/Shell/Window/Close_button_red.png")  # Terminal close button

        def Close_Terminal():
            """Close the Terminal"""

            # destroy all the widgets from self.terminal
            for widget in self.Terminal.winfo_children():
                widget.destroy()

            self.master.after(1000, self.Terminal.destroy)

        self.Close_button = Button(
            self.Terminal,
            bg="#00142D",
            activebackground="#00142D",
            highlightbackground="#00142D",
            highlightcolor="#00142D",
            image=self.Close_button_image,
            borderwidth=0,
            command=Close_Terminal
        )

        self.Close_button.bind("<Enter>", lambda event: self.Close_button.config(image = self.Close_button_red_image))
        self.Close_button.bind("<Leave>", lambda event: self.Close_button.config(image = self.Close_button_image))

        self.Close_button.place(x=519, y=2)


# ----------------------------------------------------------------- [Maximize terminal button] ----------------------------------------------------------------------

        self.Maximize_button_image = Image.setImage("Assets/Shell/Window/Maximize_button.png")  # Terminal maximize button
        self.Maximize_button_light_image = Image.setImage("Assets/Shell/Window/Maximize_button_light.png")  # Terminal maximize button light

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

        self.Minimize_button_image = Image.setImage("Assets/Shell/Window/Minimize_button.png")  # Terminal minimize button
        self.Minimize_button_light_image = Image.setImage("Assets/Shell/Window/Minimize_button_light.png")  # Terminal minimize button light

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
                image=DE_Splash_image,
                borderwidth="0",
            )

            self.Splash.place(x=0, y=0)

            self.Splash_icon = Label(
                self.Splash,
                image=DE_Terminal_icon,
                borderwidth="0",
            )

            # Put the icon in the middle of the window, .5 is the center of the window
            self.Splash_icon.place(relx=.5, y=170, anchor="center")

            self.Splash.after(time, self.Splash.destroy)

        Splash_screen(5000)

        self.Terminal_screen.bind("<Button-1>", lambda event: self.Terminal.lift())
        self.Terminal_entry.bind("<Button-1>", lambda event: self.Terminal.lift())
# --------------------------------------------------------------------------- [End] ----------------------------------------------------------------------------------

        # draggable terminal window
        if self.draggable:
            # drag n drop using tkinter.dnd module
            drag_it(self.Terminal)
