from tkinter import Misc, Button, PhotoImage
from Libs.pyImage.Image import getTkColor, setImage


def Taskbar_button(master: Misc, button_image_path, master_image_path, position: tuple):
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

    bright = 12

    image_color = getTkColor(master_image_path, position[0], position[1])
    image_active_color = ("#%02x%02x%02x" % (int(image_color[1:3], 16) + bright, int(image_color[3:5], 16) + bright, int(image_color[5:7], 16) + bright))

    normal_image = setImage(button_image_path, (24, 24), "#ff00ff", image_color)
    active_image = setImage(button_image_path, (24, 24), "#ff00ff", image_active_color)

    # Creates the button
    task_button = Button(
        master,
        relief="flat",
        bg=image_color,
        activebackground=image_active_color,
        image=normal_image,
        borderwidth=0
    )

    # Binds the mouse enter and leave events
    task_button.bind("<Enter>", lambda event: task_button.config(image = active_image))
    task_button.bind("<Leave>", lambda event: task_button.config(image = normal_image))

    return task_button
