# -*- coding: utf-8 -*-

"""
    Module Name:
        OS.py

    Abstract:
        This module implements the Python OS main window and args parser.

    Author:
        TheBigEye 2-Jul-2021
"""

import tkinter as tk
from sys import argv, exit
from tkinter import PhotoImage

from Libs.pyLogger.Logger import Logger
from Libs.pyUtils.pyFetch import Color, get_neofetch
from System.Core.Kernel import python_modules_check

# ------------------------------------------[ Main ]------------------------------------------- #

# FIXME: Here, somewhere in this module, there is a big performance loss (slow start)

class main(tk.Tk):
    """ This class implements the main window of the OS. """

    def __init__(self):
        """ Initializes the system """

        from System.Core.Core import boot_check
        from System.Core.Kernel import screen_check

        super().__init__()

        self.title("Python OS")

        self.WIDTH = 1024
        self.HEIGHT = 600

        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.window_x = (self.screen_width/2) - (self.WIDTH /2)
        self.window_y = (self.screen_height/2) - (self.HEIGHT/2)

        self.geometry('%dx%d+%d+%d' % (self.WIDTH, self.HEIGHT, self.window_x, self.window_y))
        self.resizable(False, False)

        self.icon = PhotoImage(file = "Assets/Icon.png")

        self.configure(background= "#000000")
        self.wm_iconphoto(True, self.icon)

        screen_check(self) # Check if the screen is big
        boot_check(self) # Start the boot process

        self.update()

        self.mainloop()

    def stop(self):
        """ Stops the system """
        self.destroy()
        exit()

def start_runtime():
    """
    This function gets the arguments from the command line.

    Example:
        >>> python OS.py --help --version --delete-logs --set-boot
    """

    from System.Core.Core import set_boot

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
        print(get_neofetch("Assets/Data/logo.txt", Color.YELLOW, ["*", None, None, "#", None, None, None]))

    # Check if the user wants to start the system
    if "--run-clean" in arguments:
        import os
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        Logger.delete_logs()
        main()


    # If no arguments are given, run the OS
    if len(arguments) == 1:
        main()

if __name__ == "__main__":
    start_runtime()

# -------------------------------------------[ End ]------------------------------------------- #
