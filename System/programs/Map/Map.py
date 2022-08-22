from tkinter import Button, Frame, Label

import tkintermapview as tkmapview
from Libs.pyImage.Image import Image
from System.shell.Attributes.Draggable import drag_it

class Map(Frame):

    """
    Map viewer
    """

    def __init__(self, master, draggable: bool):
        """
        Map constructor
        """

        Frame.__init__(self, master)

        self.master = master
        self.draggable = draggable

        self.Map_image = Image.setImage("Assets/Shell/Programs/Map/Window.png", None, "#ff00ff", "#002C4F")  # Map image base
        self.Splash_logo_image = Image.setImage("Assets/Shell/Programs/Map/Map_icon.png", (112, 112), "#ff00ff", "#002C4F")  # Splash image
        self.Splash_image = Image.setImage("Assets/Shell/Programs/Map/Splash.png")  # Splash image

        self.Map = Label(
            self.master,
            bg="#CCCCCC",
            image=self.Map_image,
            borderwidth="0",
        )

        self.Map_view = tkmapview.TkinterMapView(self.Map, width=538, height=319, corner_radius=0)

        self.Map.place(relx=.2, y=132)
        self.Map_view.place(x=0.5, y=23)


# ----------------------------------------------------------------- [Close map button] -------------------------------------------------------------------------

        self.Close_button_image = Image.setImage("Assets/Shell/Window/Close_button.png")  # Map close button
        self.Close_button_red_image = Image.setImage("Assets/Shell/Window/Close_button_red.png")  # Map close button

        def Close_Map():
            """Close the Map"""

            for widget in self.Map.winfo_children():
                widget.destroy()

            self.master.after(1000, self.Map.destroy)

        self.Close_button = Button(
            self.Map,
            width=13,
            height=13,
            bg="#2E2E2E",
            image=self.Close_button_image,
            borderwidth=0,
            command=Close_Map
        )

        self.Close_button.bind("<Enter>", lambda event: self.Close_button.config(image = self.Close_button_red_image))
        self.Close_button.bind("<Leave>", lambda event: self.Close_button.config(image = self.Close_button_image))

        self.Close_button.place(x=520, y=4)


# ----------------------------------------------------------------- [Maximize map button] ----------------------------------------------------------------------

        self.Maximize_button_image = Image.setImage("Assets/Shell/Window/Maximize_button.png")  # Map maximize button
        self.Maximize_button_light_image = Image.setImage("Assets/Shell/Window/Maximize_button_light.png")  # Map maximize button light

        def Maximize_Map():
            """Maximize the Map"""

            self.Map.place(x=0, y=0)
            self.Map.config(image=self.Map_image)

        self.Maximize_button = Button(
            self.Map,
            width=13,
            height=13,
            bg="#2E2E2E",
            image=self.Maximize_button_image,
            borderwidth=0,
            command=Maximize_Map
        )

        self.Maximize_button.bind("<Enter>", lambda event: self.Maximize_button.config(image = self.Maximize_button_light_image))
        self.Maximize_button.bind("<Leave>", lambda event: self.Maximize_button.config(image = self.Maximize_button_image))

        self.Maximize_button.place(x=502, y=4)


        # ----------------------------------------------------------------- [Minimize terminal button] ----------------------------------------------------------------------

        self.Minimize_button_image = Image.setImage("Assets/Shell/Window/Minimize_button.png")  # Terminal minimize button
        self.Minimize_button_light_image = Image.setImage("Assets/Shell/Window/Minimize_button_light.png")  # Terminal minimize button light

        def Minimize_Map():
            """Minimize the Map"""

            self.Map.place(x=0, y=0)
            self.Map.config(image=self.Map_image)

        self.Minimize_button = Button(
            self.Map,
            width=13,
            height=13,
            bg="#2E2E2E",
            image=self.Minimize_button_image,
            borderwidth="0",
            command=Minimize_Map,
        )

        self.Minimize_button.bind("<Enter>", lambda event: self.Minimize_button.config(image = self.Minimize_button_light_image))
        self.Minimize_button.bind("<Leave>", lambda event: self.Minimize_button.config(image = self.Minimize_button_image))

        self.Minimize_button.place(x=484, y=4)


# ---------------------------------------------------------------------- [Terminal input entry] ---------------------------------------------------------------------------
        def Splash_screen(time):
            """Splash screen"""

            self.Splash = Label(
                self.Map,
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

        if self.draggable:
            # drag n drop using tkinter.dnd module
            drag_it(self.Map)
