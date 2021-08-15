from tkinter import *
from System.GUI.Attributes.Draggable import make_draggable

__author__ = 'TheBigEye'
__version__ = '1.1'



def Display_MessageBox(master, type, title, message, draggable = False):

    # Documentation -----------------------------------------------------------------------------------------------------------

    """
    Create and display a Message box with title and personalized message.

    Parameters
    ----------
    `master` : string
        The parent where the Message box will be placed.

    `type` : string
        Type of Message box to be displayed: `Error`, `Warning`, `Info`, (this is obligatory for it to work).

    `title` : string
        The title that the Message box will show.

    `message` : string
        The message that the Message box will show.

    `draggable` : boolean
        Specifies whether or not the Message box can be moved with the mouse.

    """

    # Error messagebox global variables ---------------------------------------------------------------------------------------
    global Error_MessageBox_GUI_Image, Error_Close_MessageBox_Image, Error_Logo_Image, Error_Ok_MessageBox_Image # Images
    global Error_Title_bg, Error_Message_bg # Colors
    global Error_MessageBox, Error_Title_label, Error_Message_label, Error_Logo, Error_Close_MessageBox, Error_Ok_button, Error_Close_button # Functions

    # Info messagebox global variables ----------------------------------------------------------------------------------------
    global Info_MessageBox_GUI_Image, Info_Close_MessageBox_Image, Info_Logo_Image, Info_Ok_MessageBox_Image
    global Info_Title_bg, Info_Message_bg
    global Info_MessageBox, Info_Title_label, Info_Message_label, Info_Logo, Info_Close_MessageBox, Info_Ok_button, Info_Close_button

    # Warning messagebox global variables -------------------------------------------------------------------------------------
    global Warning_MessageBox_GUI_Image, Warning_Close_MessageBox_Image, Warning_Logo_Image, Warning_Ok_MessageBox_Image
    global Warning_Title_bg, Warning_Message_bg
    global Warning_MessageBox, Warning_Title_label, Warning_Message_label, Warning_Logo, Warning_Close_MessageBox, Warning_Ok_button, Warning_Close_button


# Error messagebox ------------------------------------------------------------------------------------------------------------

    if (type == "Error"):

        Error_MessageBox_GUI_Image = PhotoImage(file = "Assets/GUI/Messagebox/Error_MessageBox.png")

        Error_Close_MessageBox_Image = PhotoImage(file="Assets/GUI/Messagebox/Close_Error_Button.png")
        Error_Logo_Image = PhotoImage(file="Assets/GUI/Messagebox/Error.png")
        Error_Ok_MessageBox_Image = PhotoImage(file="Assets/GUI/Messagebox/OK_Error_Button.png")

        Error_Title_bg = "#CF3325"
        Error_Message_bg = "#DE4142"

        Error_MessageBox = Label(
            master,
            width=382,
            height=106,
            bg="white",
            image=Error_MessageBox_GUI_Image,
            borderwidth="0",
        )

        Error_Title_label = Label (
            Error_MessageBox,
            width = 8,
            height = 1,
            bg = Error_Title_bg,
            fg = "#FFFFFF",
            text = title,
            font=("Segou UI", 9)
        )

        Error_Message_label = Label (
            Error_MessageBox,
            width = 32,
            height = 1,
            bg = Error_Message_bg,
            fg = "#FFFFFF",
            text = message,
            font=("Segou UI", 8)
        )

        Error_Logo = Label (
            Error_MessageBox,
            width = 32,
            height = 32,
            bg = Error_Message_bg ,
            fg = "#FFFFFF",
            image = Error_Logo_Image
        )

        def Error_Close_MessageBox():
            """Close the Message box"""

            Error_MessageBox.place_forget()

        Error_Ok_button = Button(
            Error_MessageBox,
            width=26,
            height=20,
            bg= Error_Message_bg,
            image=Error_Ok_MessageBox_Image,
            borderwidth="0",
            command=Error_Close_MessageBox,
        )

        Error_Ok_button.place(x=343, y=78)


        Error_Close_button = Button(
            Error_MessageBox,
            width=7,
            height=7,
            bg= Error_Title_bg,
            image= Error_Close_MessageBox_Image,
            borderwidth="0",
            command=Error_Close_MessageBox,
        )

        Error_Close_button.place(x=359, y=11)

        if (draggable == True):

            make_draggable(Error_MessageBox)

        Error_Title_label.place(x= 4, y= 5)
        Error_Message_label.place(x= 28, y= 44)
        Error_Logo.place(x= 12, y= 44)

        Error_MessageBox.place(x= 320, y= 240)


