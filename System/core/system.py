"""
    Module Name:
        System.py

    Abstract:
        This module implements the Python OS main window and args parser.

    Author:
        TheBigEye 2-Jul-2021 - Initial Version written on OS.py
        TheBigEye 31-Jul-2022 - Updated Version moved to System.py
"""

import os
from tkinter import PhotoImage, Tk

from Libs.pyLogger.Logger import Logger
from Libs.pyUtils.pyFetch import Color, get_neofetch

from System.core.boot import boot_check, set_boot, set_desktop_mode
from System.core.kernel import screen_check

OS_NAME = "Python OS"
OS_VERSION = "0.0.2"
OS_AUTHOR = "TheBigEye"
OS_LICENSE = "GPLv3"
OS_COPYRIGHT = "Copyright (C) 2022 TheBigEye"
OS_DESCRIPTION = "A simple OS simulator written in Python"

START_PROCESSES = {
    "SCREEN CHECK": [screen_check],
    "BOOT CHECK": [boot_check]
}

class Display(Tk):
    """ Start the window amd run the procresses """

    def __init__(self, processes: dict) -> None:
        """ Initializes the system """

        super().__init__()

        self.processes = processes
        self.title("Python OS")

        self.WIDTH = 1024
        self.HEIGHT = 600

        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.window_x = (self.screen_width /2) - (self.WIDTH /2)
        self.window_y = (self.screen_height /2) - (self.HEIGHT /2)

        self.geometry('%dx%d+%d+%d' % (self.WIDTH, self.HEIGHT, self.window_x, self.window_y))
        self.resizable(False, False)

        self.ICON = PhotoImage(file = "Assets/Icon.png")

        self.configure(background= "#000000")
        self.wm_iconphoto(True, self.ICON)

        # Run the processes
        for process in self.processes:
            for function in self.processes[process]:
                function(self)

        self.update()
        self.mainloop()

class System():
    """ Parse arguments"""

    def run(argv: list[str]) -> None:
        """ Get the arguments and run them """

        arguments = ()
        for arg in argv:
            arguments += (arg,)

        # Check if the user wants to see the help
        if "--help" in arguments:
            print("""
            Command line arguments:
                --help: Shows this help.
                --version: Shows the version.
                --delete-logs: Deletes the logs.
                --set-boot int: Sets the boot.
                --neofetch: Shows the neofetch.
            """)

        # Check if the user wants to see the version
        if "--version" in arguments:
            print("""
            This is the version of the OS.py script.
            """)

        # Check if the user wants to delete the logs
        if "--delete-logs" in arguments:
            Logger.delete_logs()

        # Check if the user wants to set the boot
        if "--set-boot" in arguments:
            # get the value of the boot
            boot = arguments[arguments.index("--set-boot") + 1]
            # set the boot
            set_boot(boot)

        # Check if the user see the neofetch
        if "--neofetch" in arguments:
            print(
                get_neofetch(
                    "Assets/Data/logo.txt",
                    Color.YELLOW,
                    ["*", None, None, "#", None, None, None]
                )
            )

        # Check if the user wants to start the system
        if "--run-clean" in arguments:
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
            Logger.delete_logs()
            Display(START_PROCESSES)

        if "--wm" in arguments:
            set_desktop_mode("0")

        if "--de" in arguments:
            set_desktop_mode("1")

        # If no arguments are given, run the OS
        if len(arguments) == 1:
            Display(START_PROCESSES)
