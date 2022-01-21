from tkinter import Button, Label
import time
from System.GUI.Attributes.Draggable import make_draggable_button

from System.GUI.Browser import Display_Browser
from System.GUI.FileManager import Display_FileManager
from System.GUI.MessageBox import MessageBox
from System.GUI.Terminal import Terminal
from System.Utils.Utils import get_asset, print_log, Execute

__author__ = 'Nahuel senek'
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

    print_log("Escritorio cargado y ejecutandose")

    global Wallpaper, Desktop_wallpaper

    master.configure(background = "#000000")  # Establece el fondo a color azul

    Wallpaper = get_asset("Assets/Wallpapers/BlissHill.png")
    Desktop_wallpaper = Label(master, image= Wallpaper, borderwidth="0.1")
    Desktop_wallpaper.place(x=0, y=0) # Posiciona el fondo de escritorio en el centro


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

    global File_manager, Terminal, Browser

    # LLama al metodo del Explorador de archivos en forma de aplicacion
    def File_manager():
        Close_start_menu()

        Display_FileManager(master, "This PC", draggable=True)


    # LLama a la terminal
    def Terminal_programm():
        Close_start_menu()

        Execute(master, 1512, Terminal, master, True)


    # LLama al navegador
    def Browser():
        Close_start_menu()

        Display_Browser(master, draggable=True)

 # ------------------------------------------------------------[ Barra de tareas ]------------------------------------------------------------------

    global Taskbar_GUI_Image, Taskbar

    Taskbar_GUI_Image = get_asset("Assets/GUI/Taskbar/Taskbar.png")

    # Barra de tareas
    Taskbar = Label(
        master,
        width = 915,
        height = 29,
        borderwidth = "0",
        image = Taskbar_GUI_Image,
        background = "black",
        foreground = "gray",
        relief = "raised",
    )

    Taskbar.place(x= 109, y= 571)



    global Startbar_GUI_Image, Startbar
    Startbar_GUI_Image = get_asset("Assets/GUI/Taskbar/Startbar.png")

    # Barra de inicio
    Startbar = Label(
        master,
        width = 109,
        height = 29,
        borderwidth = "0",
        image = Startbar_GUI_Image,
        background = "white",
        foreground = "gray",
        relief = "raised",
    )

    Startbar.place(x= 0, y= 571)



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

    Clockbar.place(x=850, y=1)

    # El reloj
    def times():

        current_time = time.strftime("%H: %M")
        clock.config(bg="#080D11", text=current_time, fg="white", font=("Segou UI", 9))
        clock.after(1, times)

    clock = Label(Taskbar, borderwidth="0", relief="raised")
    clock.after(1, times)
    clock.place(x=865, y=6)


 # ------------------------------------------------------------[ Menu de inicio ]-------------------------------------------------------------------

    # Widget base del menu de inicio
    global Start_menu_GUI, Start_menu
    Start_menu_GUI = get_asset("Assets/GUI/Start menu/StartMenu.png")

    Start_menu = Label(
        master,
        width = 314,
        height = 440,
        image = Start_menu_GUI,
        borderwidth = "0"
    )

    global Start_menu_button, Start_menu_active_button, Open_start_menu, Close_start_menu, Open_start_button, Close_start_button
    Start_menu_button = get_asset("Assets/GUI/Start menu/Start_Button.png")
    Start_menu_active_button = get_asset("Assets/GUI/Start menu/Start_Button_active.png")

    # Abre
    def Open_start_menu():
        Start_menu.place(x=1, y=126)
        Start_menu.lift()
        time.sleep(0.1)

        Open_start_button.place_forget()
        Close_start_button.place(x=6, y=2)

    # Cierra
    def Close_start_menu():
        Start_menu.place_forget()
        time.sleep(0.1)

        Open_start_button.place(x=6, y=2)
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
    Open_start_button.place(x=6, y=2)

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
    Modules_startbar_icon = get_asset("Assets/GUI/Taskbar/Modules_button.png")
    Modules_startbar_active_icon = get_asset("Assets/GUI/Taskbar/Modules_button_active.png")

    Modules_startbar_button = Button(
        Startbar,
        width=28,
        height=25,
        borderwidth="0",
        relief="raised",
        bg = "#070E11",
        image= Modules_startbar_icon,
        command=Terminal_programm
    )
    Modules_startbar_button.place(x=42, y=2)

    Modules_startbar_button.bind("<Enter>", lambda event: Modules_startbar_button.config(image = Modules_startbar_active_icon))
    Modules_startbar_button.bind("<Leave>", lambda event: Modules_startbar_button.config(image = Modules_startbar_icon))


    # icono de busqueda
    global Search_startbar_icon, Search_startbar_active_icon, Search_startbar_button
    Search_startbar_icon = get_asset("Assets/GUI/Taskbar/Search_button.png")
    Search_startbar_active_icon = get_asset("Assets/GUI/Taskbar/Search_button_active.png")

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
    Search_startbar_button.place(x=76, y=2)

    Search_startbar_button.bind("<Enter>", lambda event: Search_startbar_button.config(image = Search_startbar_active_icon))
    Search_startbar_button.bind("<Leave>", lambda event: Search_startbar_button.config(image = Search_startbar_icon))

 # ----------------------------------------------------[ Botones de la barra de tareas ]------------------------------------------------------------



    # Icono de la aplicacion de terminal en la barra de tareas
    global Terminal_taskbar_icon, Terminal_taskbar_active_icon, Terminal_taskbar_button
    Terminal_taskbar_icon = get_asset("Assets/GUI/Terminal/Terminal_taskbar_icon.png")
    Terminal_taskbar_active_icon = get_asset("Assets/GUI/Terminal/Terminal_taskbar_active_icon.png")

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
    File_manager_taskbar_icon = get_asset("Assets/GUI/File manager/FileManager_taskbar_icon.png")
    File_manager_taskbar_active_icon = get_asset("Assets/GUI/File manager/FileManager_taskbar_active_icon.png")

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
    Browser_taskbar_icon = get_asset("Assets/GUI/Browser/Browser_taskbar_icon.png")
    Browser_taskbar_active_icon = get_asset("Assets/GUI/Browser/Browser_taskbar_active_icon.png")

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
    #Browser_taskbar_button.place(x=76, y=2)#116

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
    Clockbar_taskbar_icons = get_asset("Assets/Taskbar_Icons.png")

    Clockbar_icons = Label(
        Taskbar,
        width=100,
        height=28,
        borderwidth="0",
        relief="raised",
        bg="#070E11",
        image = Clockbar_taskbar_icons
    )
    Clockbar_icons.place(x=755, y=1)


    # Icono del estado de la bateria
    global Battery_taskbar_icon, Battery_status_icon
    Battery_taskbar_icon = get_asset("Assets/Images/Battery.png")

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
    global Internet_Warning_icon, Internet_Connected_icon, Internet_status_icon

    # Estado desconectado
    Internet_Warning_icon = get_asset("Assets/Images/Internet_Warning.png")

    # Estado conectado
    Internet_Connected_icon = get_asset("Assets/Images/Internet_Connected.png")

    Internet_status_icon = Button(
        Clockbar_icons,
        width=20,
        height=40,
        borderwidth="0",
        relief="flat",
        bg="#080D11",
        image=Internet_Connected_icon,
        command = Print_error
    )
    Internet_status_icon.place(x=48, y=-6)


    # Icono de volumen del sonido
    global Volume_icon, Volume_status_icon
    Volume_icon = get_asset("Assets/Images/Volume.png")

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
    global Settings_Start_icon, Settings_Start_icon_2
    Settings_Start_icon = get_asset("Assets/Images/Settings_Icon.png")
    Settings_Start_icon_2 = get_asset("Assets/Images/Settings_Icon_2.png")