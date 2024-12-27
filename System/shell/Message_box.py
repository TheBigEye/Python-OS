import random
from tkinter import Label, Misc

from Libs.pyImage.Image import Image
from System.shell.Attributes.Draggable import drag_it

__author__ = 'TheBigEye'
__version__ = '1.2'

Font = "Segou UI"

class MessageBox(Label):
    """MessageBox class"""

    def __init__(self, master: Misc, message, mb_type: str, draggable):
        """Constructor"""

        Label.__init__(self, master)

        self.master = master
        self.message = message
        self.mb_type = mb_type.lower()
        self.draggable = draggable

        self.FG_color = "#ffffff"
        self.BG_color = "#001633"

        # Change the border color depending on the messagebox type.
        if self.mb_type == "info":
            self.MB_Image = Image.setImage("Assets/Shell/Desktop/Message box/WM_Window.png", None, "#003C6C", "#4A91A7")
        elif self.mb_type == "warning": 
            self.MB_Image = Image.setImage("Assets/Shell/Desktop/Message box/WM_Window.png", None, "#003C6C", "#D66535")
        elif self.mb_type == "error": 
            self.MB_Image = Image.setImage("Assets/Shell/Desktop/Message box/WM_Window.png", None, "#003C6C", "#D63A35" )
        else:
            self.MB_Image = Image.setImage("Assets/Shell/Desktop/Message box/WM_Window.png")

        # Icons.
        self.MB_Error_icon = Image.setImage("Assets/Shell/Desktop/Message box/Error.png", (36, 36), "#ff00ff", self.BG_color)
        self.MB_Info_icon = Image.setImage("Assets/Shell/Desktop/Message box/Info.png", (36, 36), "#ff00ff", self.BG_color)
        self.MB_Warning_icon = Image.setImage("Assets/Shell/Desktop/Message box/Warning.png", (36, 36), "#ff00ff", self.BG_color)

        """Create a message box"""

        # Make the window.
        self.MB_Window = Label (
            master = self.master,
            bg = self.BG_color,
            image = self.MB_Image,
            borderwidth = "0",
        )

        # Make the icon depending on the messagebox type.
        if (self.mb_type == "error"):
            self.MB_Icon = Label (
                self.MB_Window,
                bg = self.BG_color,
                image = self.MB_Error_icon,
                borderwidth = "0",
            )
        elif (self.mb_type == "info"):
            self.MB_Icon = Label (
                self.MB_Window,
                bg = self.BG_color,
                image = self.MB_Info_icon,
                borderwidth = "0",
            )
        elif (self.mb_type == "warning"):
            self.MB_Icon = Label (
                self.MB_Window,
                bg = self.BG_color,
                image = self.MB_Warning_icon,
                borderwidth = "0",
            )
        else:
            raise Exception("MessageBox type " + self.mb_type +" not found")

        self.MB_Icon.place(x=18, y=32)

        # Make the message.
        self.MB_Message = Label (
            self.MB_Window,
            width = len(self.message),
            height = 1,
            bg = self.BG_color,
            fg = self.FG_color,
            text = self.message,
            font="Consolas 8",
            anchor="w"
        )

        self.MB_Message.place(x=64, y=36)
        self.MB_Window.place(x=320 , y=240)

        # Make window active
        self.MB_Window.lift()
        self.MB_Window.focus_set()

        # if click right button, lift window
        self.MB_Window.bind("<Button-3>", lambda event: self.MB_Window.lift())

        # if click in the message box, focus on it
        self.MB_Window.bind("<Button-1>", lambda event: self.MB_Window.focus_set())

        def close_MB():
            """Close message box"""

            self.MB_Window.destroy()

        # if press alt + q, close the message box
        self.MB_Window.bind("<Alt-q>", lambda event: close_MB())

        if (self.draggable):
            #drag_it(self.MB_Window) # waiting drag_it() rewriting
            pass
