from tkinter import Button, Entry, Label, PhotoImage, Tk
import time

from System.GUI.FileManager import Display_FileManager
from System.GUI.MessageBox import Display_MessageBox
from System.GUI.Terminal import Display_Terminal
from System.Utils.Utils import print_log

__author__ = 'TheBigEye'
__version__ = '2.0'


def Desktop(master):

 # Documentacion ---------------------------------------------------------------------------------------------------------------

    """
    Esto crea el escritorio usando widgets.

    Parametros:
    master: es el objeto principal de la ventana.

    Retorna:
    None
    """

 # ---------------------------------------------------------------[ Escritorio ]-------------------------------------------------------------------

    print_log("Desktop: Escritorio cargado y ejecutandose")    

    global Wallpaper, Desktop_wallpaper

    master.configure(background = "#000000")  # Establece el fondo a color azul

    Wallpaper = PhotoImage(file = "Assets/Wallpapers/BlissHill.png")
    Desktop_wallpaper = Label(master, image= Wallpaper, borderwidth="0.1")
    Desktop_wallpaper.place(x=0, y=0) # Posiciona el fondo de escritorio en el centro

 # -------------------------------------------------------------[ Tipos de errores ]----------------------------------------------------------------

    global Settings_error, Print_error, This_PC_error, FileManager_error

    # Lista de los cuadros de dialogo que se usan, Error, advertencia, peligro, e info
    def Settings_error():
        Close_start_menu()
        Display_MessageBox(master, "Error", "Settings not found", draggable=False)
    
    def Print_error():
        Close_start_menu()
        Display_MessageBox(master, "Info", "Printing not found", draggable=False)

    def This_PC_error():
        Close_start_menu()
        Display_MessageBox(master, "Warning", "This PC not found", draggable=False)

    def FileManager_error():
        Close_start_menu()
        Display_MessageBox(master, "Error", "File Manager not found", draggable=False)
    

 # ----------------------------------------------------------------[ Programas ]--------------------------------------------------------------------

    global File_manager, Terminal

    # LLama al metodo del Explorador de archivos en forma de aplicacion
    def File_manager():

        import threading # Crea un hilo por cada vez que abre, para evitar sobreposiciones
        Close_start_menu() 
        Display_FileManager(master, "This PC", draggable=True)

    # LLama a la terminal 
    def Terminal():
        Close_start_menu()
        Display_Terminal(master, draggable=True)

 # ------------------------------------------------------------[ Barra de tareas ]------------------------------------------------------------------

    global Taskbar_GUI_Image, Taskbar

    Taskbar_GUI_Image = PhotoImage(file = "Assets/GUI/Taskbar.png") 

    # Barra de tareas
    Taskbar = Label(
        master,
        width = 1024,
        height = 29,
        borderwidth = "0",
        image = Taskbar_GUI_Image,
        background = "black",
        foreground = "gray",
        relief = "raised",
    )

    Taskbar.place(x= 0, y= 571)


 # -------------------------------------------------------------[ Barra del reloj ]-----------------------------------------------------------------

    global Clockbar, times, clock

    Clockbar = Label(
        Taskbar,
        width=70,
        height=28,
        borderwidth="0",
        relief="raised",
        bg="#080D11",
    )

    Clockbar.place(x=950, y=1)

    # El reloj
    def times():

        current_time = time.strftime("%H: %M")
        clock.config(bg="#080D11", text=current_time, fg="white", font=("Segou UI", 9))
        clock.after(1, times)

    clock = Label(Taskbar, borderwidth="0", relief="raised")
    clock.after(1, times)
    clock.place(x=965, y=6)  


 # ------------------------------------------------------------[ Menu de inicio ]-------------------------------------------------------------------

    # Widget base del menu de inicio
    global Start_menu_GUI, Start_menu
    Start_menu_GUI = PhotoImage(file = "Assets/GUI/StartMenu.png")

    Start_menu = Label(
        master,
        width = 314,
        height = 440,
        image = Start_menu_GUI,
        borderwidth = "0"
    )

    global Start_menu_button, Open_start_menu, Close_start_menu, Open_start_button, Close_start_button
    Start_menu_button = PhotoImage(file = "Assets/Buttons/Start_Button.png")

    # Abre
    def Open_start_menu():
        Start_menu.place(x=1, y=126)
        time.sleep(0.1)

        Open_start_button.place_forget()
        Close_start_button.place(x=0, y=571)

    # Cierra
    def Close_start_menu():
        Start_menu.place_forget()
        time.sleep(0.1)

        Open_start_button.place(x=0, y=571)
        Close_start_button.place_forget()

    # Los botones se van reemplazando uno al otro para usar diferentes funciones a la vez
    Open_start_button = Button(
        master,
        width=48,
        height=28,
        borderwidth="0",
        bg = "#000000",
        relief="raised",
        command=Open_start_menu,
        image= Start_menu_button
    )
    Open_start_button.place(x=0, y=571)

    Close_start_button = Button(
        master,
        width=48,
        height=28,
        borderwidth="0",
        bg = "#000000",
        relief="raised",
        command=Close_start_menu,
        image= Start_menu_button
    )
    Close_start_button.place_forget()

 # ----------------------------------------------------[ Botones de la barra de tareas ]------------------------------------------------------------


    # Icono de la aplciacion de terminal en la barra de tareas
    global Terminal_taskbar_icon, Terminal_taskbar_button
    Terminal_taskbar_icon = PhotoImage(file = "Assets/Buttons/TerminalTaskIcon.png")

    Terminal_taskbar_button = Button(
        Taskbar,
        width=43,
        height=25,
        borderwidth="0",
        relief="raised",
        bg="#080D11",
        command=Terminal,
        image = Terminal_taskbar_icon
    )
    Terminal_taskbar_button.place(x=40, y=2)

    # Icono del explorador de archivos en la barra de tareas
    global File_manager_taskbar_icon, File_manager_taskbar_button
    File_manager_taskbar_icon = PhotoImage(file = "Assets/Buttons/FileManagerTaskIcon.png")

    File_manager_taskbar_button = Button(
        Taskbar,
        width=43,
        height=25,
        borderwidth="0",
        relief="raised",
        bg="#080D11",
        command=File_manager,
        image = File_manager_taskbar_icon
    )
    File_manager_taskbar_button.place(x=80, y=2)

    # Icono del navegador en la barra de tareas
    global Browser_taskbar_icon, Browser_taskbar_button
    Browser_taskbar_icon = PhotoImage(file = "Assets/Buttons/BrowserTaskIcon.png")

    Browser_taskbar_button = Button(
        Taskbar,
        width=43,
        height=25,
        borderwidth="0",
        relief="raised",
        bg="#080D11",
        command = File_manager,
        image = Browser_taskbar_icon
    )
    Browser_taskbar_button.place(x=120, y=2)


    # Widget base para los iconos de la barra del reloj
    global Clokcbar_taskbar_icons, Clockbar_icons
    Clockbar_taskbar_icons = PhotoImage(file="Assets/Taskbar_Icons.png")

    Clockbar_icons = Label(
        Taskbar,
        width=100,
        height=28,
        borderwidth="0",
        relief="raised",
        bg="#080D11",
        image = Clockbar_taskbar_icons
    )
    Clockbar_icons.place(x=864, y=1)


    # Icono del estado de la bateria
    global Battery_taskbar_icon, Batery_status_icon
    Battery_taskbar_icon = PhotoImage(file="Assets/Images/Battery.png")

    Battery_status_icon = Button(
        Clockbar_icons,
        width=20,
        height=40,
        borderwidth="0",
        relief="flat",
        bg="#080D11",
        image=Battery_taskbar_icon,
    )
    Battery_status_icon.place(x=24, y=-6)


    # Icono del estado del internet
    global Internet_Warning_icon, Internet_Connected_icon, Internet_status_icon

    # Estado desconectado
    Internet_Warning_icon = PhotoImage(file="Assets/Images/Internet_Warning.png")

    # Estado conectado
    Internet_Connected_icon = PhotoImage(file="Assets/Images/Internet_Connected.png")

    Internet_status_icon = Button(
        Clockbar_icons,
        width=20,
        height=40,
        borderwidth="0",
        relief="flat",
        bg="#080D11",
        image=Internet_Connected_icon,
    )
    Internet_status_icon.place(x=48, y=-6)


    # Icono de volumen del sonido
    global Volume_icon, Volume_status_icon
    Volume_icon = PhotoImage(file="Assets/Images/Volume.png")

    Volume_status_icon = Button(
        Clockbar_icons,
        width=20,
        height=40,
        borderwidth="0",
        relief="flat",
        bg="#080D11",
        image=Volume_icon,
    )
    Volume_status_icon.place(x=72, y=-6)


 # ----------------------------------------------------------------- [ Iconos del menu de inicio ] --------------------------------------------------

    # Icono de configuracion del menu de inicio
    global Settings_Start_icon, Settings_Start_icon_2
    Settings_Start_icon = PhotoImage(file="Assets/Images/Settings_Icon.png")
    Settings_Start_icon_2 = PhotoImage(file="Assets/Images/Settings_Icon_2.png")



    

    

