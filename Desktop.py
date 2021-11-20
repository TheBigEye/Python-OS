# ---------------------------- License - Read pls -------------------------------- #
#                                                                                   #
#     TheBigEye - Python operating system simulator                                 #
#     Copyright (C) 2021                                                            #
#                                                                                   #
#     This program is free software: you can redistribute it and/or modify          #
#     it under the terms of the GNU General Public License as published by          #
#     the Free Software Foundation, either version 3 of the License, or             #
#     (at your option) any later version.                                           #
#                                                                                   #
#     This program is distributed in the hope that it will be useful,               #
#     but WITHOUT ANY WARRANTY; without even the implied warranty of                #
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                 #
#     GNU General Public License for more details.                                  #
#                                                                                   #
#     You should have received a copy of the GNU General Public License             #
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.         #
#                                                                                   #
#                                                                                   #
#     NOTICE: The program or software was made for educational / theoretical        #
#     topics about the operation of the real operating system, some of the          #
#     resources, sounds and images used are from Windows and continue to be         #
#     from Microsoft (Until I replace them of course ...)                           #
# --------------------------------------------------------------------------------- #


from System.GUI.Terminal import Display_Terminal
from System.GUI.MessageBox import Display_MessageBox # MessageBox package
from System.GUI.FileManager import Display_FileManager # FileManager package
from tkinter import Button, Label  
import tkinter as tk
import time

Ventana = tk.Tk()
Ventana.title("PythonOS")
Ventana.geometry("1024x600")
Ventana.resizable(0, 0)
Ventana.configure(background="#000000")
Ventana.iconbitmap("Assets\Images\icon.ico")

# Variables
Wallpaper = "BlissHill"

Contextual_Menu_BG_Color = "#ffffff"
Start_Menu_image_BG_Color = "#ffffff"
FileManager_BG_Color = "#ffffff"

# Wallpaper
Background_image = tk.PhotoImage(file = "Assets/Wallpapers/BlissHill.png")
Background = tk.Label(Ventana, image = Background_image)
Background.place(x = -1, y = -1, relwidth = 1, relheight = 1)

Default_Taskbar_x = 50
Default_Taskbar_y = 571


# ----------------------------------------------------------------[ Resources ]----------------------------------------------------------------------- #

# ---------------------------------------------------------------------------------- #
#    Here the addresses of all the images, sounds and resources used are specified   #
#    To make it more comfortable, I will put a numbering so that it is by order      #
#                                                                                    #
#    so organized I am XD...                                                         #
# ---------------------------------------------------------------------------------- #

# GUI
Taskbar_GUI_Image = tk.PhotoImage(file = "Assets/GUI/Taskbar.png")                                              # Taskbar
Clockbar_GUI_Image = tk.PhotoImage(file = "Assets/GUI/Clockbar.png")                                            # Clockbar
StartMenu_GUI_Image = tk.PhotoImage(file = "Assets/GUI/StartMenu.png")                                          # Start Menu
FileManager_GUI_Image = tk.PhotoImage(file = "Assets/GUI/FileManager.png")                                      # File Manager

# Taskbar Buttons
StartMenu_TB_Button_Image = tk.PhotoImage(file = "Assets/Buttons/Start_Button.png")                             # Start Menu
Search_TB_Button_Image = tk.PhotoImage(file = "Assets/Buttons/SearchTaskIcon.png")                              # Search
Browser_TB_Button_Image = tk.PhotoImage(file = "Assets/Buttons/BrowserTaskIcon.png")                            # Browser
FileManager_TB_Button_Image = tk.PhotoImage(file = "Assets/Buttons/FileManagerTaskIcon.png")                    # File Manager

# Window buttons
Close_WD_button_image = tk.PhotoImage(file = "Assets/Buttons/Close_white.png")

# -----------------------------------------------------------------[ Taskbar ]------------------------------------------------------------------------ #


# Taskbar GUI
Taskbar = Label(

    Ventana,
    width = 974,
    height = 29,
    borderwidth = "0",
    image = Taskbar_GUI_Image,
    background = "black",
    foreground = "gray",
    relief = "raised",

)
Taskbar.place(x=Default_Taskbar_x, y=Default_Taskbar_y)



# ---------------------------------------------------------------[ Start menu ]----------------------------------------------------------------------- #



# Start menu GUI
StartMenu = Label(

    Ventana,
    width = 314,
    height = 440,
    image = StartMenu_GUI_Image,
    borderwidth = "0"

)

