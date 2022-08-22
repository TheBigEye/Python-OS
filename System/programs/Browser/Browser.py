from tkinter import Label
import tkinterweb
from Libs.pyImage.Image import Image
from System.utils.vars import Assets_directory

__author__ = 'TheBigEye'
__version__ = '1.1'

# TODO: remove and replace it with a more efficient function.


def Browser(master):

# Documentation ---------------------------------------------------------------------------------------------------------------

    """
    Create and display the web browser.

    Parameters:
    `master` : string
        The parent where the Browser will be placed.

    `draggable` : boolean
        If True, the browser will be draggable.

    Returns:
    None
    """

# Browser ---------------------------------------------------------------------------------------------------------------

    global Browser, Browser_GUI_Image
    Browser_GUI_Image = Image.setImage("Assets/Shell/Programs/Browser/Browser.png")

    Browser = Label(
        master,
        bg= "white",
        image=Browser_GUI_Image,
        borderwidth="0",
    )

    Browser.place(x= 32, y= 32)

    Browser_frame = Label(
        Browser,
        width=137,
        height=32,
        borderwidth="0",
        bg= "white",
    )

    Browser_frame.place(x=0, y=74)

    Page_frame= tkinterweb.HtmlFrame(Browser_frame, messages_enabled = False)
    Page_frame.load_website('http://google.com')

    Page_frame.place(x= 68, y= 0)
