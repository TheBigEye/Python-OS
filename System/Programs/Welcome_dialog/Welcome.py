from tkinter import Button, Frame, Label
from Libs.pyImage.Image import Image

from System.shell.Attributes.Draggable import drag_it
from System.programs.Terminal.Commands import CMD

__author__ = "TheBigEye"
__version__ = "1.8"

class Welcome_dialog(Frame):

    """
    Clase Welcome
    """

    def __init__(self, master, draggable: bool = True):
        """
        Constructor de la clase Welcome
        """

        Frame.__init__(self, master)

        self.master = master
        self.draggable = draggable


        self.Welcome_window_image = Image.setImage("Assets/Shell/Programs/Welcome dialog/Window.png")  # Welcome dialog image base

        self.Welcome_window = Label(
            self.master,
            bg="#CCCCCC",
            image=self.Welcome_window_image,
            borderwidth="0"
        )

        self.Welcome_screen_image = Image.setImage("Assets/Shell/Programs/Welcome dialog/Dialog.png")

        self.Welcome_screen = Label(
            self.Welcome_window,
            bg="#CCCCCC",
            image=self.Welcome_screen_image,
            borderwidth="0"
        )

        self.Welcome_window.place(x=260, y=148)
        self.Welcome_screen.place(x=0.5, y=22)


        # ----------------------------------------------------------------- [Boton de cerrar ventana] -------------------------------------------------------------------------

        self.Close_button_image = Image.setImage("Assets/Shell/Window/Close_button.png")  # Window close button
        self.Close_button_red_image = Image.setImage("Assets/Shell/Window/Close_button_red.png")  # Window close red button

        def Close_window():
            """Close the window"""

            self.Welcome_window.destroy()


        self.Close_button = Button(
            self.Welcome_window,
            width=13,
            height=13,
            bg="#2E2E2E",
            image=self.Close_button_image,
            borderwidth=0,
            command=Close_window
        )

        self.Close_button.bind("<Enter>", lambda event: self.Close_button.config(image = self.Close_button_red_image))
        self.Close_button.bind("<Leave>", lambda event: self.Close_button.config(image = self.Close_button_image))

        self.Close_button.place(x=463, y=4)

        # --------------------------------------------------------------------------- [Final] ----------------------------------------------------------------------------------

        if (draggable):

            drag_it(self.Welcome_dialog)
