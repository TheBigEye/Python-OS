import tkinter as tk

from System.Core.Core import (
    Is_Boot,
    Is_FAIL,
    Is_in_BIOS,
    Is_in_Boot,
    Is_in_Desktop,
    Is_in_INSTALLER,
    Is_in_Login,
    routines
)

from System.GUI.Boot.BIOS import BIOS
from System.GUI.Boot.Bootloader import Boot_loader
from System.GUI.Boot.Desktop import Desktop
from System.GUI.Boot.Installer import Os_Installer
from System.GUI.Boot.Login import Login
from System.GUI.Boot.RSOD import RSOD

from System.Utils.Colormap import Black
from System.Utils.Utils import (print_error, print_info, print_log, print_warning)
from System.Utils.Vars import Assets_dir

# -----------------------------------------------------------------[ Main ]----------------------------------------------------------------------- #


Os = tk.Tk()  # Create the window that will be the base of the program
Os.title("Python OS")  # Window title
Os.iconbitmap(Assets_dir + "/Images/icon.ico")  # Window icon

Os.geometry("1024x600")  # Window size
Os.resizable(False, False)  # Window resizing
Os.configure(background = Black)  # Black is the base color


# Warnings.
def warnings():

    # In case the screen resolution is lower than expected in the window, a warning will be displayed
    if ((Os.winfo_screenwidth() < 1024) and (Os.winfo_screenheight() < 600)):

        print_warning("The resolution of the screen is less than that of the window.")


warnings() # Show warnings before execution
routines() # Execute system routines

# -----------------------------------------------------------------[ Boot ]-------------------------------------------------------------------------- #

# This part starts the important functions of the program
def start_boot():

    # Start bootloader animation
    Boot_loader(Os)

    # After 12 seconds (or when everything is loaded), launch the desktop.
    Os.after(12000, Desktop, Os)


# Here the variables of the boot order are checked and the corresponding function is executed:
if (Is_FAIL == True):
    RSOD(Os) # Red screen of death
    print_error("The system has failed.")

    # Stop the program after 8 seconds.
    Os.after(8000, Os.destroy)

elif (Is_in_BIOS == True):
    BIOS(Os) # Start BIOS
    print_log("Starting from BIOS/UEFI")

elif (Is_in_INSTALLER == True):
    Os_Installer(Os) # Start the installer (For now it is non-graphical mode)
    print_log("Starting from non-graphical mode")

elif (Is_in_Boot == True):
    Boot_loader(Os) # Starts the boot loader
    print_log("Starting from bootloader")

elif (Is_in_Login == True):
    Login(Os) # Start the login
    print_log("Starting from Login") # Not used

elif (Is_in_Desktop == True):
    Desktop(Os) # Start the desktop
    print_log("Starting from desktop")

elif (Is_Boot == True):
    start_boot() # Start the general boot
    print_log("Starting from normal boot")

# In case the boot order fails, stop the program and write the following:
else:
    print_error("Invalid or not found boot order, STOPPING...")

    # Stop the program destroying the window
    Os.destroy()

Os.mainloop() # Tkinter main loop

# ------------------------------------------------------------------[ End ]-------------------------------------------------------------------------- #
