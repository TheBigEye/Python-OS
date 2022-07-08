# -*- coding: utf-8 -*-

"""
    Module Name:
        OS.py

    Abstract:
        This module implements the Python OS main window and executable.

    Author:
        TheBigEye 2-Jul-2021
"""

import os as Current_OS
import sys as System
import tkinter as tk
from tkinter import PhotoImage

from Libs.pyLogger.Logger import Logger
from System.Core.Kernel import python_modules_check
from Libs.pyUtils.pyFetch import Color, get_neofetch

# ------------------------------------------[ Main ]------------------------------------------- #

# FIXME: Here, somewhere in this module, there is a big performance loss (slow start)

class main(tk.Tk):
    """ This class implements the main window of the OS. """

    def __init__(self):
        """ Initializes the system """

        from System.Core.Core import boot_check
        from System.Core.Kernel import screen_check
        from System.Utils.Vars import Assets_directory

        super().__init__()

        self.title("Python OS")
        self.geometry("1024x600+64+32")
        self.resizable(False, False)

        self.icon = PhotoImage(file = Assets_directory + "/Icon.png")

        if Current_OS.name == "nt":
            self.configure(background= "#000000")
            self.iconphoto(True, self.icon)
        else:
            self.configure(background= "#000000")

        screen_check(self) # Check if the screen is big

        boot_check(self) # Start the boot process

        self.mainloop()

    def stop(self):
        """ Stops the system """
        self.destroy()
        System.exit()

def run():
    """
    This function gets the arguments from the command line.

    Example:
        >>> python OS.py --help --version --delete-logs --set-boot
    """

    from System.Core.Core import set_boot

    arguments = System.argv[1:]

    def help_arg():
        print("""
        --help | --h:                Shows this help.
        --version | --v:             Shows the version of the program.
        --delete-logs | --dl:        Deletes the logs.
        --set-boot int | --b int:     Sets the boot value.
        """)

    def version_arg():
        print("Python OS version: 1.0.0")

    def neofetch_arg():
        print(get_neofetch("Assets/Data/logo.txt", Color.YELLOW, ["*", None, None, "#", None, None, None]))

    if len(arguments) == 0:
        main()
    else:
        match arguments[0]:
            case "--help"        | "--h":   help_arg()
            case "--modules"     | "--mc":  python_modules_check()
            case "--version"     | "--v":   version_arg()
            case "--delete-logs" | "--dl":  Logger.delete_logs()
            case "--set-boot"    | "--b":   set_boot(System.argv[2])
            case "--neofetch"    | "--nf":  neofetch_arg()
            case _:
                raise ValueError("Invalid argument {}, use --help to see the help.", arguments[0])

if __name__ == "__main__":
    run()

# -------------------------------------------[ End ]------------------------------------------- #
