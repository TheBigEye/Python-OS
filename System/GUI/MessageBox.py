from tkinter import Button, Label
from System.GUI.Attributes.Draggable import make_draggable
from System.Utils.Utils import get_asset

__author__ = 'TheBigEye'
__version__ = '1.1'

Font = "Segou UI"

class MessageBox(Label):
    """
    Clase MessageBox
    """

    def __init__(self, master, type, title, message, draggable = True):

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


            global Error_Title_bg, Error_Message_bg
            self.Error_Title_bg = "#CF3325"
            self.Error_Message_bg = "#ffffff"


            global Error_MessageBox_GUI_Image, Error_MessageBox
            self.Error_MessageBox_GUI_Image = get_asset("Assets/GUI/Messagebox/Error_MessageBox.png")

            self.Error_MessageBox = Label(
                self.master,
                width=382,
                height=106,
                bg="white",
                image=self.Error_MessageBox_GUI_Image,
                borderwidth="0",
            )


            global Error_Title_label
            self.Error_Title_label = Label (
                self.Error_MessageBox,
                width = 8,
                height = 1,
                bg = self.Error_Title_bg,
                fg = "#FFFFFF",
                text = self.title,
                font=(Font, 9)
            )


            global Error_Message_label
            self.Error_Message_label = Label (
                self.Error_MessageBox,
                width = 32,
                height = 1,
                bg = self.Error_Message_bg,
                fg = "#000000",
                text = self.message,
                font=(Font, 8)
            )


            global Error_Logo_Image, Error_Logo
            self.Error_Logo_Image = get_asset("Assets/GUI/Messagebox/Error.png")

            self.Error_Logo = Label (
                self.Error_MessageBox,
                width = 32,
                height = 32,
                bg = self.Error_Message_bg ,
                fg = "#FFFFFF",
                image = self.Error_Logo_Image
            )


            global Error_Close_MessageBox
            def Error_Close_MessageBox():
                """Close the Message box"""

                self.Error_MessageBox.place_forget()


            global Error_Ok_MessageBox_Image, Error_Ok_button
            self.Error_Ok_MessageBox_Image = get_asset("Assets/GUI/Messagebox/OK_Error_Button.png")

            self.Error_Ok_button = Button(
                self.Error_MessageBox,
                width=28,
                height=22,
                bg= self.Error_Message_bg,
                image=self.Error_Ok_MessageBox_Image,
                borderwidth="0",
                command=Error_Close_MessageBox,
            )

            self.Error_Ok_button.place(x=343, y=78)


            global Error_Close_MessageBox_Image
            self.Error_Close_MessageBox_Image = get_asset("Assets/GUI/Messagebox/Close_Error_Button.png")

            self.Error_Close_button = Button(
                self.Error_MessageBox,
                width=7,
                height=7,
                bg= self.Error_Title_bg,
                image= self.Error_Close_MessageBox_Image,
                borderwidth="0",
                command=Error_Close_MessageBox,
            )

            self.Error_Close_button.place(x=359, y=11)


            if (self.draggable == True):

                make_draggable(self.Error_MessageBox)

            self.Error_Title_label.place(x= 4, y= 5)
            self.Error_Message_label.place(x= 20, y= 44)
            self.Error_Logo.place(x= 18, y= 44)

            self.Error_MessageBox.place(x= 320, y= 240)


    # Info messagebox -------------------------------------------------------------------------------------------------------------

        if (self.type == "Info"):

            global Info_Title_bg, Info_Message_bg
            self.Info_Title_bg = "#388499"
            self.Info_Message_bg = "#ffffff"


            global Info_MessageBox_GUI_Image, Info_MessageBox
            self.Info_MessageBox_GUI_Image = get_asset("Assets/GUI/Messagebox/Info_MessageBox.png")

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
                font=(Font, 9)
            )


            self.Info_Message_label = Label (
                self.Info_MessageBox,
                width = 32,
                height = 1,
                bg = self.Info_Message_bg,
                fg = "#000000",
                text = self.message,
                font=(Font, 8)
            )


            global Info_Logo_Image, Info_Logo
            self.Info_Logo_Image = get_asset("Assets/GUI/Messagebox/Info.png")

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
            self.Info_Ok_MessageBox_Image = get_asset("Assets/GUI/Messagebox/OK_Info_Button.png")

            self.Info_Ok_button = Button(
                self.Info_MessageBox,
                width=28,
                height=22,
                bg= self.Info_Message_bg,
                image=self.Info_Ok_MessageBox_Image,
                borderwidth="0",
                command=Info_Close_MessageBox,
            )

            self.Info_Ok_button.place(x=343, y=78)


            global Info_Close_MessageBox_Image, Info_Close_button
            self.Info_Close_MessageBox_Image = get_asset("Assets/GUI/Messagebox/Close_Info_Button.png")

            self.Info_Close_button = Button(
                self.Info_MessageBox,
                width=7,
                height=7,
                bg= self.Info_Title_bg,
                image= self.Info_Close_MessageBox_Image,
                borderwidth="0",
                command=Info_Close_MessageBox,
            )

            self.Info_Close_button.place(x=359, y=11)


            if (self.draggable == True):

                make_draggable(self.Info_MessageBox)


            self.Info_Title_label.place(x= 4, y= 5)
            self.Info_Message_label.place(x= 20, y= 44)
            self.Info_Logo.place(x= 18, y= 44)

            self.Info_MessageBox.place(x= 320, y= 240)


    # Warning messagebox ----------------------------------------------------------------------------------------------------------

        if (self.type == "Warning"):


            global Warning_Title_bg, Warning_Message_bg
            self.Warning_Title_bg = "#CC6A14"
            self.Warning_Message_bg = "#Ffffff"


            global Warning_MessageBox_GUI_Image, Warning_MessageBox
            self.Warning_MessageBox_GUI_Image = get_asset("Assets/GUI/Messagebox/Warning_MessageBox.png")

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
                font=(Font, 9)
            )

            self.Warning_Message_label = Label (
                self.Warning_MessageBox,
                width = 32,
                height = 1,
                bg = self.Warning_Message_bg,
                fg = "#000000",
                text = self.message,
                font=(Font, 8)
            )


            global Warning_Logo_Image, Warning_Logo
            self.Warning_Logo_Image = get_asset("Assets/GUI/Messagebox/Warning.png")

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
            self.Warning_Ok_MessageBox_Image = get_asset("Assets/GUI/Messagebox/OK_Warning_Button.png")

            self.Warning_Ok_button = Button(
                self.Warning_MessageBox,
                width=28,
                height=22,
                bg= self.Warning_Message_bg,
                image=self.Warning_Ok_MessageBox_Image,
                borderwidth="0",
                command=Warning_Close_MessageBox,
            )

            self.Warning_Ok_button.place(x=343, y=78)


            global Warning_Close_MessageBox_Image, Warning_Close_button
            self.Warning_Close_MessageBox_Image = get_asset("Assets/GUI/Messagebox/Close_Warning_Button.png")

            self.Warning_Close_button = Button(
                self.Warning_MessageBox,
                width=7,
                height=7,
                bg= self.Warning_Title_bg,
                image= self.Warning_Close_MessageBox_Image,
                borderwidth="0",
                command=Warning_Close_MessageBox,
            )

            self.Warning_Close_button.place(x=359, y=11)

            if (draggable == True):

                make_draggable(self.Warning_MessageBox)

            self.Warning_Title_label.place(x= 4, y= 5)
            self.Warning_Message_label.place(x= 20, y= 44)
            self.Warning_Logo.place(x= 18, y= 44)

            self.Warning_MessageBox.place(x= 320, y= 240)