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

from System.Core.Kernel import python_modules_check

# ------------------------------------------[ Main ]------------------------------------------- #

# FIXME: Here, somewhere in this module, there is a big performance loss (slow start)

class main(tk.Tk):
    """ This class implements the main window of the OS. """

    def __init__(self):
        """ Initializes the system """

        from System.Core.Core import boot_check, routines
        from System.Core.Kernel import screen_check
        from System.Utils.Vars import Assets_directory, XCursor_2

        super().__init__()

        self.title("Python OS")
        self.geometry("1024x600")
        self.resizable(False, False)

        self.icon = PhotoImage(file = Assets_directory + "/Icon.png")

        if Current_OS.name == "nt":
            self.configure(cursor = XCursor_2)
            self.configure(background= "#000000")
            self.iconphoto(False, self.icon)
        else:
            self.configure(background= "#000000")

        screen_check(self) # Check if the screen is big
        routines() # Execute the routines (essential for the system)
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

    from Libs.pyLogger.Logger import Logger
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
        print("""
        Python OS version: 1.0.0
        """)

    def debug():
        Logger.info("---------------- Debug mode activated -----------------")
        main()

    if len(arguments) == 0:
        main()
    else:
        match arguments[0]:
            case "--help"        | "--h":  help_arg()
            case "--modules"     | "--mc":  python_modules_check()
            case "--version"     | "--v":  version_arg()
            case "--debug"       | "--d":  debug()
            case "--delete-logs" | "--dl": Logger.clean_logs()
            case "--set-boot"    | "--b":  set_boot(System.argv[2])
            case _:
                Logger.info("Invalid argument {}, use --help to see the help.", arguments[0])
                System.exit()

if __name__ == "__main__":
    run()

# -------------------------------------------[ End ]------------------------------------------- #
