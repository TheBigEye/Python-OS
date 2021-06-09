# ---------------------------- Liscence - Read pls -------------------------------- #
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

#=====================================================================================================================

from tkinter import *
import tkinter as tk
import time

Ventana = tk.Tk()
Ventana.title("PythonOS")
Ventana.geometry("1024x600")
Ventana.resizable(0, 0)
Ventana.configure(background="#000000")

# Variables
Wallpaper = "BlissHill"

Contextual_Menu_BG_Color = "#ffffff"
Start_Menu_image_BG_Color = "#ffffff"
FileManager_BG_Color = "#ffffff"

# Imagen de fondo
Background_image = tk.PhotoImage(file="Assets/pythontheme/Wallpapers/" + Wallpaper + ".png")

Background = tk.Label(Ventana, image=Background_image)
Background.place(x=-1, y=-1, relwidth=1, relheight=1)

Default_Taskbar_y = 571


# Drag and drop function
def make_draggable(widget):
    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)


def on_drag_start(event):
    widget = event.widget
    widget.update_idletasks()
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y


def on_drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.update_idletasks()
    widget.place(x= x, y= y)


# Resource address table ==============================================================================================

# ------------------------------------------------------------------------------------ #
#     Here the addresses of all the images, sounds and resources used are specified    #
#     To make it more comfortable, I will put a numbering so that it is by order       #
#                                                                                      #
#     so organized I am XD...                                                          #
# ------------------------------------------------------------------------------------ #

# GUI
Taskbar_image = tk.PhotoImage(file="Assets/pythontheme/GUI/Taskbar.png") # ------------------------------------------------ Taskbar
Clockbar_image = tk.PhotoImage(file="Assets/pythontheme/GUI/Clockbar.png") # ----------------------------------------------Clockbar
StartMenu_image = tk.PhotoImage(file="Assets/pythontheme/GUI/StartMenu.png") # ----------------------------------------- Start Menu
FileManager_image = tk.PhotoImage(file="Assets/pythontheme/GUI/FileManager.png") # ----------------------------------- File Manager
ErrorMessagebox_image = tk.PhotoImage(file="Assets/pythontheme/GUI/Error_MessageBox.png") # ---------------------- Error Messagebox

# Taskbar Buttons
Start_Button_image = tk.PhotoImage(file="Assets/pythontheme/Buttons/Start_Button.png") # ------------------------------- Start Menu
FileManager_tb_Button_image = tk.PhotoImage(file="Assets/pythontheme/GUI/FileManager.png") # ------------------------- File Manager

# Clockbar Buttons

# Start menu buttons

# Window buttons
Close_wd_button_image = tk.PhotoImage(file="Assets/pythontheme/Buttons/Close_white.png") # 1

# =================================================== Taskbar ========================================================

# Taskbar posicion
Taskbar = Label(

    Ventana,
    width = 974,
    height = 29,
    borderwidth = "0",
    image = Taskbar_image,
    background = "black",
    foreground = "gray",
    relief = "raised",

)
Taskbar.place(x=50, y=Default_Taskbar_y)

# ================================================= Start menu =======================================================

# Start menu GUI
StartMenu = Label(
    Ventana, width=314, height=440, image=StartMenu_image, borderwidth="0"
)

# Open
def Open_StartMenu():
    StartMenu.place(x=1, y=126)
    time.sleep(0.1)

    Start_A.place(x=0, y=600)
    Start_B.place(x=0, y=571)


# Close
def Close_StartMenu():

    StartMenu.place(x=1, y=1000)
    time.sleep(0.1)

    Start_A.place(x=0, y=571)
    Start_B.place(x=0, y=600)


# Crea y posiciona el boton de Inicio en la Barra de tareas

# Boton original
Start_A = Button(
    Ventana,
    width=48,
    height=28,
    borderwidth="0",
    bg="black",
    relief="raised",
    image=Start_Button_image,
    command=Open_StartMenu,
)
Start_A.place(x=0, y=571)

# Segundo boton
Start_B = Button(
    Ventana,
    width=48,
    height=28,
    borderwidth="0",
    bg="black",
    relief="raised",
    image=Start_Button_image,
    command=Close_StartMenu,
)
Start_B.place(x=0, y=600)

# =================================================== Programs ========================================================

# File Manager
FileManagerMenu = Label(
    Background,
    width=687,
    height=374,
    bg="black",
    image=FileManager_image,
    borderwidth="0",
)

FileManagerMenu.place(x=1512, y=1512)
make_draggable(FileManagerMenu)


def Open_FileManager():

    # Menu.place(x=1, y=1000)
    Close_StartMenu()

    Ventana.title("PythonOS - File Manager")

    time.sleep(0.2)
    FileManagerMenu.place(x=250, y=150)


