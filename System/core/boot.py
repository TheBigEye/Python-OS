"""
    Module Name:
        Core.py

    Abstract:
        This module implements the boot process of the OS and...
        the routines that are executed in the first seconds of system startup.

    Author:
        TheBigEye 29-oct-2021
"""

import datetime
import platform
import sys
from tkinter import Misc

from Libs.pyLogger.Logger import Logger
from Libs.pyUtils.pyData import JSON

from System.core.filesystem import FS_routines
from System.core.kernel import KRNL_Bug_check
from System.utils.vars import Assets_directory

BOOT_DATA_FILE = (Assets_directory + "/Data/System data/Boot/Boot.json")

# Load the boot value from boot.json
Boot_phase = JSON.get(BOOT_DATA_FILE, "Boot_phase")

# Each screen has an ID
isBSOD = False        # Black screen of death 0
isRSOD = False        # Red screen of death 1
isGSOD = False        # Green screen of death 2

isBIOS = False        # bios screen 3
isINSTALLER = False   # installer screen 4

isBootloader = False  # Boot screen 5
isLogin = False       # Login screen 6
isDesktop = False     # Desktop screen 7
isBoot = False        # Boot the system 8

in_linux = False
in_windows = False
in_mac = False


# Start the boot order
# Start the boot order
if Boot_phase == 0:
    isBSOD = True
elif Boot_phase == 1:
    isRSOD = True
elif Boot_phase == 2:
    isGSOD = True
elif Boot_phase == 3:
    isBIOS = True
elif Boot_phase == 4:
    isINSTALLER = True
elif Boot_phase == 5:
    isBootloader = True
elif Boot_phase == 6:
    isLogin = True
elif Boot_phase == 7:
    isDesktop = True
elif Boot_phase == 8:
    isBoot = True
else:
    raise ValueError("Invalid value, must be 0-8, STOPPING..")

def check_os():

    """ This function is used to check if the system is running on Linux, Windows or Mac. """

    global in_linux, in_windows, in_mac

    if platform.system() == "Linux": in_linux = True
    elif platform.system() == "Windows": in_windows = True
    elif platform.system() == "Darwin": in_mac = True


def routines():
    """ Used to execute the first tasks in the first seconds of system startup """

    check_os()
    Logger.info("System started at: {}", datetime.datetime.now())

    # In what os is running the system?
    if in_linux: Logger.info("Running on Linux")
    elif in_windows: Logger.info("Running on Windows")
    elif in_mac: Logger.info("Running on Mac")
    else:
        Logger.warning("Unknown OS, starting anyway...")

    # Load the file system
    FS_routines()


def set_boot(value: int):
    """
    This function is used to set the kernel level (boot order)

    Arguments:
        `value` : `[int]` - The value to set the boot level to.

    """

    from Libs.pyLogger.Logger import Logger

    str_value = str(value)
    int_value = int(value)

    if int_value == 0:
        Logger.info("{} | Kernel level set to: Black screen of death", str_value)
    elif int_value == 1: 
        Logger.info("{} | set to: Red screen of death", str_value)
    elif int_value == 2: 
        Logger.info("{} | Kernel level set to: Green screen of death", str_value)
    elif int_value == 3: 
        Logger.info("{} | Kernel level set to: BIOS", str_value)
    elif int_value == 4: 
        Logger.info("{} | Kernel level set to: Installer", str_value)
    elif int_value == 5: 
        Logger.info("{} | Kernel level set to: Bootloader", str_value)
    elif int_value == 6: 
        Logger.info("{} | Kernel level set to: Login", str_value)
    elif int_value == 7: 
        Logger.info("{} | Kernel level set to: Desktop", str_value)
    elif int_value == 8: 
        Logger.info("{} | Kernel level set to: Boot", str_value)
    else:
        raise ValueError("Invalid value, must be 0-8, STOPING..")

    JSON.set(BOOT_DATA_FILE, "Boot_phase", int_value)

def set_desktop_mode(value: int):
    """
    It sets the desktop mode

    Arguments:
        `value` : `[int]` The value to set the desktop mode to.

    """

    from Libs.pyLogger.Logger import Logger

    str_value = str(value)
    int_value = int(value)

    if int_value == 0:
        Logger.info("{} | Desktop mode set to: WINDOW MANAGER", str_value)
    elif int_value == 1: 
        Logger.info("{} | Desktop mode set to: DESKTOP ENVIROMENT", str_value)
    else:
        raise ValueError("Invalid value, must be 0-1, STOPING..")
        sys.exit()

    JSON.set(BOOT_DATA_FILE, "Desktop_mode", int_value)

class boot:
    """
    Start a boot process.

    Arguments:
        `master` : `[Misc]` The parent widget or window.
        `screen` : `[Misc]` The screen to be displayed.
        `time` : `[int]` The time to wait before to display the screen.

    Example:
        >>> # Wait 5 seconds before to display the Desktop screen.
        >>> boot(root, Desktop, 5000)
    """

    def __init__(self, master: Misc, screen: Misc, time: int):
        """ Start a boot process. """

        from System.shell.Boot.Bootloader import Bootloader

        self.master = master
        self.screen = screen

        Bootloader(self.master, time)

        self.master.after(time  + 1000, screen, self.master)


def boot_check(master):
    """ Check if the boot process is complete. """

    from System.shell.Boot.BIOS import BIOS
    from System.shell.Boot.Desktop.Desktop import Desktop
    from System.shell.Boot.Installer import Os_Installer
    from System.shell.Boot.Login import Login

    # Here the variables of the boot order are checked and the corresponding function is executed:
    if isBSOD:
        KRNL_Bug_check(master, "0xDEADDEAD" , "#ffffff", "#000000")

    elif isRSOD:
        KRNL_Bug_check(master, "0xDEADDEAD" , "#ffffff", "#ba0000")

    elif isGSOD:
        KRNL_Bug_check(master, "0xDEADDEAD" , "#ffffff", "#00ba00")

    elif isBIOS:
        boot(master, BIOS, 0)
        Logger.info("Starting from BIOS/UEFI")

    elif isINSTALLER:
        boot(master, Os_Installer, 5000) # Start the installer
        Logger.info("Starting from non-graphical mode")

    elif isBootloader:
        boot(master, Desktop, 60000) # Starts the boot loader
        Logger.info("Starting from bootloader")

    elif isLogin:
        boot(master, Login, 0) # Start the login
        Logger.info("Starting from Login") # Not used

    elif isDesktop:
        boot(master, Desktop, 0) # Start the desktop
        Logger.info("Starting from desktop")

    elif isBoot:
        boot(master, Desktop, 10000) # Start the general boot
        Logger.info("Starting from normal boot")

    # In case the boot order fails, stop the program and write the following:
    else:
        Logger.error("Invalid or not found boot order, STOPPING...")
        sys.exit()