# Open
def Open_StartMenu():
    StartMenu.place(x = 1, y = 126)
    time.sleep(0.1)

    Open_Start_Button.place_forget()
    Close_Start_Button.place(x = 0, y = 571)


# Close
def Close_StartMenu():

    StartMenu.place_forget()
    time.sleep(0.1)

    Open_Start_Button.place(x = 0, y = 571)
    Close_Start_Button.place_forget()



# Start buttons
Open_Start_Button = Button(
    Ventana,
    width = 48,
    height = 28,
    borderwidth = "0",
    bg = "black",
    relief = "raised",
    image = StartMenu_TB_Button_Image,
    command = Open_StartMenu,
)
Open_Start_Button.place(x = 0, y = 571)

Close_Start_Button = Button(
    Ventana,
    width = 48,
    height = 28,
    borderwidth = "0",
    bg = "black",
    relief = "raised",
    image = StartMenu_TB_Button_Image,
    command = Close_StartMenu,
)
Close_Start_Button.place_forget()

# ================================================== Error types ======================================================

def Settings_error():
    Close_StartMenu()
    Display_MessageBox(Ventana, "Error", "Settings.py", "In development, this is a test", draggable = False)

def Print_error():
    Close_StartMenu()
    Display_MessageBox(Ventana, "Info", "Spoolvs.py", "this is a test", draggable = False)

def This_PC_error():
    Close_StartMenu()
    Display_MessageBox(Ventana, "Warning", "Core.py", "In development", draggable = False)

def FileManager_error():
    Close_StartMenu()
    Display_MessageBox(Ventana, "Error", "Explorer.py", "lol", draggable = False)


# =================================================== Programs ========================================================


def FileManager():
    Close_StartMenu()
    Display_FileManager(Ventana, "This PC", draggable = True)

def Terminal():
    Close_StartMenu()
    Display_Terminal(Ventana, draggable = True)    


# ============================================== Taskbar icons ========================================================

Search_task_icon = Button(
    Taskbar,
    width=43,
    height=25,
    borderwidth="0",
    relief="raised",
    bg="#080D11",
    image=Search_TB_Button_Image,
    command=Terminal,
)
Search_task_icon.place(x=-12, y=2)

FileManager_task_icon = Button(
    Taskbar,
    width=43,
    height=25,
    borderwidth="0",
    relief="raised",
    bg="#080D11",
    image=FileManager_TB_Button_Image,
    command=FileManager,
)
FileManager_task_icon.place(x=24, y=2)

Browser_task_icon = Button(
    Taskbar,
    width=43,
    height=25,
    borderwidth="0",
    relief="raised",
    bg="#080D11",
    image=Browser_TB_Button_Image,
    command=FileManager,
)
Browser_task_icon.place(x=64, y=2)


# Taskbar icons base (volume, internet, battery, etc)
Taskbar_Icons_image = tk.PhotoImage(file="Assets/Taskbar_Icons.png")

Taskbar_Icons = Label(
    Taskbar,
    width=100,
    height=28,
    borderwidth="0",
    relief="raised",
    bg="#080D11",
    image=Taskbar_Icons_image,
)
Taskbar_Icons.place(x=824, y=1)


# Battery icon
Battery_icon = tk.PhotoImage(file="Assets/Images/Battery.png")

Battery_Status_icon = Button(
    Taskbar_Icons,
    width=20,
    height=40,
    borderwidth="0",
    relief="flat",
    bg="#080D11",
    image=Battery_icon,
)
Battery_Status_icon.place(x=24, y=-6)


# Internet connection icon
Internet_Warning_icon = tk.PhotoImage(
    file="Assets/Images/Internet_Warning.png"
)  # Warning status

Internet_Connected_icon = tk.PhotoImage(
    file="Assets/Images/Internet_Connected.png"
)  # Connected status

Internet_Status_icon = Button(
    Taskbar_Icons,
    width=20,
    height=40,
    borderwidth="0",
    relief="flat",
    bg="#080D11",
    image=Internet_Connected_icon,
)
Internet_Status_icon.place(x=48, y=-6)


# Sound volume icon
Volume_icon = tk.PhotoImage(file="Assets/Images/Volume.png")

Volume_Status_icon = Button(
    Taskbar_Icons,
    width=20,
    height=40,
    borderwidth="0",
    relief="flat",
    bg="#080D11",
    image=Volume_icon,
)
Volume_Status_icon.place(x=72, y=-6)




# ============================================== Clockbar =====================================================