def Close_FileManager():
    time.sleep(0.4)

    Ventana.title("PythonOS")

    FileManagerMenu.place(x=1512, y=1512)


Close_FileManager_Button = Button(
    FileManagerMenu,
    width=10,
    height=10,
    bg="black",
    image=Close_wd_button_image,
    borderwidth="0",
    command=Close_FileManager,
)

Close_FileManager_Button.place(x=666, y=7)

# ============================================== Error MessageBox ====================================================

# Error MessgaeBox
Error_MessageBox = Label(
    Background,
    width=382,
    height=106,
    bg="white",
    image=ErrorMessagebox_image,
    borderwidth="0",
)

Error_MessageBox.place(x=1512, y=1512)


def Open_error():

    StartMenu.place(x=1, y=1000)
    time.sleep(0.1)
    Close_StartMenu

    time.sleep(1)
    Error_MessageBox.place(x=320, y=240)


def Close_error():
    time.sleep(0.3)
    Error_MessageBox.place(x=1512, y=1512)


OK_ErrorMessageBox_image = tk.PhotoImage(file="Assets/pythontheme/Buttons/OK_Button.png")
OK_ErrorMessageBox = Button(
    Error_MessageBox,
    width=30,
    height=22,
    bg="white",
    image=OK_ErrorMessageBox_image,
    borderwidth="0",
    command=Close_error,
)

OK_ErrorMessageBox.place(x=343, y=78)

Close_ErrorMessageBox_image = tk.PhotoImage(file="Assets/pythontheme/Buttons/Close_red.png")
Close_ErrorMessageBox = Button(
    Error_MessageBox,
    width=7,
    height=7,
    bg="red",
    image=Close_ErrorMessageBox_image,
    borderwidth="0",
    command=Close_error,
)

Close_ErrorMessageBox.place(x=359, y=11)

# ============================================== Iconos de la barra ===================================================

# Icono del explorador de archivos
FileManager_icon_image = tk.PhotoImage(file="Assets/FileManagerTaskIcon.png")

FileManager_task_icon = Button(
    Taskbar,
    width=43,
    height=25,
    borderwidth="0",
    relief="raised",
    bg="#080D11",
    image=FileManager_icon_image,
    command=Open_FileManager,
)
FileManager_task_icon.place(x=0, y=2)


# Base de los iconos de la barra de tarea
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


# Icono de la bateria
Battery_icon = tk.PhotoImage(file="Assets/pythontheme/Images/Battery.png")

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


# Icono del internet
Internet_Warning_icon = tk.PhotoImage(
    file="Assets/pythontheme/Images/Internet_Warning.png"
)  # Warning status

Internet_Connected_icon = tk.PhotoImage(
    file="Assets/pythontheme/Images/Internet_Connected.png"
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


# Icono del volumen de sonido
Volume_icon = tk.PhotoImage(file="Assets/pythontheme/Images/Volume.png")

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


# ============================================== Barra del reloj =====================================================

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
clock.place(x=928, y=5)


# ============================================== Botones de inicio =====================================================

icon_bg = "#212121"

# load icons images
Settings_Icon = tk.PhotoImage(file="Assets/pythontheme/Images/Settings_Icon.png")
Settings_Icon_2 = tk.PhotoImage(file="Assets/pythontheme/Images/Settings_Icon_2.png")

Print_Dialog_Icon = tk.PhotoImage(file="Assets/pythontheme/Images/Print_Dialog_Icon.png")
Tasks_Icon = tk.PhotoImage(file="Assets/pythontheme/Images/Tasks_Icon.png")

File_Manager_Icon = tk.PhotoImage(file="Assets/pythontheme/Images/File_Manager_Icon.png")
Screen_Icon = tk.PhotoImage(file="Assets/pythontheme/Images/Screen_Icon.png")

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
    command=Open_error,
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
    command=Open_error,
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
    command=Open_error,
)
Print_Button.place(x=65, y=204)

# Task manager button
# Tasks_Button = Button(
# Menu,
# width=22,
# height=23,
# borderwidth='0',
# bg=icon_bg,
# relief='raised',
# image=Tasks_Icon,
# command=Open_error,
# )
# Tasks_Button.place(x=275, y=41)

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
    command=Open_error,
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
    command=Open_FileManager,
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
ViewButton = tk.PhotoImage(file="Assets/pythontheme/Buttons/CM_View_button.png")

Contextual_Menu = Label(
    Ventana,
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


View_Button = Button(
    Contextual_Menu,
    width=182,
    height=21,
    borderwidth="0",
    image=ViewButton,
    command=View_Event,
)
View_Button.place(x=0, y=0)


Background.bind("<Button-3>", open_popup)
Background.bind("<Motion>", enable_depopup)
Contextual_Menu.bind("<Motion>", disable_depopup)
# ======================================================================================================================

# Desktop icons

Ventana.mainloop()
