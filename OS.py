import tkinter as tk
from System.Core.Core import Is_Boot, Is_FAIL, Is_in_BIOS, Is_in_Boot, Is_in_Desktop, Is_in_INSTALLER, Is_in_Login, Logger, routines

from System.Utils.Colormap import Black
from System.GUI.Boot.BIOS import BIOS
from System.GUI.Boot.Bootloader import Boot_loader
from System.GUI.Boot.Desktop import Desktop
from System.GUI.Boot.Installer import Os_Installer
from System.GUI.Boot.Login import Login
from System.GUI.Boot.RSOD import RSOD

# -----------------------------------------------------------------[ Main ]----------------------------------------------------------------------- #


Os = tk.Tk()  # Make the main window
Os.title("PythonOS")  # Window title
Os.iconbitmap("Assets/Images/icon.ico")  # Window icon

Os.geometry("1024x600")  # Window resolution
Os.resizable(0, 0)  # Not is resizable
Os.configure(background=Black)  # Black is the color base


#  if the resolution of the screen is lower than that of the window, then it will print a warning on the console.
def warning():

    if Os.winfo_screenwidth() < 1024 and Os.winfo_screenheight() < 600:
        print("Warning: The resolution of the screen is lower than that of the window.\n")
        Logger("Warning: The resolution of the screen is lower than that of the window.")

warning()
routines()

# -----------------------------------------------------------------[ Boot ]-------------------------------------------------------------------------- #

def start_boot():

    # Start the Bootloader animation
    Boot_loader(Os)

    # Go to the desktop
    Os.after(12000, Desktop, Os)



# Boot order in sections
if Is_FAIL == True:

    RSOD(Os)

if Is_in_BIOS == True:

    BIOS(Os)

if Is_in_INSTALLER == True:

    Os_Installer(Os)

if Is_in_Boot == True:

    Boot_loader(Os)

if Is_in_Login == True:

    Login(Os)   

if Is_in_Desktop == True:  

    Desktop(Os)

if Is_Boot == True:

    start_boot()


Os.mainloop()

# ------------------------------------------------------------------[ End ]-------------------------------------------------------------------------- #
