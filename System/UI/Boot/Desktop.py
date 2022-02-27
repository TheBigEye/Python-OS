import time
from tkinter import Button, Label

from System.Core.KeysSystem import add_key, get_value
from System.Programs.Terminal.Terminal import Terminal
from System.Programs.Welcome.Welcome import Welcome_window
from System.UI.Browser import Display_Browser
from System.UI.FileManager import Display_FileManager
from System.UI.MessageBox import MessageBox
from System.Utils.Utils import Asset, Asset_colored, Execute, internet_on, print_log

__author__ = 'TheBigEye'
__version__ = '2.0'


def Desktop(master):

 # Documentation ---------------------------------------------------------------------------------------------------------------

    """
    This creates the desktop using widgets.

    Parametros:
    master: is the main object of the window.

    Returns:
    None
    """

 # ---------------------------------------------------------------[ Desktop ]-----------------------------------------------------------------------

    print_log("Desktop loaded and running")

    global Wallpaper, Desktop_wallpaper

    master.configure(background = "#000000")

    real_time_wallpaper = get_value("PYTHON-OS", "System", "Desktop", "Real-time-wallpaper")

    if real_time_wallpaper == "True":
        if time.localtime().tm_hour >= 18 or time.localtime().tm_hour < 6:
            Wallpaper = Asset("Night_dusk.png")
        else:
            Wallpaper = Asset("Day_dusk.png")
    else:
        Wallpaper = Asset("BlissHill.png")

    Desktop_wallpaper = Label(master, image= Wallpaper, borderwidth=0)
    Desktop_wallpaper.place(x=0, y=0) # Posiciona el fondo de escritorio en el centro


 # ---------------------------------------------------------------[Welcome window]------------------------------------------------------------------

    Welcome_window(master, draggable=False)


 # -------------------------------------------------------------[ Tipos de errores ]----------------------------------------------------------------

    global Settings_error, Print_error, This_PC_error, FileManager_error

    # Lista de los cuadros de dialogo que se usan, Error, advertencia, peligro, e info
    def Settings_error():
        Close_start_menu()
        MessageBox(master, "Error", "Settsvc.py" ,"Settings not found", False)

    def Print_error():
        Close_start_menu()
        MessageBox(master, "Info", "Info", "Printing not found", False)

    def This_PC_error():
        Close_start_menu()
        MessageBox(master, "Warning", "This PC", "This PC not found", True)

    def FileManager_error():
        Close_start_menu()
        MessageBox(master, "Error", "Explorer.py", "File Manager not found", False)


 # ----------------------------------------------------------------[ Programas ]--------------------------------------------------------------------

    global File_manager, Terminal, Registry, Browser

    # LLama al metodo del Explorador de archivos en forma de aplicacion
    def File_manager():
        Close_start_menu()

        Display_FileManager(master, "This PC", draggable=True)


    # LLama a la terminal
    def Terminal_programm():
        Close_start_menu()

        Execute(master, 1000, Terminal, master, True)

    # LLama al navegador
    def Browser():
        Close_start_menu()

        Display_Browser(master, draggable=True)

 # ------------------------------------------------------------[ Barra de tareas ]------------------------------------------------------------------

    global Taskbar_UI_Image, Taskbar

    Taskbar_UI_Image = Asset("Taskbar.png")

    # Barra de tareas
    Taskbar = Label(
        master,
        width = 1024,
        height = 29,
        borderwidth = "0",
        image = Taskbar_UI_Image,
        background = "black",
        foreground = "gray",
        relief = "raised",
    )

    Taskbar.place(x= 109, y= 571)



    global Startbar_UI_Image, Startbar
    Startbar_UI_Image = Asset("Startbar.png")

    # Barra de inicio
    Startbar = Label(
        master,
        width = 109,
        height = 29,
        borderwidth = "0",
        image = Startbar_UI_Image,
        background = "white",
        foreground = "gray",
        relief = "raised",
    )

    Startbar.place(x= 0, y= 571)


 # ------------------------------------------------------------[ Menu de inicio ]-------------------------------------------------------------------

    # Widget base del menu de inicio
    global Start_menu_UI, Start_menu
    Start_menu_UI = Asset("StartMenu.png")

    Start_menu = Label(
        master,
        width = 314,
        height = 440,
        image = Start_menu_UI,
        borderwidth = "0"
    )

    global Start_menu_button, Start_menu_active_button, Open_start_menu, Close_start_menu, Open_start_button, Close_start_button
    Start_menu_button = Asset("Start_Button.png")
    Start_menu_active_button = Asset_colored("Start_Button_active.png", 1)

    # Abre
    def Open_start_menu():
        Start_menu.place(x=1, y=126)
        Start_menu.lift()
        time.sleep(0.1)

        Open_start_button.place_forget()
        Close_start_button.place(x=4, y=2)

    # Cierra
    def Close_start_menu():
        Start_menu.place_forget()
        time.sleep(0.1)

        Open_start_button.place(x=4, y=2)
        Close_start_button.place_forget()

    # Los botones se van reemplazando uno al otro para usar diferentes funciones a la vez
    Open_start_button = Button(
        Startbar,
        width=28,
        height=25,
        borderwidth="0",
        bg = "#070E11",
        relief="raised",
        command=Open_start_menu,
        image= Start_menu_button
    )
    Open_start_button.place(x=4, y=2)

    Close_start_button = Button(
        Startbar,
        width=28,
        height=25,
        borderwidth="0",
        bg = "#070E11",
        relief="raised",
        command=Close_start_menu,
        image= Start_menu_button
    )
    Close_start_button.place_forget()

    Open_start_button.bind("<Enter>", lambda event: Open_start_button.config(image = Start_menu_active_button))
    Open_start_button.bind("<Leave>", lambda event: Open_start_button.config(image = Start_menu_button))

    Close_start_button.bind("<Enter>", lambda event: Close_start_button.config(image = Start_menu_active_button))
    Close_start_button.bind("<Leave>", lambda event: Close_start_button.config(image = Start_menu_button))

 # ----------------------------------------------------[ Botones de la barra de inicio ]------------------------------------------------------------


    # Icono de modulos
    global Modules_startbar_icon, Modules_startbar_active_icon, Modules_startbar_button
    Modules_startbar_icon = Asset("Modules_button.png")
    Modules_startbar_active_icon = Asset_colored("Modules_button_active.png", 1)

    Modules_startbar_button = Button(
        Startbar,
        width=28,
        height=25,
        borderwidth="0",
        relief="raised",
        bg = "#070E11",
        image= Modules_startbar_icon
    )
    Modules_startbar_button.place(x=35, y=2)

    Modules_startbar_button.bind("<Enter>", lambda event: Modules_startbar_button.config(image = Modules_startbar_active_icon))
    Modules_startbar_button.bind("<Leave>", lambda event: Modules_startbar_button.config(image = Modules_startbar_icon))


    # icono de busqueda
    global Search_startbar_icon, Search_startbar_active_icon, Search_startbar_button
    Search_startbar_icon = Asset("Search_button.png")
    Search_startbar_active_icon = Asset_colored("Search_button_active.png", 1)

    Search_startbar_button = Button(
        Startbar,
        width=28,
        height=25,
        borderwidth="0",
        relief="raised",
        bg = "#070E11",
        image= Search_startbar_icon,
        command=Terminal_programm
    )
    Search_startbar_button.place(x=66, y=2)

    Search_startbar_button.bind("<Enter>", lambda event: Search_startbar_button.config(image = Search_startbar_active_icon))
    Search_startbar_button.bind("<Leave>", lambda event: Search_startbar_button.config(image = Search_startbar_icon))

 # ----------------------------------------------------[ Botones de la barra de tareas ]------------------------------------------------------------



    # Icono de la aplicacion de terminal en la barra de tareas
    global Terminal_taskbar_icon, Terminal_taskbar_active_icon, Terminal_taskbar_button
    Terminal_taskbar_icon = Asset("Terminal_taskbar_icon.png")
    Terminal_taskbar_active_icon = Asset("Terminal_taskbar_active_icon.png")

    Terminal_taskbar_button = Button(
        Taskbar,
        width=28,
        height=25,
        borderwidth="0",
        relief="raised",
        bg="#070E11",
        command=Terminal_programm,
        image = Terminal_taskbar_icon
    )
    #Terminal_taskbar_button.place(x=8, y=2) #48

    Terminal_taskbar_button.bind("<Enter>", lambda event: Terminal_taskbar_button.config(image = Terminal_taskbar_active_icon))
    Terminal_taskbar_button.bind("<Leave>", lambda event: Terminal_taskbar_button.config(image = Terminal_taskbar_icon))


    # Icono del explorador de archivos en la barra de tareas
    global File_manager_taskbar_icon, File_manager_taskbar_active_icon, File_manager_taskbar_button
    File_manager_taskbar_icon = Asset("FileManager_taskbar_icon.png")
    File_manager_taskbar_active_icon = Asset("FileManager_taskbar_active_icon.png")

    File_manager_taskbar_button = Button(
        Taskbar,
        width=28,
        height=25,
        borderwidth="0",
        relief="flat",
        bg="#070E11",
        command=File_manager,
        image = File_manager_taskbar_icon
    )
    #File_manager_taskbar_button.place(x=42, y=2)#82

    File_manager_taskbar_button.bind("<Enter>", lambda event: File_manager_taskbar_button.config(image = File_manager_taskbar_active_icon))
    File_manager_taskbar_button.bind("<Leave>", lambda event: File_manager_taskbar_button.config(image = File_manager_taskbar_icon))


    # Icono del navegador en la barra de tareas
    global Browser_taskbar_icon, Browser_taskbar_active_icon, Browser_taskbar_button
    Browser_taskbar_icon = Asset("Browser_taskbar_icon.png")
    Browser_taskbar_active_icon = Asset("Browser_taskbar_active_icon.png")

    Browser_taskbar_button = Button(
        Taskbar,
        width=28,
        height=25,
        borderwidth="0",
        relief="raised",
        bg="#070E11",
        command = Browser,
        image = Browser_taskbar_icon
    )
    #Browser_taskbar_button.place(x=76, y=2) 116

    Browser_taskbar_button.bind("<Enter>", lambda event: Browser_taskbar_button.config(image = Browser_taskbar_active_icon))
    Browser_taskbar_button.bind("<Leave>", lambda event: Browser_taskbar_button.config(image = Browser_taskbar_icon))

    # se crea una lista de los botones de la barra de tarea
    global taskbar_buttons
    taskbar_buttons = [Terminal_taskbar_button, File_manager_taskbar_button, Browser_taskbar_button]

    # los botones se posicionan en la barra de tareas en el orden de la lista
    for i in range(len(taskbar_buttons)):
        taskbar_buttons[i].place(x=8 + (i * 32), y=2)


 # ---------------------------------------------------------[ Widgets de la barra de reloj ]--------------------------------------------------------


    # Widget base para los iconos de la barra del reloj
    global Clokcbar_taskbar_icons, Clockbar_icons
    Clockbar_taskbar_icons = Asset("Taskbar_Icons.png")

    Clockbar_icons = Label(
        Taskbar,
        width=164,
        height=28,
        borderwidth="0",
        relief="raised",
        bg="#070E11",
        image = Clockbar_taskbar_icons
    )
    Clockbar_icons.place(x=755, y=1)


    # -------------------------------------------------------------[ Barra del reloj ]-----------------------------------------------------------

    global Clock, clock

    def clock():
        global Time
        Time = time.strftime("%H:%M")
        Clock.config(text=Time)
        Clock.after(200, clock)


    Clock = Label(
        Clockbar_icons,
        width = 8,
        height = 2,
        borderwidth = "0",
        background = "#070E11",
        foreground = "white",
        relief = "raised",
        font=("Segoe UI Semibold", 9),
        text = "",
    )

    Clock.place(x= 96, y= -1)

    clock()

    # Icono del estado de la bateria
    global Battery_taskbar_icon, Battery_status_icon
    Battery_taskbar_icon = Asset("Battery.png")

    Battery_status_icon = Button(
        Clockbar_icons,
        width=20,
        height=40,
        borderwidth="0",
        relief="flat",
        bg="#070E11",
        image=Battery_taskbar_icon,
        command = Settings_error
    )
    Battery_status_icon.place(x=24, y=-6)


    # Icono del estado del internet
    global Internet_icon, Internet_status_icon

    # Comprueba si hay conexion a internet
    if internet_on() == True:
        # Estado conectado
        Internet_icon = Asset("Internet_Connected.png")
    else:
        # Estado desconectado
        Internet_icon = Asset("Internet_Warning.png")

    Internet_status_icon = Button(
        Clockbar_icons,
        width=20,
        height=40,
        borderwidth="0",
        relief="flat",
        bg="#080D11",
        image=Internet_icon,
        command = Print_error
    )
    Internet_status_icon.place(x=48, y=-6)


    # Icono de volumen del sonido
    global Volume_icon, Volume_status_icon
    Volume_icon = Asset("Volume.png")

    Volume_status_icon = Button(
        Clockbar_icons,
        width=20,
        height=40,
        borderwidth="0",
        relief="flat",
        bg="#080D11",
        image=Volume_icon,
        command = This_PC_error
    )
    Volume_status_icon.place(x=72, y=-6)


 # ----------------------------------------------------------------- [ Iconos del menu de inicio ] --------------------------------------------------

    # Icono de configuracion del menu de inicio
    #global Settings_Start_icon, Settings_Start_icon_2
    #Settings_Start_icon = Asset("Assets/Images/Settings_Icon.png")
    #Settings_Start_icon_2 = Asset("Assets/Images/Settings_Icon_2.png")
