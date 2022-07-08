import time
from tkinter import Button, Frame, Label

from Libs.pyImage.Image import setImage
from Libs.pyLogger.Logger import Logger

from System.Core.Core import boot
from System.Core.Kernel import bug_check
from System.Programs.Browser.Browser import Browser
from System.Programs.File_manager.File_manager import File_manager
from System.Programs.Terminal.Terminal import Terminal
from System.Programs.Map.Map import Map
from System.Programs.Welcome_dialog.Welcome import Welcome_dialog
from System.Shell.Boot.Desktop.Startmenu import startmenu
from System.Shell.Message_box import Message_box
from System.Utils.Utils import Execute, check_internet
from System.Utils.Vars import XCursor_2

__author__ = 'TheBigEye'
__version__ = '2.0'

def Terminal_programm(master):
    Execute(master, 800, Terminal, master, True)

def File_manager_programm(master):
    Execute(master, 1000, File_manager, master, True)

def Browser_programm(master):
    Message_box(master, "Warning", "Browser", "this may not work very well", True)
    #Execute(master, 1200, Browser, master, True) # REMOVED: Browser is not working properly and will be fixed in the future.
    for widget in master.winfo_children():
        widget.destroy()

    bc = bug_check(master, "0x00000007" , "#ffffff", "#000000")

    master.after(3000, bc)

def Map_programm(master):
    Execute(master, 800, Map, master, True)

class Desktop(Frame):
    def __init__(self, master):

        Frame.__init__(self, master)

        self.master = master

        # Initialize the desktop
        Desktop.desktop_initializer(self)
        Logger.info("### Desktop initialized!")

# -------------------------------------------------------------[ Desktop ]--------------------------------------------------------------

    def desktop_initializer(self):

        Logger.info("### Loading desktop enviroment ...")

        # Initialize the Wallpaper
        self.Wallpaper_image = setImage("Assets/Shell/Desktop/Wallpapers/default.png")
        self.Wallpaper = Label(
            self.master,
            image= self.Wallpaper_image,
            borderwidth="0",
            relief="flat",
            bg="#001023"
        )
        self.Wallpaper.place(x=0, y=0)
        Logger.info("Wallpaper processed and loaded")

        # Initialize the Cursor
        self.master.configure(background = "#001023",cursor = XCursor_2)
        Logger.info("Cursor processed and loaded")

        # Initialize the Taskbar
        self.Taskbar_image = setImage("Assets/Shell/Desktop/Taskbar/Taskbar.png")
        self.Taskbar = Label(
            self.master,
            width = 740,
            height = 29,
            borderwidth = "0",
            image = self.Taskbar_image,
            background = "black",
            foreground = "gray",
            relief = "raised",
        )
        self.Taskbar.place(x= 109, y= 571)
        self.Taskbar.lift()
        Logger.info("Taskbar processed and loaded")

        # Initialize the Start bar
        self.Startbar_image = setImage("Assets/Shell/Desktop/Taskbar/Startbar.png")
        self.Startbar = Label(
            self.master,
            width = 109,
            height = 29,
            borderwidth = "0",
            image = self.Startbar_image,
            background = "white",
            foreground = "gray",
            relief = "raised",
        )
        self.Startbar.place(x= 0, y= 571)
        self.Startbar.lift()
        Logger.info("Startbar processed and loaded")

        # Initialize the Clockbar
        self.Clockbar_image = setImage("Assets/Shell/Desktop/Taskbar/Clockbar.png")
        self.Clockbar = Label(
            self.master,
            width = 284,
            height = 29,
            borderwidth = "0",
            image = self.Clockbar_image,
            background = "white",
            foreground = "gray",
            relief = "raised",
        )
        self.Clockbar.place(x= 849, y= 571)
        self.Clockbar.lift()
        Logger.info("Clockbar processed and loaded")

        # Initialize the Start menu
        startmenu(self.master, self.Startbar)

