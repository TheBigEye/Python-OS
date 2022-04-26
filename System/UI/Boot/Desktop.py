import time
from tkinter import Button, Label

from System.Programs.Browser.Browser import Browser
from System.Programs.File_manager.File_manager import File_manager
from System.Programs.Terminal.Terminal import Terminal
from System.Programs.Welcome_dialog.Welcome import Welcome_dialog
from System.UI.Message_box import Message_box
from System.Utils.Logger import Logger
from System.Utils.Utils import Asset, Asset_color, Asset_colored, Execute, internet_on

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

    Logger.log("Desktop loaded and running")

    global Wallpaper, Desktop_wallpaper

    master.configure(background = "#000000")

    Wallpaper = Asset("Wallpapers", "Night_dusk.png")

    Desktop_wallpaper = Label(master, image= Wallpaper, borderwidth=0)
    Desktop_wallpaper.place(x=0, y=0) # set the position of the wallpaper to the center of the screen


 # ---------------------------------------------------------------[Welcome dialog]------------------------------------------------------------------

    Welcome_dialog(master, draggable=False)


 # -------------------------------------------------------------[ Errors types ]----------------------------------------------------------------

    global Settings_error, Print_error, This_PC_error, FileManager_error

    # Lista de los cuadros de dialogo que se usan, Error, advertencia, peligro, e info
    def Settings_error():
        Close_start_menu()
        Message_box(master, "Error", "Settsvc.py" ,"Settings not found", False)

    def Print_error():
        Close_start_menu()
        Message_box(master, "Info", "Info", "Printing not found", False)

    def This_PC_error():
        Close_start_menu()
        Message_box(master, "Warning", "This PC", "This PC not found", True)

    def FileManager_error():
        Close_start_menu()
        Message_box(master, "Error", "Explorer.py", "File Manager not found", False)


 # ----------------------------------------------------------------[ Programas ]--------------------------------------------------------------------

    global File_manager, Terminal, Browser

    # LLama al metodo del Explorador de archivos en forma de aplicacion
    def File_manager():
        Close_start_menu()

        File_manager(master, "This PC", draggable=True)


    # LLama a la terminal
    def Terminal_programm():
        Close_start_menu()

        Execute(master, 1000, Terminal, master, True)

    # LLama al navegador
    def Browser_programm():
        Close_start_menu()

        Browser(master)

 # ------------------------------------------------------------[ Barra de tareas ]------------------------------------------------------------------

    global Taskbar_image, Taskbar

    Taskbar_image = Asset("Taskbar", "Taskbar.png")

    # Barra de tareas
    Taskbar = Label(
        master,
        width = 1024,
        height = 29,
        borderwidth = "0",
        image = Taskbar_image,
        background = "black",
        foreground = "gray",
        relief = "raised",
    )

    Taskbar.place(x= 109, y= 571)

    global Startbar_image, Startbar
    Startbar_image = Asset("Taskbar", "Startbar.png")

    # Barra de inicio
    Startbar = Label(
        master,
        width = 109,
        height = 29,
        borderwidth = "0",
        image = Startbar_image,
        background = "white",
        foreground = "gray",
        relief = "raised",
    )

    Startbar.place(x= 0, y= 571)


 # ------------------------------------------------------------[ Menu de inicio ]-------------------------------------------------------------------

    # Widget base del menu de inicio
    global Start_menu_image, Start_menu
    Start_menu_image = Asset("Start menu", "Start_menu.png")

    Start_menu = Label(
        master,
        width = 314,
        height = 440,
        image = Start_menu_image,
        borderwidth = "0"
    )

    global Start_button, Start_button_light, Open_start_menu, Close_start_menu, Open_start_button, Close_start_button
    Start_button = Asset_color("Start menu", "Start_icon.png", "24x24", "#ff00ff", "#002C4F")
    Start_button_light = Asset_color("Start menu", "Start_icon.png", "24x24", "#ff00ff", "#00345B")

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
        borderwidth="0",
        bg = "#002C4F",
        activebackground = "#002C4F",
        relief="raised",
        command=Open_start_menu,
        image= Start_button
    )
    Open_start_button.place(x=4, y=2)

    Close_start_button = Button(
        Startbar,
        borderwidth="0",
        bg = "#002C4F",
        activebackground = "#002C4F",
        relief="raised",
        command=Close_start_menu,
        image= Start_button_light
    )
    Close_start_button.place_forget()

    Open_start_button.bind("<Enter>", lambda event: Open_start_button.config(image = Start_button_light))
    Open_start_button.bind("<Leave>", lambda event: Open_start_button.config(image = Start_button))

    Close_start_button.bind("<Enter>", lambda event: Close_start_button.config(image = Start_button_light))
    Close_start_button.bind("<Leave>", lambda event: Close_start_button.config(image = Start_button))

 # ----------------------------------------------------[ Botones de la barra de inicio ]------------------------------------------------------------


    # Icono de modulos
    global Modules_bbutton, Modules_button_light, Modules_startbar_button
    Modules_button = Asset_color("Taskbar", "Modules_icon.png", "24x24", "#ff00ff", "#002C4F")
    Modules_button_light = Asset_color("Taskbar", "Modules_icon.png", "24x24", "#ff00ff", "#00345B")

    Modules_startbar_button = Button(
        Startbar,
        borderwidth="0",
        relief="raised",
        bg = "#002C4F",
        activebackground = "#002C4F",
        image= Modules_button
    )
    Modules_startbar_button.place(x=35, y=2)

    Modules_startbar_button.bind("<Enter>", lambda event: Modules_startbar_button.config(image = Modules_button_light))
    Modules_startbar_button.bind("<Leave>", lambda event: Modules_startbar_button.config(image = Modules_button))


    # icono de busqueda
    global Search_button, Search_button_light, Search_startbar_button
    Search_button = Asset_color("Taskbar", "Search_icon.png", "24x24", "#ff00ff", "#002C4F")
    Search_button_light = Asset_color("Taskbar", "Search_icon.png", "24x24", "#ff00ff", "#00345B")

    Search_startbar_button = Button(
        Startbar,
        borderwidth="0",
        relief="raised",
        bg = "#002C4F",
        activebackground = "#002C4F",
        image= Search_button,
        command=Terminal_programm
    )
    Search_startbar_button.place(x=66, y=2)

    Search_startbar_button.bind("<Enter>", lambda event: Search_startbar_button.config(image = Search_button_light))
    Search_startbar_button.bind("<Leave>", lambda event: Search_startbar_button.config(image = Search_button))

 # ----------------------------------------------------[ Botones de la barra de tareas ]------------------------------------------------------------



    # Icono de la aplicacion de terminal en la barra de tareas
    global Terminal_button, Terminal_button_light, Terminal_taskbar_button
    Terminal_button= Asset_color("Terminal", "Terminal_icon.png", "24x24", "#ff00ff", "#00142D")
    Terminal_button_light = Asset_color("Terminal", "Terminal_icon.png", "24x24", "#ff00ff", "#001B3D")

    Terminal_taskbar_button = Button(
        Taskbar,
        borderwidth="0",
        relief="flat",
        bg="#00142D",
        activebackground = "#00142D",
        command=Terminal_programm,
        image = Terminal_button
    )

    Terminal_taskbar_button.bind("<Enter>", lambda event: Terminal_taskbar_button.config(image = Terminal_button_light))
    Terminal_taskbar_button.bind("<Leave>", lambda event: Terminal_taskbar_button.config(image = Terminal_button))


    # Icono del explorador de archivos en la barra de tareas
    global File_manager_button, File_manager_button_light, File_manager_taskbar_button
    File_manager_button = Asset_color("File manager", "File_manager_icon.png", "24x24", "#ff00ff", "#00142D")
    File_manager_button_light = Asset_color("File manager", "File_manager_icon.png", "24x24", "#ff00ff", "#001B3D")

    File_manager_taskbar_button = Button(
        Taskbar,
        borderwidth="0",
        relief="flat",
        bg="#00142D",
        activebackground = "#00142D",
        command=File_manager,
        image = File_manager_button
    )

    File_manager_taskbar_button.bind("<Enter>", lambda event: File_manager_taskbar_button.config(image = File_manager_button_light))
    File_manager_taskbar_button.bind("<Leave>", lambda event: File_manager_taskbar_button.config(image = File_manager_button))


    # Icono del navegador en la barra de tareas
    global Browser_button, Browser_button_light, Browser_taskbar_button
    Browser_button = Asset_color("Browser", "Browser_icon.png", "24x24", "#ff00ff", "#00142D")
    Browser_button_light = Asset_color("Browser", "Browser_icon.png", "24x24", "#ff00ff", "#001B3D")

    Browser_taskbar_button = Button(
        Taskbar,
        borderwidth="0",
        relief="flat",
        bg="#00142D",
        activebackground = "#00142D",
        command = Browser_programm,
        image = Browser_button
    )

    Browser_taskbar_button.bind("<Enter>", lambda event: Browser_taskbar_button.config(image = Browser_button_light))
    Browser_taskbar_button.bind("<Leave>", lambda event: Browser_taskbar_button.config(image = Browser_button))

    # se crea una lista de los botones de la barra de tarea
    global taskbar_buttons
    taskbar_buttons = [Terminal_taskbar_button, File_manager_taskbar_button, Browser_taskbar_button]

    # los botones se posicionan en la barra de tareas en el orden de la lista
    for i in range(len(taskbar_buttons)):
        taskbar_buttons[i].place(x=8 + (i * 32), y=2)


 # ---------------------------------------------------------[ Widgets de la barra de reloj ]--------------------------------------------------------


    # Widget base para los iconos de la barra del reloj
    global Clokcbar_taskbar_icons, Clockbar_icons
    Clockbar_taskbar_icons = Asset("Taskbar", "Taskbar_Icons.png")

    Clockbar_icons = Label(
        Taskbar,
        width=164,
        height=28,
        borderwidth="0",
        relief="raised",
        bg="#001023",
        image = Clockbar_taskbar_icons
    )
    Clockbar_icons.place(x=755, y=1)


    # -------------------------------------------------------------[ Barra del reloj ]-----------------------------------------------------------

    global Clock, clock

    def clock():
        global Time
        Time = time.strftime("%I:%M %p")
        Date = time.strftime("%d/%m/%Y")

        ClockStr = ""
        ClockStr += Time
        ClockStr += "\n"
        ClockStr += Date

        Clock.config(text=ClockStr)
        Clock.after(200, clock)


    Clock = Label(
        Clockbar_icons,
        width = 12,
        height = 2,
        borderwidth = "0",
        background = "#001023",
        foreground = "#F3F3F3",
        relief = "raised",
        font=("Segoe UI Semibold", 7),
        text = "",
    )

    Clock.place(x= 96, y= -1)

    clock()

    # Icono del estado de la bateria
    global Battery_taskbar_icon, Battery_status_icon
    Battery_taskbar_icon = Asset("Taskbar", "Battery.png")

    Battery_status_icon = Button(
        Clockbar_icons,
        width=20,
        height=40,
        borderwidth="0",
        relief="flat",
        bg="#001023",
        image=Battery_taskbar_icon,
        command = Settings_error
    )
    Battery_status_icon.place(x=16, y=-6)


    # Internet status icon
    global Internet_icon, Internet_status_icon

    if internet_on() == True:
        # Connected
        Internet_icon = Asset("Taskbar", "Internet_connected.png")
    else:
        # Disconnected
        Internet_icon = Asset("Taskbar", "Internet_warning.png")

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
    Internet_status_icon.place(x=38, y=-6)


    # Sound volume icon
    global Volume_icon, Volume_status_icon
    Volume_icon = Asset("Taskbar", "Volume.png")

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
    Volume_status_icon.place(x=60, y=-6)


 # ----------------------------------------------------------------- [ Start menu icons ] --------------------------------------------------

    #global Settings_Start_icon, Settings_Start_icon_2
    #Settings_Start_icon = Asset("Assets/Images/Settings_Icon.png")
    #Settings_Start_icon_2 = Asset("Assets/Images/Settings_Icon_2.png")
