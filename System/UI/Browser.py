from tkinter import Label
import tkinterweb
from System.UI.Attributes.Draggable import make_draggable
from System.Utils.Utils import Asset
from System.Utils.Vars import Assets_directory

__author__ = 'TheBigEye'
__version__ = '1.1'

# TODO: remove and replace it with a more efficient fucntion.


def Display_Browser(master, draggable: bool = False):

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

# Navegaador ---------------------------------------------------------------------------------------------------------------

    global Browser, Browser_GUI_Image
    Browser_GUI_Image = Asset("Browser.png")

    Browser = Label(
        master,
        bg= "white",
        image=Browser_GUI_Image,
        borderwidth="0",
    )

    Browser.place(x= 32, y= 32)

    if (draggable == True):

        make_draggable(Browser)

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


