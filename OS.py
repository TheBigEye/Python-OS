import tkinter as tk
from System.Core.Core import (
    Is_Boot,
    Is_FAIL,
    Is_in_BIOS,
    Is_in_Boot,
    Is_in_Desktop,
    Is_in_INSTALLER,
    Is_in_Login,
    Load_FileSystem,
    routines,
)

from System.Utils.Colormap import Black
from System.GUI.Boot.BIOS import BIOS
from System.GUI.Boot.Bootloader import Boot_loader
from System.GUI.Boot.Desktop import Desktop
from System.GUI.Boot.Installer import Os_Installer
from System.GUI.Boot.Login import Login
from System.GUI.Boot.RSOD import RSOD
from System.Utils.Utils import print_error, print_log, print_warning

# -----------------------------------------------------------------[ Main ]----------------------------------------------------------------------- #


Os = tk.Tk()  # Make the main window
Os.title("PythonOS")  # Window title
Os.iconbitmap("Assets/Images/icon.ico")  # Window icon

Os.geometry("1024x600")  # Window resolution
Os.resizable(0, 0)  # Not is resizable
Os.configure(background=Black)  # Black is the color base


#  Warnings.
def warnings():

    if Os.winfo_screenwidth() < 1024 and Os.winfo_screenheight() < 600:

        print_warning("The resolution of the screen is lower than that of the window.")


warnings()
routines()
Load_FileSystem()

# -----------------------------------------------------------------[ Boot ]-------------------------------------------------------------------------- #


def start_boot():

    # Start the Bootloader animation
    Boot_loader(Os)

    # Go to the desktop
    Os.after(12000, Desktop, Os)


# Boot order in sections
if Is_FAIL == True:
    RSOD(Os)
    print_error("The system has failed.")

    # Stop the program after 8 secs.
    Os.after(8000, Os.destroy)

elif Is_in_BIOS == True:
    BIOS(Os)
    print_log("Starting from BIOS/UEFI")

elif Is_in_INSTALLER == True:
    Os_Installer(Os)
    print_log("Starting from installer screen")

elif Is_in_Boot == True:
    Boot_loader(Os)
    print_log("Starting from bootloader")

elif Is_in_Login == True:
    Login(Os)
    print_log("Starting from the lLogin screen")

elif Is_in_Desktop == True:
    Desktop(Os)
    print_log("Starting from desktop")

elif Is_Boot == True:
    start_boot()
    print_log("Starting from the normal boot")

else:
    print_error("Boot order not found or not assigned, STOPING...")

    # Stop the program
    Os.destroy()

Os.mainloop()

# ------------------------------------------------------------------[ End ]-------------------------------------------------------------------------- #