Clockbar = Label(
    Taskbar,
    width=70,
    height=28,
    borderwidth="0",
    relief="raised",
    bg="#080D11",
)
Clockbar.place(x=940, y=1)


def times():

    current_time = time.strftime("%H: %M")
    clock.config(bg="#080D11", text=current_time, fg="white", font=("Segou UI", 9))
    clock.after(1, times)


clock = Label(Taskbar, borderwidth="0", relief="raised")
clock.after(1, times)
clock.place(x=928, y=6)


# ============================================== Start buttons =====================================================

icon_bg = "#212121"

# load icons images
Settings_Icon = tk.PhotoImage(file="Assets/Images/Settings_Icon.png")
Settings_Icon_2 = tk.PhotoImage(file="Assets/Images/Settings_Icon_2.png")

Print_Dialog_Icon = tk.PhotoImage(file="Assets/Images/Print_Dialog_Icon.png")
Tasks_Icon = tk.PhotoImage(file="Assets/Images/Tasks_Icon.png")

File_Manager_Icon = tk.PhotoImage(file="Assets/Images/File_Manager_Icon.png")
Screen_Icon = tk.PhotoImage(file="Assets/Images/Screen_Icon.png")

# Buttons (left side) =============================================================================================


# Settings button
Settings_Button = Button(
    StartMenu,
    width=229,
    height=16,
    borderwidth="0",
    bg=icon_bg,
    relief="raised",
    image=Settings_Icon,
    command= Settings_error
)
Settings_Button.place(x=65, y=224)

# Blue Settings button
Settings_Button_2 = Button(
    StartMenu,
    width=22,
    height=23,
    borderwidth="0",
    bg=icon_bg,
    relief="raised",
    image=Settings_Icon_2,
    command= Settings_error
)
Settings_Button_2.place(x=275, y=7)

# Print button
Print_Button = Button(
    StartMenu,
    width=229,
    height=16,
    borderwidth="0",
    bg=icon_bg,
    relief="raised",
    image=Print_Dialog_Icon,
    command= Print_error
)
Print_Button.place(x=65, y=204)

# Buttons (right side) ============================================================================================

# ThisPC Button
This_PC_Button = Button(
    StartMenu,
    width=32,
    height=18,
    borderwidth="0",
    bg=icon_bg,
    relief="raised",
    image=Screen_Icon,
    command= This_PC_error
)
This_PC_Button.place(x=5, y=48)

# File Manager Button
File_Manager_Button = Button(
    StartMenu,
    width=32,
    height=18,
    borderwidth="0",
    bg=icon_bg,
    relief="raised",
    image=File_Manager_Icon,
    command= FileManager_error
)
File_Manager_Button.place(x=5, y=83)


# Create a right click menu ==========================================================================================


def View_Event():
    print("View option activated!")
    try:
        Contextual_Menu.place_forget()
    except:
        pass


def RightClickEvent():
    print("function1 activated")
    try:
        Contextual_Menu.place_forget()
    except:
        pass


# Load images
ContextualMenu = tk.PhotoImage(file="Assets/ContextualMenu.png")

# Buttons
ViewButton = tk.PhotoImage(file="Assets/Buttons/CM_View_button.png")

Contextual_Menu = Label(
    Background,
    width=184,
    height=233,
    image=ContextualMenu,
    borderwidth="0",
    background=Contextual_Menu_BG_Color,
)


def open_popup(event):
    try:
        Contextual_Menu.place(x=event.x, y=event.y)
        Background.after(1)
        Contextual_Menu.focus_set()
    except:
        pass


def close_popup(event):
    try:
        Contextual_Menu.place_forget()
        Background.after(1)
        Background.unbind_all("<Button-1>")
    except:
        pass


def enable_depopup(event):
    Background.bind_all("<Button-1>", close_popup)


def disable_depopup(event):
    Background.unbind_all("<Button-1>")


View_Contextual_Button = Button(
    Contextual_Menu,
    width=182,
    height=21,
    borderwidth="0",
    image=ViewButton,
    command=View_Event,
)
View_Contextual_Button.place(x=0, y=0)


Background.bind("<Button-3>", open_popup)
Background.bind("<Motion>", enable_depopup)
Contextual_Menu.bind("<Motion>", disable_depopup)
# ======================================================================================================================

# Desktop icons


# all widgets in the window are updated forever every 1 milliseconds without it freezing the window or widgets.
# This is done by the after method.



# this fixes the bug (Taskbar buttons or labels disappear or blink when a widget is dragged onto them).
# This is done by the bind method.




Ventana.mainloop()
