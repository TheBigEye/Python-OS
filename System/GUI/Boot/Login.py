from System.Utils.Colormap import White
from tkinter import Button, Entry, Label

from System.Utils.Utils import get_asset

__author__ = 'TheBigEye'
__version__ = '2.0'

# Specific Colors
Login_background_color = "#477afb"
Login_entry_color = "#5A7EFC"

def Login(master):  # Display the login window

    global Login_GUI, Login_Button_icon

    master.configure(background = Login_background_color)  # Sets the background to Blue

    Login_GUI = get_asset("Assets/GUI/Login.png")
    Login = Label(master, image = Login_GUI, borderwidth="0.1")
    Login.place(x=0, y=0)

    # Login entry (Password)
    Login_Password_Entry = Entry(
        Login,
        width = 20,
        show = "•",
        borderwidth = "0.1",
        fg = "White",
        background = Login_entry_color,
        font = ("Segou UI", 10)
    )

    Login_Password_Entry.config(insertbackground= White)
    Login_Password_Entry.insert(0,"Password")
    Login_Password_Entry.focus()
    Login_Password_Entry.place(x= 435, y= 344)

    Login_Button_icon = get_asset("Assets/Buttons/Login_Button.png")
    Login_Button = Button(Login,
        width = 30,
        height = 19,
        borderwidth = "0",
        relief = "raised",
        image = Login_Button_icon
    )
    Login_Button.place(x = 495, y = 384)