# -------------------------------------------------------------[ Startbar buttons ]-----------------------------------------------------------

        # Modules icon in startbar
        self.Modules_button = setImage("Assets/Shell/Desktop/Taskbar/Modules_icon.png", (24,24), "#ff00ff", "#002C4F")
        self.Modules_button_light = setImage("Assets/Shell/Desktop/Taskbar/Modules_icon.png", (24,24), "#ff00ff", "#00345B")
        self.Modules_startbar_button = Button(
            self.Startbar,
            borderwidth="0",
            relief="raised",
            bg = "#002C4F",
            activebackground = "#002C4F",
            image= self.Modules_button
        )
        self.Modules_startbar_button.place(x=35, y=2)
        self.Modules_startbar_button.bind("<Button-1>", lambda event: Map_programm(self.master))
        self.Modules_startbar_button.bind("<Enter>", lambda event: self.Modules_startbar_button.config(image = self.Modules_button_light))
        self.Modules_startbar_button.bind("<Leave>", lambda event: self.Modules_startbar_button.config(image = self.Modules_button))
        Logger.info("Modules icon loaded on startbar")


        # Search icon in startbar
        self.Search_button = setImage("Assets/Shell/Desktop/Taskbar/Search_icon.png", (24, 24), "#ff00ff", "#002C4F")
        self.Search_button_light = setImage("Assets/Shell/Desktop/Taskbar/Search_icon.png", (24, 24), "#ff00ff", "#00345B")
        self.Search_startbar_button = Button(
            self.Startbar,
            borderwidth="0",
            relief="raised",
            bg = "#002C4F",
            activebackground = "#002C4F",
            image= self.Search_button
        )
        self.Search_startbar_button.place(x=66, y=2)
        self.Search_startbar_button.bind("<Button-1>", lambda event: Terminal_programm(self.master))
        self.Search_startbar_button.bind("<Enter>", lambda event: self.Search_startbar_button.config(image = self.Search_button_light))
        self.Search_startbar_button.bind("<Leave>", lambda event: self.Search_startbar_button.config(image = self.Search_button))
        Logger.info("Search icon loaded on startbar")

# -------------------------------------------------------------[ Taskbar buttons ]-----------------------------------------------------------

        # Terminal icon in taskbar
        self.Terminal_button = setImage("Assets/Shell/Programs/Terminal/Terminal_icon.png", (24, 24), "#ff00ff", "#00142D")
        self.Terminal_button_light = setImage("Assets/Shell/Programs/Terminal/Terminal_icon.png", (24, 24), "#ff00ff", "#001B3D")
        self.Terminal_taskbar_button = Button(
            self.Taskbar,
            borderwidth="0",
            relief="flat",
            bg="#00142D",
            activebackground = "#00142D",
            image = self.Terminal_button
        )
        self.Terminal_taskbar_button.bind("<Button-1>", lambda event: Terminal_programm(self.master))
        self.Terminal_taskbar_button.bind("<Enter>", lambda event: self.Terminal_taskbar_button.config(image = self.Terminal_button_light))
        self.Terminal_taskbar_button.bind("<Leave>", lambda event: self.Terminal_taskbar_button.config(image = self.Terminal_button))
        Logger.info("Terminal icon loaded on taskbar")

        # File manager icon in taskbar
        self.File_manager_button = setImage("Assets/Shell/Programs/File manager/File_manager_icon.png", (24, 24), "#ff00ff", "#00142D")
        self.File_manager_button_light = setImage("Assets/Shell/Programs/File manager/File_manager_icon.png", (24, 24), "#ff00ff", "#001B3D")
        self.File_manager_taskbar_button = Button(
            self.Taskbar,
            borderwidth="0",
            relief="flat",
            bg="#00142D",
            activebackground = "#00142D",
            image = self.File_manager_button
        )
        self.File_manager_taskbar_button.bind("<Button-1>", lambda event: File_manager_programm(self.master))
        self.File_manager_taskbar_button.bind("<Enter>", lambda event: self.File_manager_taskbar_button.config(image = self.File_manager_button_light))
        self.File_manager_taskbar_button.bind("<Leave>", lambda event: self.File_manager_taskbar_button.config(image = self.File_manager_button))
        Logger.info("File manager icon loaded on taskbar")

        # Browser icon in taskbar
        self.Browser_button = setImage("Assets/Shell/Programs/Browser/Browser_icon.png", (24, 24), "#ff00ff", "#00142D")
        self.Browser_button_light = setImage("Assets/Shell/Programs/Browser/Browser_icon.png", (24, 24), "#ff00ff", "#001B3D")
        self.Browser_taskbar_button = Button(
            self.Taskbar,
            borderwidth="0",
            relief="flat",
            bg="#00142D",
            activebackground = "#00142D",
            image = self.Browser_button
        )
        self.Browser_taskbar_button.bind("<Button-1>", lambda event: Browser_programm(self.master))
        self.Browser_taskbar_button.bind("<Enter>", lambda event: self.Browser_taskbar_button.config(image = self.Browser_button_light))
        self.Browser_taskbar_button.bind("<Leave>", lambda event: self.Browser_taskbar_button.config(image = self.Browser_button))
        Logger.info("Browser icon loaded on taskbar")

        # se crea una lista de los botones de la barra de tarea
        self.taskbar_buttons = [self.Terminal_taskbar_button, self.File_manager_taskbar_button, self.Browser_taskbar_button]

        # los botones se posicionan en la barra de tareas en el orden de la lista
        for i in range(len(self.taskbar_buttons)):
            self.taskbar_buttons[i].place(x=8 + (i * 32), y=2)
        Logger.info("Taskbar buttons loaded and palced")

        # self.master.after(2000, Welcome_dialog(self.master, False))

