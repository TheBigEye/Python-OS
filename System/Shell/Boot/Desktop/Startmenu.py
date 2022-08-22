import time
from tkinter import Button, Frame, Label

from Libs.pyImage.Image import Image
from Libs.pyLogger.Logger import Logger


class startmenu(Frame):

    def __init__(self, master, start_button_base):
        Frame.__init__(self, master)

        self.master = master
        self.Startbar = start_button_base

        # Initialize the desktop
        startmenu.start_menu_initializer(self)

    def start_menu_initializer(self):

        Logger.info("### Loading start menu components ...")

        # Initialize the Start menu
        self.Startmenu_image = Image.setImage("Assets/Shell/Desktop/Start menu/Start_menu.png")
        self.Startmenu = Label(
            self.master,
            width = 314,
            height = 440,
            image = self.Startmenu_image,
            borderwidth = "0"
        )

        self.Start_button_image = Image.setImage("Assets/Shell/Desktop/Start menu/Start_icon.png", (24, 24), "#ff00ff", "#002C4F")
        self.Start_button_light = Image.setImage("Assets/Shell/Desktop/Start menu/Start_icon.png", (24, 24), "#ff00ff", "#00345B")

        def open_start_menu():
            self.Startmenu.place(x=1, y=128)
            self.Startmenu.lift()
            time.sleep(0.1)

            Open_start_button.place_forget()
            Close_start_button.place(x=4, y=2)

        def close_start_menu():
            self.Startmenu.place_forget()
            time.sleep(0.1)

            Open_start_button.place(x=4, y=2)
            Close_start_button.place_forget()

        Open_start_button = Button(
            self.Startbar,
            image = self.Start_button_image,
            borderwidth = "0",
            relief = "flat",
            bg = "#002C4F",
            activebackground = "#002C4F",
            activeforeground = "#ffffff",
            command = open_start_menu
        )
        Open_start_button.place(x=4, y=2)

        Close_start_button = Button(
            self.Startbar,
            image = self.Start_button_light,
            borderwidth = "0",
            relief = "flat",
            bg = "#002C4F",
            activebackground = "#002C4F",
            activeforeground = "#ffffff",
            command = close_start_menu
        )
        Close_start_button.place_forget()

        Open_start_button.bind("<Enter>", lambda event: Open_start_button.config(image = self.Start_button_light))
        Open_start_button.bind("<Leave>", lambda event: Open_start_button.config(image = self.Start_button_image))

        Close_start_button.bind("<Enter>", lambda event: Close_start_button.config(image = self.Start_button_light))
        Close_start_button.bind("<Leave>", lambda event: Close_start_button.config(image = self.Start_button_image))

        Logger.info("Start menu component loaded")

        # Initialize the Start menu programs list
