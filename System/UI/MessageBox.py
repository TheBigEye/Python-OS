from tkinter import Button, Label
from typing import Literal

from System.UI.Attributes.Draggable import make_draggable
from System.Utils.Utils import Asset

__author__ = 'TheBigEye'
__version__ = '1.1'

Font = "Segou UI"

class MessageBox(Label):
    """
    Clase MessageBox
    """

    def __init__(self, master, type: Literal['Error', 'Info', 'Warning'], title: str, message: str, draggable: bool = True):

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

        Label.__init__(self, master)

        self.master = master
        self.type = type
        self.title = title
        self.message = message
        self.draggable = draggable


        # Error messagebox ------------------------------------------------------------------------------------------------------------

        if (self.type == "Error"):

            self.Error_title_bg = "#F95352"
            self.Error_message_bg = "#ffffff"


            global Error_MessageBox_GUI_Image, Error_MessageBox
            self.Error_MessageBox_GUI_Image = Asset("Error_MessageBox.png")

            self.Error_MessageBox = Label(
                self.master,
                width=382,
                height=106,
                bg="white",
                image=self.Error_MessageBox_GUI_Image,
                borderwidth="0",
            )


            self.Error_title_label = Label (
                self.Error_MessageBox,
                width = 8,
                height = 1,
                bg = self.Error_title_bg,
                fg = "#FFFFFF",
                text = self.title,
                font="Tahoma 8 bold"
            )


            self.Error_message_label = Label (
                self.Error_MessageBox,
                width = 32,
                height = 1,
                bg = self.Error_message_bg,
                fg = "#000000",
                text = self.message,
                font="Tahoma 8"
            )


            self.Error_logo_image = Asset("Error.png")

            self.Error_logo = Label (
                self.Error_MessageBox,
                width = 32,
                height = 32,
                bg = self.Error_message_bg ,
                fg = "#FFFFFF",
                image = self.Error_logo_image
            )


            def Error_close_messagebox():
                """Close the Message box"""

                self.Error_MessageBox.place_forget()


            self.Error_OK_button_image = Asset("OK_button.png")

            self.Error_OK_button = Button(
                self.Error_MessageBox,
                width=28,
                height=21,
                bg= self.Error_message_bg,
                image=self.Error_OK_button_image,
                borderwidth="0",
                command=Error_close_messagebox,
            )

            self.Error_OK_button.place(x=343, y=78)


            self.Error_close_button_image = Asset("Close_error_button.png")
            self.Error_close_button_light_image = Asset("Close_error_button_light.png")

            self.Error_close_button = Button(
                self.Error_MessageBox,
                width=13,
                height=13,
                bg= self.Error_title_bg,
                image= self.Error_close_button_image,
                borderwidth="0",
                command=Error_close_messagebox,
            )

            # Change the image when the mouse is over the button
            self.Error_close_button.bind("<Enter>", lambda event: self.Error_close_button.config(image=self.Error_close_button_light_image))
            self.Error_close_button.bind("<Leave>", lambda event: self.Error_close_button.config(image=self.Error_close_button_image))

            self.Error_close_button.place(x=362, y=4)

            if (self.draggable == True):

                make_draggable(self.Error_MessageBox)

            self.Error_title_label.place(x= 11, y= 1)
            self.Error_message_label.place(x= 20, y= 32)
            self.Error_logo.place(x= 18, y= 32)

            self.Error_MessageBox.place(x= 320, y= 240)


    # Info messagebox -------------------------------------------------------------------------------------------------------------

        if (self.type == "Info"):

            global Info_Title_bg, Info_Message_bg
            self.Info_Title_bg = "#67B4C8"
            self.Info_Message_bg = "#ffffff"


            global Info_MessageBox_GUI_Image, Info_MessageBox
            self.Info_MessageBox_GUI_Image = Asset("Info_MessageBox.png")

            self.Info_MessageBox = Label(
                self.master,
                width=382,
                height=106,
                bg="white",
                image=self.Info_MessageBox_GUI_Image,
                borderwidth="0",
            )


            self.Info_Title_label = Label (
                self.Info_MessageBox,
                width = 8,
                height = 1,
                bg = self.Info_Title_bg,
                fg = "#FFFFFF",
                text = self.title,
                font="Tahoma 8 bold"
            )


            self.Info_Message_label = Label (
                self.Info_MessageBox,
                width = 32,
                height = 1,
                bg = self.Info_Message_bg,
                fg = "#000000",
                text = self.message,
                font="Tahoma 8"
            )


            global Info_Logo_Image, Info_Logo
            self.Info_Logo_Image = Asset("Info.png")

            self.Info_Logo = Label (
                self.Info_MessageBox,
                width = 32,
                height = 32,
                bg = self.Info_Message_bg ,
                fg = "#FFFFFF",
                image = self.Info_Logo_Image
            )


            global Info_Close_MessageBox
            def Info_Close_MessageBox():
                """Close the Message box"""

                self.Info_MessageBox.place_forget()


            global Info_Ok_MessageBox_Image, Info_Ok_button
            self.Info_Ok_MessageBox_Image = Asset("OK_button.png")

            self.Info_Ok_button = Button(
                self.Info_MessageBox,
                width=28,
                height=21,
                bg= self.Info_Message_bg,
                image=self.Info_Ok_MessageBox_Image,
                borderwidth="0",
                command=Info_Close_MessageBox,
            )

            self.Info_Ok_button.place(x=343, y=78)


            self.Info_close_button_image = Asset("Close_info_button.png")
            self.Info_close_button_light_image = Asset("Close_info_button_light.png")

            self.Info_close_button = Button(
                self.Info_MessageBox,
                width=13,
                height=13,
                bg= self.Info_Title_bg,
                image= self.Info_close_button_image,
                borderwidth="0",
                command=Info_Close_MessageBox,
            )

            # Change the image when the mouse is over the button
            self.Info_close_button.bind("<Enter>", lambda event: self.Info_close_button.config(image=self.Info_close_button_light_image))
            self.Info_close_button.bind("<Leave>", lambda event: self.Info_close_button.config(image=self.Info_close_button_image))

            self.Info_close_button.place(x=362, y=4)


            if (self.draggable == True):

                make_draggable(self.Info_MessageBox)


            self.Info_Title_label.place(x= 11, y= 1)
            self.Info_Message_label.place(x= 20, y= 32)
            self.Info_Logo.place(x= 18, y= 32)

            self.Info_MessageBox.place(x= 320, y= 240)


    # Warning messagebox ----------------------------------------------------------------------------------------------------------

        if (self.type == "Warning"):


            global Warning_Title_bg, Warning_Message_bg
            self.Warning_Title_bg = "#F98052"
            self.Warning_Message_bg = "#Ffffff"


            global Warning_MessageBox_GUI_Image, Warning_MessageBox
            self.Warning_MessageBox_GUI_Image = Asset("Warning_MessageBox.png")

            self.Warning_MessageBox = Label(
                self.master,
                width=382,
                height=106,
                bg="white",
                image=self.Warning_MessageBox_GUI_Image,
                borderwidth="0",
            )

            self.Warning_Title_label = Label (
                self.Warning_MessageBox,
                width = 8,
                height = 1,
                bg = self.Warning_Title_bg,
                fg = "#FFFFFF",
                text = self.title,
                font="Tahoma 8 bold"
            )

            self.Warning_Message_label = Label (
                self.Warning_MessageBox,
                width = 32,
                height = 1,
                bg = self.Warning_Message_bg,
                fg = "#000000",
                text = self.message,
                font="Tahoma 8"
            )


            global Warning_Logo_Image, Warning_Logo
            self.Warning_Logo_Image = Asset("Warning.png")

            self.Warning_Logo = Label (
                self.Warning_MessageBox,
                width = 32,
                height = 32,
                bg = self.Warning_Message_bg ,
                fg = "#FFFFFF",
                image = self.Warning_Logo_Image
            )


            global Warning_Close_MessageBox
            def Warning_Close_MessageBox():
                """Close the Message box"""

                self.Warning_MessageBox.place_forget()


            global Warning_Ok_MessageBox_Image, Warning_Ok_button
            self.Warning_Ok_MessageBox_Image = Asset("OK_button.png")

            self.Warning_Ok_button = Button(
                self.Warning_MessageBox,
                width=28,
                height=21,
                bg= self.Warning_Message_bg,
                image=self.Warning_Ok_MessageBox_Image,
                borderwidth="0",
                command=Warning_Close_MessageBox,
            )

            self.Warning_Ok_button.place(x=343, y=78)


            self.Warning_close_button_image = Asset("Close_warning_button.png")
            self.Warning_close_button_light_image = Asset("Close_warning_button_light.png")

            self.Warning_close_button= Button(
                self.Warning_MessageBox,
                width=13,
                height=13,
                bg= self.Warning_Title_bg,
                image= self.Warning_close_button_image,
                borderwidth="0",
                command=Warning_Close_MessageBox,
            )

            # Change the image when the mouse is over the button
            self.Warning_close_button.bind("<Enter>", lambda event: self.Warning_close_button.config(image=self.Warning_close_button_light_image))
            self.Warning_close_button.bind("<Leave>", lambda event: self.Warning_close_button.config(image=self.Warning_close_button_image))

            self.Warning_close_button.place(x=362, y=4)

            if (draggable == True):

                make_draggable(self.Warning_MessageBox)

            self.Warning_Title_label.place(x= 11, y= 1)
            self.Warning_Message_label.place(x= 20, y= 32)
            self.Warning_Logo.place(x= 18, y= 32)

            self.Warning_MessageBox.place(x= 320, y= 240)