# -------------------------------------------------------------[ Clockbar ]-----------------------------------------------------------

        # Clock icon in clockbar
        def clock():
            Time = time.strftime("%I:%M %p")
            Date = time.strftime("%d/%m/%Y")

            ClockStr = ""
            ClockStr += Time
            ClockStr += "\n"
            ClockStr += Date

            self.Clock.config(text=ClockStr)
            self.Clock.after(200, clock)

        self.Clock = Label(
            self.Clockbar,
            width = 12,
            height = 2,
            borderwidth = "0",
            background = "#002C4F",
            foreground = "#F3F3F3",
            relief = "raised",
            font=("Segoe UI Semibold", 7),
            text = "",
        )
        self.Clock.place(x= 96, y= 0.5)
        clock()
        Logger.info("Clock component loaded")

        # Sound volume icon in clockbar
        self.Sound_button = setImage("Assets/Shell/Desktop/Taskbar/high-volume.png", (24, 24), "#ff00ff", "#002C4F")
        self.Sound_button_light = setImage("Assets/Shell/Desktop/Taskbar/high-volume.png", (24, 24), "#ff00ff", "#004C82")
        self.Sound_clockbar_button = Button(
            self.Clockbar,
            width = 16,
            height = 32,
            borderwidth="0",
            relief="flat",
            bg="#002C4F",
            activebackground = "#002C4F",
            image = self.Sound_button
        )
        self.Sound_clockbar_button.bind("<Button-1>", lambda event: Message_box(self.master, "Info", "Sound", "In development...", True))
        self.Sound_clockbar_button.bind("<Enter>", lambda event: self.Sound_clockbar_button.config(image = self.Sound_button_light))
        self.Sound_clockbar_button.bind("<Leave>", lambda event: self.Sound_clockbar_button.config(image = self.Sound_button))
        Logger.info("Sound volume icon loaded on clockbar")

        # Battery icon in clockbar
        self.Battery_button = setImage("Assets/Shell/Desktop/Taskbar/high-battery.png", (24, 24), "#ff00ff", "#002C4F")
        self.Battery_button_light = setImage("Assets/Shell/Desktop/Taskbar/high-battery.png", (24, 24), "#ff00ff", "#004C82")
        self.Battery_clockbar_button = Button(
            self.Clockbar,
            width = 16,
            height = 32,
            borderwidth="0",
            relief="flat",
            bg="#002C4F",
            activebackground = "#002C4F",
            image = self.Battery_button
        )
        self.Battery_clockbar_button.bind("<Button-1>", lambda event: Message_box(self.master, "Error", "Battery", "Nice error :)", True))
        self.Battery_clockbar_button.bind("<Enter>", lambda event: self.Battery_clockbar_button.config(image = self.Battery_button_light))
        self.Battery_clockbar_button.bind("<Leave>", lambda event: self.Battery_clockbar_button.config(image = self.Battery_button))
        Logger.info("Battery icon loaded on clockbar")

        # Internet icon in clockbar
        self.Internet_button = setImage("Assets/Shell/Desktop/Taskbar/high-internet.png", (24, 24), "#ff00ff", "#002C4F")
        self.Internet_button_light = setImage("Assets/Shell/Desktop/Taskbar/high-internet.png", (24, 24), "#ff00ff", "#004C82")
        self.Internet_clockbar_button = Button(
            self.Clockbar,
            width = 16,
            height = 32,
            borderwidth="0",
            relief="flat",
            bg="#002C4F",
            activebackground = "#002C4F",
            image = self.Internet_button
        )
        self.Internet_clockbar_button.bind("<Button-1>", lambda event: Message_box(self.master, "Warning", "Internet", "Nice warning :)", True))
        self.Internet_clockbar_button.bind("<Enter>", lambda event: self.Internet_clockbar_button.config(image = self.Internet_button_light))
        self.Internet_clockbar_button.bind("<Leave>", lambda event: self.Internet_clockbar_button.config(image = self.Internet_button))
        Logger.info("Internet icon loaded on clockbar")

        # se crea una lista de los botones de la barra de tarea
        self.clockbar_buttons = [self.Battery_clockbar_button, self.Internet_clockbar_button, self.Sound_clockbar_button]

        # los botones se posicionan en la barra de tareas en el orden de la lista
        for i in range(len(self.clockbar_buttons)):
            self.clockbar_buttons[i].place(x=16 + (i * 24), y=-2)
        Logger.info("Clockbar buttons loaded and palced")
