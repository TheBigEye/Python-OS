from tkinter import *
from System.GUI.Attributes.Draggable import make_draggable

__author__ = 'TheBigEye'
__version__ = '1.0'


def Display_MessageBox(master, type, title, message, draggable = False):

    """
    Create and display a Message box with title and personalized message.

    Parameters
    ----------
    `master` : string
        The parent where the Message box will be placed.

    `type` : string
        Type of Message box to be displayed: `Error`, `Warning`, `Info`.        

    `title` : string
        The title that the Message box will show.

    `message` : string
        The message that the Message box will show.

    `draggable` : boolean
        Specifies whether or not the Message box can be moved with the mouse.
                
    """

    global MessageBox, MessageBox_GUI_Image, Title_label, Message_label, Logo_Image, Ok_MessageBox_Image, Close_MessageBox_Image, Title_bg, Message_bg  # For avoid image problems

    if (type == "Error"):

        MessageBox_GUI_Image = PhotoImage(file = "Assets/GUI/Messagebox/Error_MessageBox.png")    

        Close_MessageBox_Image = PhotoImage(file="Assets/GUI/Messagebox/Close_Error_Button.png")
        Logo_Image = PhotoImage(file="Assets/GUI/Messagebox/Error.png")
        Ok_MessageBox_Image = PhotoImage(file="Assets/GUI/Messagebox/OK_Error_Button.png")

        Title_bg = "#CF3325"
        Message_bg = "#DE4142"

    if (type == "Info"):

        MessageBox_GUI_Image = PhotoImage(file = "Assets/GUI/Messagebox/Info_MessageBox.png")    

        Close_MessageBox_Image = PhotoImage(file="Assets/GUI/Messagebox/Close_Info_Button.png")
        Logo_Image = PhotoImage(file="Assets/GUI/Messagebox/Info.png")
        Ok_MessageBox_Image = PhotoImage(file="Assets/GUI/Messagebox/OK_Info_Button.png")

        Title_bg = "#388499"
        Message_bg = "#44A0BA" 

    if (type == "Warning"):

        MessageBox_GUI_Image = PhotoImage(file = "Assets/GUI/Messagebox/Warning_MessageBox.png")    

        Close_MessageBox_Image = PhotoImage(file="Assets/GUI/Messagebox/Close_Warning_Button.png")
        Logo_Image = PhotoImage(file="Assets/GUI/Messagebox/Warning.png")
        Ok_MessageBox_Image = PhotoImage(file="Assets/GUI/Messagebox/OK_Warning_Button.png")

        Title_bg = "#CC6A14"
        Message_bg = "#F98118"               



    MessageBox = Label(
        master,
        width=382,
        height=106,
        bg="white",
        image=MessageBox_GUI_Image,
        borderwidth="0",
    )

    Title_label = Label (
        MessageBox,
        width = 8,
        height = 1,
        bg = Title_bg,
        fg = "#FFFFFF",
        text = title,
        font=("Segou UI", 9)
    )
    
    Message_label = Label (
        MessageBox,
        width = 32,
        height = 1,
        bg = Message_bg,
        fg = "#FFFFFF",
        text = message,
        font=("Segou UI", 8)
    )

    Logo = Label (
        MessageBox,
        width = 32,
        height = 32,
        bg = Message_bg ,
        fg = "#FFFFFF",
        image = Logo_Image
    )

    def Close_MessageBox():
        """Close the Message box"""

        MessageBox.place_forget()

    Ok_button = Button(
        MessageBox,
        width=26,
        height=20,
        bg= Message_bg,
        image=Ok_MessageBox_Image,
        borderwidth="0",
        command=Close_MessageBox,    
    )

    Ok_button.place(x=343, y=78)


    Close_button = Button(
        MessageBox,
        width=7,
        height=7,
        bg= Title_bg,
        image= Close_MessageBox_Image,
        borderwidth="0",
        command=Close_MessageBox,
    )

    Close_button.place(x=359, y=11)    

    if (draggable == True):

        make_draggable(MessageBox)

    Title_label.place(x= 4, y= 5)
    Message_label.place(x= 28, y= 44)
    Logo.place(x= 12, y= 44)

    MessageBox.place(x= 320, y= 240)