# Info messagebox -------------------------------------------------------------------------------------------------------------

    if (type == "Info"):

        Info_MessageBox_GUI_Image = PhotoImage(file = "Assets/GUI/Messagebox/Info_MessageBox.png")

        Info_Close_MessageBox_Image = PhotoImage(file="Assets/GUI/Messagebox/Close_Info_Button.png")
        Info_Logo_Image = PhotoImage(file="Assets/GUI/Messagebox/Info.png")
        Info_Ok_MessageBox_Image = PhotoImage(file="Assets/GUI/Messagebox/OK_Info_Button.png")

        Info_Title_bg = "#388499"
        Info_Message_bg = "#44A0BA"

        Info_MessageBox = Label(
            master,
            width=382,
            height=106,
            bg="white",
            image=Info_MessageBox_GUI_Image,
            borderwidth="0",
        )

        Info_Title_label = Label (
            Info_MessageBox,
            width = 8,
            height = 1,
            bg = Info_Title_bg,
            fg = "#FFFFFF",
            text = title,
            font=("Segou UI", 9)
        )

        Info_Message_label = Label (
            Info_MessageBox,
            width = 32,
            height = 1,
            bg = Info_Message_bg,
            fg = "#FFFFFF",
            text = message,
            font=("Segou UI", 8)
        )

        Info_Logo = Label (
            Info_MessageBox,
            width = 32,
            height = 32,
            bg = Info_Message_bg ,
            fg = "#FFFFFF",
            image = Info_Logo_Image
        )

        def Info_Close_MessageBox():
            """Close the Message box"""

            Info_MessageBox.place_forget()

        Info_Ok_button = Button(
            Info_MessageBox,
            width=26,
            height=20,
            bg= Info_Message_bg,
            image=Info_Ok_MessageBox_Image,
            borderwidth="0",
            command=Info_Close_MessageBox,
        )

        Info_Ok_button.place(x=343, y=78)


        Info_Close_button = Button(
            Info_MessageBox,
            width=7,
            height=7,
            bg= Info_Title_bg,
            image= Info_Close_MessageBox_Image,
            borderwidth="0",
            command=Info_Close_MessageBox,
        )

        Info_Close_button.place(x=359, y=11)

        if (draggable == True):

            make_draggable(Info_MessageBox)

        Info_Title_label.place(x= 4, y= 5)
        Info_Message_label.place(x= 28, y= 44)
        Info_Logo.place(x= 12, y= 44)

        Info_MessageBox.place(x= 320, y= 240)


# Warning messagebox ----------------------------------------------------------------------------------------------------------

    if (type == "Warning"):

        Warning_MessageBox_GUI_Image = PhotoImage(file = "Assets/GUI/Messagebox/Warning_MessageBox.png")

        Warning_Close_MessageBox_Image = PhotoImage(file="Assets/GUI/Messagebox/Close_Warning_Button.png")
        Warning_Logo_Image = PhotoImage(file="Assets/GUI/Messagebox/Warning.png")
        Warning_Ok_MessageBox_Image = PhotoImage(file="Assets/GUI/Messagebox/OK_Warning_Button.png")

        Warning_Title_bg = "#CC6A14"
        Warning_Message_bg = "#F98118"

        Warning_MessageBox = Label(
            master,
            width=382,
            height=106,
            bg="white",
            image=Warning_MessageBox_GUI_Image,
            borderwidth="0",
        )

        Warning_Title_label = Label (
            Warning_MessageBox,
            width = 8,
            height = 1,
            bg = Warning_Title_bg,
            fg = "#FFFFFF",
            text = title,
            font=("Segou UI", 9)
        )

        Warning_Message_label = Label (
            Warning_MessageBox,
            width = 32,
            height = 1,
            bg = Warning_Message_bg,
            fg = "#FFFFFF",
            text = message,
            font=("Segou UI", 8)
        )

        Warning_Logo = Label (
            Warning_MessageBox,
            width = 32,
            height = 32,
            bg = Warning_Message_bg ,
            fg = "#FFFFFF",
            image = Warning_Logo_Image
        )

        def Warning_Close_MessageBox():
            """Close the Message box"""

            Warning_MessageBox.place_forget()

        Warning_Ok_button = Button(
            Warning_MessageBox,
            width=26,
            height=20,
            bg= Warning_Message_bg,
            image=Warning_Ok_MessageBox_Image,
            borderwidth="0",
            command=Warning_Close_MessageBox,
        )

        Warning_Ok_button.place(x=343, y=78)


        Warning_Close_button = Button(
            Warning_MessageBox,
            width=7,
            height=7,
            bg= Warning_Title_bg,
            image= Warning_Close_MessageBox_Image,
            borderwidth="0",
            command=Warning_Close_MessageBox,
        )

        Warning_Close_button.place(x=359, y=11)

        if (draggable == True):

            make_draggable(Warning_MessageBox)

        Warning_Title_label.place(x= 4, y= 5)
        Warning_Message_label.place(x= 28, y= 44)
        Warning_Logo.place(x= 12, y= 44)

        Warning_MessageBox.place(x= 320, y= 240)
