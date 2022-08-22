from tkinter import Button, Misc, PhotoImage

from Libs.pyImage.Image import Image


class Taskbar_button(Button):
    """
    Taskbar button

    Arguments:
        `master : [Misc]` The parent widget where the button will be placed.
        `button_image_path : [str]` The path to the button image.
        `master_image_path : [str]` The path to the master image.
        `position : [tuple]` The position of the button.

    Returns:
        `button : [Button]` The button.
    """

    def __init__(self, master: Misc, button_image_path: str, master_image_path: str, position: tuple) -> None:

        self.master = master
        self.button_image_path = button_image_path
        self.master_image_path = master_image_path
        self.position = position

        self.bright = 12

        self.image_color = Image.getTkColor(master_image_path, position[0], position[1])
        self.image_active_color = ("#%02x%02x%02x" % (
            int(self.image_color[1:3], 16) + self.bright, # Red
            int(self.image_color[3:5], 16) + self.bright, # Green
            int(self.image_color[5:7], 16) + self.bright  # Blue
        ))

        self.normal_image = Image.setImage(button_image_path, (24, 24), "#ff00ff", self.image_color)
        self.active_image = Image.setImage(button_image_path, (24, 24), "#ff00ff", self.image_active_color)

        # Creates the button
        super().__init__(
            master,
            relief="flat",
            bg=self.image_color,
            activebackground=self.image_active_color,
            image=self.normal_image,
            borderwidth=0
        )

        # Binds the mouse enter and leave events
        self.bind("<Enter>", lambda event: self.config(image = self.active_image))
        self.bind("<Leave>", lambda event: self.config(image = self.normal_image))
