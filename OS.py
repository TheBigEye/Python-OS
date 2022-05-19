# -*- coding: utf-8 -*-

"""
    Module Name:
        OS.py

    Abstract:
        This module implements the Python OS main window and executable.

    Author:
        TheBigEye 2-Jul-2021
"""

import os
import sys
import tkinter as tk
from tkinter import PhotoImage

from System.Core.Core import boot_check, delete_logs, routines, set_boot
from System.Utils.Colormap import Black
from System.Utils.Logger import Logger
from System.Utils.Vars import Assets_directory, XCursor_2

# ------------------------------------------[ Main ]------------------------------------------- #

# FIXME: Here, somewhere in this module, there is a big performance loss (slow start)

def main():

    """ This is the main function of the OS. """

    Os = tk.Tk()  # Create the window that will be the base of the program.
    Os.title("Python OS")  # Window title.

    Os.geometry("1024x600")  # Window size.
    Os.resizable(False, False)  # Window resizing.

    if os.name == "nt": # Window
        icon = PhotoImage(file=Assets_directory + "/Icon.png")
        Os.iconphoto(False, icon)
        Os.configure(background= Black, cursor = XCursor_2)
    else:
        Os.configure(background= Black)

    # In case the device screen resolution is too lower, a warning will be displayed
    if (Os.winfo_screenwidth() < 1024 or Os.winfo_screenheight() < 600):
        Logger.warning("The screen resolution is too low. The program may not work properly.")

    routines() # Execute system routines
    boot_check(Os) # Start the boot process

    Os.mainloop() # Tkinter main loop


def run():

    """
    This function gets the arguments from the command line.

    Example:
        >>> python OS.py --help --version --delete-logs --set-boot
    """

    args = sys.argv[1:]

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

    def delete_logs_arg():
        delete_logs()

    def set_boot_arg():
        set_boot(sys.argv[2])

    def debug_arg():
        Logger.showConsole = True
        Logger.header()
        Logger.info("----------------- Debug mode activated -----------------")
        main()

    if len(args) == 0:
        main()
    else:
        match args[0]:
            case "--help"        | "--h":  help_arg()
            case "--version"     | "--v":  version_arg()
            case "--debug"       | "--d":  debug_arg()
            case "--delete-logs" | "--dl": delete_logs_arg()
            case "--set-boot"    | "--b":  set_boot_arg()
            case _:
                Logger.info("Invalid argument {}, use --help to see the help.", args[0])
                sys.exit()

# AVOID running the program directly by importing it
if __name__ == "__main__":
    run()

# -------------------------------------------[ End ]------------------------------------------- #
