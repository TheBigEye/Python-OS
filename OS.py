"""
    Module Name:
        OS.py

    Abstract:
        This module implements the Python OS main window and executable.

    Author:
        TheBigEye (Nahuel senek) 2-Jul-2021
"""

import os
import sys
import tkinter as tk
from tkinter import PhotoImage

from System.Core.Core import boot_check, delete_logs, routines, set_boot
from System.Utils.Colormap import Black
from System.Utils.Utils import Logger
from System.Utils.Vars import Assets_directory, XCursor_2

# -------------------------------------------[ Main ]------------------------------------------- #

def main():

    """
    This is the main function of the OS.
    """

    Os = tk.Tk()  # Create the window that will be the base of the program.
    Os.title("Python OS")  # Window title.

    Os.geometry("1024x600")  # Window size.
    Os.resizable(False, False)  # Window resizing.

    if os.name == "nt": # Window
        icon = PhotoImage(file=Assets_directory + "/Icon.png")
        Os.iconphoto(False, icon)
        Os.configure(background = Black, cursor = XCursor_2)
    else:
        Os.configure(background = Black)


    # In case the device screen resolution is too lower, a warning will be displayed
    if (Os.winfo_screenwidth() < 1024 or Os.winfo_screenheight() < 600):
        Logger.warning("The screen resolution is too low. The program may not work properly.")

    routines() # Execute system routines
    boot_check(Os) # Start the boot process

    Os.mainloop() # Tkinter main loop


def args_check():

    """
    This function gets the arguments from the command line.
    """

    args = sys.argv[1:]

    if len(args) == 0:
        main()
        return

    if args[0] == "--help":
        print("------------------------------------------------------")
        print("--help:          Show this help")
        print("--version:       Show the version of the program")
        print("--delete-logs:   Delete all logs")
        print("--set-boot:      Set the boot value")
        print("------------------------------------------------------")
        return

    if args[0] == "--version":
        print("Python OS v1.0")
        return

    if args[0] == "--delete-logs":
        print("Deleting logs...")
        delete_logs()
        return

    # --set-boot int
    if args[0] == "--set-boot":
        if len(args) == 2:
            try:
                set_boot(int(args[1]))
            except ValueError:
                print("ERROR: The boot value must be an integer.")
                return
        else:
            print("ERROR: The boot value must be an integer.")
            return

if __name__ == "__main__":
    args_check()

# -------------------------------------------[ End ]------------------------------------------- #

