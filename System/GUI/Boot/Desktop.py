from tkinter import Button, Entry, Label, PhotoImage, Tk
import time

from System.GUI.FileManager import Display_FileManager
from System.GUI.MessageBox import Display_MessageBox
from System.GUI.Terminal import Display_Terminal

#from System.Utils.Utils import print_log

__author__ = 'TheBigEye'
__version__ = '2.0'


def Desktop(master):

 # Documentation ---------------------------------------------------------------------------------------------------------------

    """
    This function is used to create the desktop.

    Parameters
    ----------
    master : str
        The Tkinter object which is the parent of all widgets.

    Returns
    -------
        None
    """

  # ------------------------------------------------------[ Desktop ]----------------------------------------------------------------

    #print_log("Desktop: Loaded desktop functions and running")    

    global Wallpaper, Desktop_wallpaper


    master.configure(background = "#000000")  # Sets the background to Blue

    Wallpaper = PhotoImage(file = "Assets/Wallpapers/BlissHill.png")
    Desktop_wallpaper = Label(master, image= Wallpaper, borderwidth="0.1")
    Desktop_wallpaper.place(x=0, y=0)

 # ------------------------------------------------------[ Error types ]------------------------------------------------------------

    global Settings_error, Print_error, This_PC_error, FileManager_error

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
    

 # ------------------------------------------------------[ Programs ]---------------------------------------------------------------

    global File_manager, Terminal

    def File_manager():
        Close_start_menu()
        Display_FileManager(master, "This PC", draggable=True)

    def Terminal():
        Close_start_menu()
        Display_Terminal(master, draggable=True)

 # ------------------------------------------------------[ Taskbar ]----------------------------------------------------------------

    global Taskbar_GUI_Image, Taskbar

    Taskbar_GUI_Image = PhotoImage(file = "Assets/GUI/Taskbar.png") 

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


 # -----------------------------------------------------[ Clockbar ]----------------------------------------------------------------

    global Clockbar

    Clockbar = Label(
        Taskbar,
        width=70,
        height=28,
        borderwidth="0",
        relief="raised",
        bg="#080D11",
    )

    Clockbar.place(x=950, y=1)

    def times():

        current_time = time.strftime("%H: %M")
        clock.config(bg="#080D11", text=current_time, fg="white", font=("Segou UI", 9))
        clock.after(1, times)

    clock = Label(Taskbar, borderwidth="0", relief="raised")
    clock.after(1, times)
    clock.place(x=965, y=6)  


 # ----------------------------------------------------[Start menu]-----------------------------------------------------------------

    global Start_menu, Open_start_button, Close_start_button
    global Start_menu_GUI, Start_menu_button

    Start_menu_GUI = PhotoImage(file = "Assets/GUI/StartMenu.png")
    Start_menu_button = PhotoImage(file = "Assets/Buttons/Start_Button.png")

    Start_menu = Label(

        master,
        width = 314,
        height = 440,
        image = Start_menu_GUI,
        borderwidth = "0"
    )

    # Open 
    def Open_start_menu():
        Start_menu.place(x=1, y=126)
        time.sleep(0.1)

        Open_start_button.place_forget()
        Close_start_button.place(x=0, y=571)

    # Close
    def Close_start_menu():
        Start_menu.place_forget()
        time.sleep(0.1)

        Open_start_button.place(x=0, y=571)
        Close_start_button.place_forget()

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

 # ----------------------------------------------------[ Taskbar buttons ]------------------------------------------------------------

    global Terminal_taskbar_button, File_manager_taskbar_button, Browser_taskbar_button
    global Terminal_taskbar_icon, File_manager_taskbar_icon, Browser_taskbar_icon

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





    

    

