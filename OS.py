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

from System.Core.Core import (
    isBSOD, isRSOD, isGSOD, isBIOS, isINSTALLER,
    isBootloader, isLogin, isDesktop,
    isBoot, routines, delete_logs, set_boot
)

from System.UI.Boot.BIOS import BIOS
from System.UI.Boot.Bootloader import Boot_loader
from System.UI.Boot.Desktop import Desktop
from System.UI.Boot.Installer import Os_Installer
from System.UI.Boot.Login import Login
from System.UI.Boot.RSOD import RSOD
from System.UI.Boot.BSOD import BSOD

from System.Utils.Colormap import Black
from System.Utils.Utils import print_error, print_info, print_log, print_warning
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
        Os.iconbitmap(Assets_directory + "/Icons/icon.ico")
        Os.configure(background = Black, cursor = XCursor_2)
    else:
        Os.configure(background = Black)


    # In case the device screen resolution is too lower, a warning will be displayed
    if (Os.winfo_screenwidth() < 1024 or Os.winfo_screenheight() < 600):
        print_warning("The screen resolution is too lower, the program may not work properly.")

    routines() # Execute system routines

    # -------------------------------------------[ Boot ]------------------------------------------- #


    # This part starts the important functions of the program
    def start_boot():
        """
        This function is used to start the boot process.
        """

        # Start bootloader animation
        Boot_loader(Os)

        # After 12 seconds (or when everything is loaded), launch the desktop.
        Os.after(12000, Desktop, Os)


    def boot_check():
        """
        This function is used to check if the boot process is complete.
        """

        # Here the variables of the boot order are checked and the corresponding function is executed:
        if isBSOD:
            BSOD(Os) # Black screen of death
            print_error("The system has failed!.")

            # Stop the program after 15 seconds.
            Os.after(15000, Os.destroy)

        elif isRSOD:
            RSOD(Os) # Red screen of death
            print_warning("The system has failed!!.")

            # Stop the program after 8 seconds.
            Os.after(8000, Os.destroy)

        elif isGSOD:
            BSOD(Os) # Green screen of death
            print_info("The system has failed?.")

            # Stop the program after 8 seconds.
            Os.after(8000, Os.destroy)

        elif isBIOS:
            BIOS(Os) # Start BIOS
            print_log("Starting from BIOS/UEFI")

        elif isINSTALLER:
            Os_Installer(Os) # Start the installer (For now it is non-graphical mode)
            print_log("Starting from non-graphical mode")

        elif isBootloader:
            Boot_loader(Os) # Starts the boot loader
            print_log("Starting from bootloader")

        elif isLogin:
            Login(Os) # Start the login
            print_log("Starting from Login") # Not used

        elif isDesktop:
            Desktop(Os) # Start the desktop
            print_log("Starting from desktop")

        elif isBoot:
            start_boot() # Start the general boot
            print_log("Starting from normal boot")

        # In case the boot order fails, stop the program and write the following:
        else:
            print_error("Invalid or not found boot order, STOPPING...")

            # Stop the program destroying the window
            Os.destroy()

    boot_check() # Execute the boot order

    Os.mainloop() # Tkinter main loop


# Get the parameters
parameters = sys.argv

# If there are no parameters, return
if len(parameters) == 1:
    main()

# If there is a parameter, check if it is a valid one:
elif len(parameters) == 2:
    if parameters[1] == "--help":
        print_info("Help:")
        print_info("\t--help: Prints this message")
        print_info("\t--test: Runs the test")
        print_info("\t--dlogs: Delete logs")
        print_info("\t--krnl int: Start the system with a specific value")
        print_info("")
        print_info("The program will start if no parameter is given.")

    elif parameters[1] == "--test":
        print_info("Running test...")
        routines()
        print_info("Test finished.")

    elif parameters[1] == "--dlogs":
        delete_logs()

elif len(parameters) == 3:
    if parameters[1] == "--boot":

        set_boot(parameters[2])

# -------------------------------------------[ End ]------------------------------------------- #
