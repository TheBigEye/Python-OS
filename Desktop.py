from tkinter import *
import tkinter as tk
import time

ventana = tk.Tk()
ventana.title("Windows PY")
ventana.geometry('1024x720')  # Ancho x Alto
ventana.resizable(False, False)
ventana.configure(background="cornflower blue")

# Variables
Wallpaper_DIR = "Assets/Wallpapers"

# imagen de fondo
background_image = tk.PhotoImage(file=Wallpaper_DIR + "/Bliss_night.png")

background_label = tk.Label(ventana, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# ============================================== Barra de tareas =====================================================


def times():
    current_time = time.strftime("%H: %M")
    clock.config(bg="#080D11", text=current_time,
                 fg="white", font="arial 10 bold")
    clock.after(200, times)

# def Error_dev_dialog():


# Crea y posiciona la barra de tareas en la ventana
# Taskbar textura
TaskbarTexture = tk.PhotoImage(file='Assets/Taskbar.png')


# Taskbar posicion
toolbar = Label(ventana, width=148, height=29, borderwidth="0", image=TaskbarTexture,
                text="", background="black", foreground="gray", relief="raised")
toolbar.pack(fill=X, expand=True, anchor="s")

# =============================================== Menu de inicio =====================================================

# Gui del menu
StartMenu = tk.PhotoImage(file='Assets/Menu.png')
Menu = Label(ventana, width=315, height=441, image=StartMenu, borderwidth="0")


# Esta funcion abre y cierra la GUI del menu.. para hacerlo facil, cada vez que se clcikea el bootn, se cambian los mismos

# Abre el menu
def Click_1():
    Menu.place(x=1, y=245)
    time.sleep(0.1)
    start_1.place(x=0, y=50)
    start_2.place(x=0, y=0)


# Cerra el menu
def Click_2():
    Menu.place(x=1, y=1000)
    time.sleep(0.1)
    start_1.place(x=0, y=0)
    start_2.place(x=0, y=32)


# Crea y posiciona el boton de Inicio en la Barra de tareas
# Textura del boton de "INICIO"
StartTexture = tk.PhotoImage(file='Assets/Start_Button.png')
StartLightTexture = tk.PhotoImage(file='Assets/Start_Light_Button.png')


# Boton original
start_1 = Button(toolbar, width=48, height=28, borderwidth="0",
                 bg="black", relief="raised", image=StartTexture, command=Click_1)
start_1.place(x=0, y=0)

# Segundo boton
start_2 = Button(toolbar, width=48, height=28, borderwidth="0",
                 bg="black", relief="raised", image=StartTexture, command=Click_2)
start_2.place(x=0, y=32)

#=================================================== Programs ========================================================

#File Manager
FileManagerGui = tk.PhotoImage(file='Assets/FileManager.png')
FileManagerMenu = Label(ventana, width=687, height=374, bg="black", image=FileManagerGui, borderwidth="0")

FileManagerMenu.place(x=1512, y=1512)

def OpenFileManager():
    time.sleep(0.1)
    FileManagerMenu.place(x=250, y=150)
    Menu.place(x=1, y=1000)
    time.sleep(0.1)
    start_1.place(x=0, y=0)
    start_2.place(x=0, y=32)

def CloseFileManager():
    time.sleep(0.1)
    FileManagerMenu.place(x=1512, y=1512)
  
Close = tk.PhotoImage(file='Assets/Close.png')
Close_Button = Button(FileManagerMenu, width=10, height=10, bg="black", image=Close, borderwidth="0", command=CloseFileManager)

Close_Button.place(x=666, y=7)

# ============================================== Barra del reloj =====================================================

ClockTexture = tk.PhotoImage(file='Assets/Clockbar.png')

clockbar = Label(toolbar, width=70, height=28, borderwidth="0",
                 relief="raised", bg="#080D11")
clockbar.place(x=950, y=1)

current_time = time.strftime("%H: %M")
clock = Label(toolbar, borderwidth="0", relief="raised")
clock.config(bg="#080D11", text=current_time, fg="white", font="arial 10 bold")
clock.after(200, times)
clock.place(x=963, y=5)

# ============================================= Botones de inicio =====================================================

icon_bg = "#212121"

# load icons images
Settings_Icon = tk.PhotoImage(file='Assets/Images/Settings_Icon.png')
Settings_Icon_2 = tk.PhotoImage(file='Assets/Images/Settings_Icon_2.png')
Print_Dialog_Icon = tk.PhotoImage(file='Assets/Images/Print_Dialog_Icon.png')
Tasks_Icon = tk.PhotoImage(file='Assets/Images/Tasks_Icon.png')

File_Manager_Icon = tk.PhotoImage(file='Assets/Images/File_Manager_Icon.png')
Screen_Icon = tk.PhotoImage(file='Assets/Images/Screen_Icon.png')


# Buttons (left side)

# Settings button
Settings_Button = Button(Menu, width=229, height=16,
                         borderwidth="0", bg=icon_bg, relief="raised", image=Settings_Icon)
Settings_Button.place(x=65, y=224)

# Blue Settings button
Settings_Button_2 = Button(Menu, width=22, height=23,
                           borderwidth="0", bg=icon_bg, relief="raised", image=Settings_Icon_2)
Settings_Button_2.place(x=275, y=7)


# Print button
Print_Button = Button(Menu, width=229, height=16,
                      borderwidth="0", bg=icon_bg, relief="raised", image=Print_Dialog_Icon)
Print_Button.place(x=65, y=204)

# Task manager button
Tasks_Button = Button(Menu, width=22, height=23,
                      borderwidth="0", bg=icon_bg, relief="raised", image=Tasks_Icon)
Tasks_Button.place(x=275, y=41)


# Buttons (right side)
#Screen Button
Screen_Button = Button(Menu, width=32, height=18,
                      borderwidth="0", bg=icon_bg, relief="raised", image=Screen_Icon)
Screen_Button.place(x=5, y=48)


#File Manager Button
File_Manager_Button = Button(Menu, width=32, height=18,
                      borderwidth="0", bg=icon_bg, relief="raised", image=File_Manager_Icon, command=OpenFileManager)
File_Manager_Button.place(x=5, y=83)

ventana.mainloop()
