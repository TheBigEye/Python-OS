import time
import os
import tkinter as tk
from tkinter import *
from colorama import Back, Fore, Style, init

from PIL import Image, ImageTk


# ----------------------------------------------------------------[ Variables ]----------------------------------------------------------------------- #

# Color for the console
init(convert=True)

# Load the logo for the boot loader
with open('System\GUI\Objects\Logon', 'r', encoding='UTF-8') as Logon_archive:
    Logon_ASCII = Logon_archive.read()


# System variables (| Variable | True/False/int |)
Kernel_lvl = "NULL"  # Kernel main variable

Is_FAIL =           False  # 0
Is_in_BIOS =        False  # 1
Is_in_INSTALLER =   False  # 2
Is_in_Boot =        False  # 3
Is_in_Login =       False  # 4
Is_in_Desktop =     False  # 5
Is_Boot =           False  # NULL


# Colors (16 only | name | code |)
White =        "#FFFFFF"
Light_gray =   "#C0C0C0"
Dark_gray =    "#808080"
Black =        "#000000"
High_red =     "#FF0000"
Low_red =      "#800000"
Yellow =       "#FFFF00"
Brown =        "#808000"
Lime =         "#00FF00"
Green =        "#008000"
Aqua =         "#00FFFF"
Cyan =         "#008080"
High_blue =    "#0000FF"
Low_blue =     "#000080"
Magenta =      "#FF00FF"
Purple =       "#800080"


# Specific Colors
Login_background_color = "#477afb"
Login_entry_color = "#5A7EFC"


# --------------------------------------------------------------------------------------------------------------------------------------------------- #


Os = tk.Tk()  # Make the main window
Os.title("PythonOS")  # Window title
Os.iconbitmap("Assets/Images/icon.ico")  # Window icon

Os.geometry("1024x600")  # Window resolution
Os.resizable(0, 0)  # Not is rezisable
Os.configure(background=Black)  # Black is the color base


# Boot order

if Kernel_lvl == 0:  # Fail message

    Is_FAIL = True

elif Kernel_lvl == 1:  # BIOS Screen

    Is_in_BIOS = True

elif Kernel_lvl == 2:  # OS Installer

    Is_in_INSTALLER = True

elif Kernel_lvl == 3:  # Bootloader

    Is_in_Boot = True

elif Kernel_lvl == 4:  # Login Screen

    Is_in_Login = True

elif Kernel_lvl == 5:  # In the desktop

    Is_in_Desktop = True

elif Kernel_lvl == "NULL":  # Normal boot

    Is_Boot = True


# ---------------------------------------------------------------[ Boot code ]----------------------------------------------------------------------- #


def RSOD():  # Display the Red screen of death

    global Red_screen_of_death_GUI

    Os.configure(background=High_red)  # Sets the background to Red

    Red_screen_of_death_GUI = tk.PhotoImage(file="Assets/GUI/RSOD.png")
    Red_screen_of_death = tk.Label(Os, image=Red_screen_of_death_GUI, borderwidth=0.1)
    Red_screen_of_death.place(x=0, y=0)


def BIOS():  # Display the Bios window

    global Bios_Advanced_GUI

    Os.configure(background=High_blue)  # Sets the background to Blue

    Bios_Advanced_GUI = tk.PhotoImage(file="Assets/GUI/BIOS_Advanced_GUI.png")
    Bios_GUI = tk.Label(Os, image=Bios_Advanced_GUI, borderwidth=0.1)
    Bios_GUI.place(x=0, y=0)


def Os_Installer():  # Display the Post-Bios window (coming soon the OOBE)

    global Post_Bios_GUI

    Os.configure(background=Low_blue)  # Sets the background to Blue

    Post_Bios_GUI = tk.PhotoImage(file="Assets/GUI/Post_BIOS.png")
    Post_Bios = tk.Label(Os, image=Post_Bios_GUI, borderwidth=0.1)
    Post_Bios.place(x=0, y=0)


def Boot_loader(): 

    global Logon

    Os.configure(background=Black)  # Sets the background to Black

    Logon = tk.PhotoImage(file="Assets/logon.png")
    Boot_Logo = tk.Label(Os, image=Logon, borderwidth=0.1)
    Boot_Logo.place(x= 400, y= 160)

    # Loading animation
    frameCnt = 60
    frames = [
        PhotoImage(file="Assets/Loading.gif", format="gif -index %i" % (i))
        for i in range(frameCnt)
    ]

    def update(ind):

        frame = frames[ind]
        ind += 1

        if ind == frameCnt:
            ind = 0

        loading.configure(image=frame)
        Os.after(50, update, ind)

    loading = Label(Os, borderwidth=0.1)
    loading.place(x= 480, y= 400)

    def End_bootloader():

        Os.configure(background= Login_background_color)

        Boot_Logo.place(x= 1000, y= 1000)
        loading.place(x=1000, y= 1000)

        print ("Booted!")


    Os.after(1, update, 0)

    Os.after(10000, End_bootloader)


def Login():  # Display the login window

    global Login_GUI, Login_Button_icon

    Os.configure(background = Login_background_color)  # Sets the background to Blue

    Login_GUI = tk.PhotoImage(file = "Assets/GUI/Login.png")
    Login = tk.Label(Os, image= Login_GUI, borderwidth="0.1")
    Login.place(x=0, y=0)

    # Login entry (Password)
    Login_Password_Entry = Entry(Login, width= 20, show= "-", borderwidth= "0.1", fg= "White", background= Login_entry_color, font= ("Segou UI", 10))

    Login_Password_Entry.config(insertbackground= White)
    Login_Password_Entry.insert(0,"Password")
    Login_Password_Entry.focus()
    Login_Password_Entry.place(x= 435, y= 344)


    Login_Button_icon = tk.PhotoImage(file="Assets/Buttons/Login_Button.png")
    Login_Button = Button(Login, width=30, height=19, borderwidth="0", relief= "raised", image=Login_Button_icon) 
    Login_Button.place(x=495, y=384)  




# ---------------------------------------------------------------[ Boot order ]----------------------------------------------------------------------- #

def start_boot():

    def clearConsole():
        command = 'clear'

        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
            
        os.system(command)

    clearConsole()

    print(Logon_ASCII)

    time.sleep(3)

    print("Loading configuration...")

    time.sleep(1)

    print  ("Loaded!")

    time.sleep(2)

    print("Starting boot...")

    Boot_loader()


    Os.after(10255, Login) 



# Boot order in sections

if Is_FAIL == True:

    RSOD()

if Is_in_BIOS == True:

    BIOS()

if Is_in_INSTALLER == True:

    Os_Installer()

if Is_in_Boot == True:

    Boot_loader()

if Is_in_Login == True:

    Login()    


# Normal boot order
if Is_Boot == True:

    start_boot()
  

Os.mainloop()
