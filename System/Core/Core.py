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
from System.Core.FileSystem import FS_routines
from System.Core.Kernel import bug_check
from System.Core.TaskSystem import ts_routines
from System.Utils.Vars import Assets_directory

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
match Boot_phase:
    case 0: isBSOD = True
    case 1: isRSOD = True
    case 2: isGSOD = True
    case 3: isBIOS = True
    case 4: isINSTALLER = True
    case 5: isBootloader = True
    case 6: isLogin = True
    case 7: isDesktop = True
    case 8: isBoot = True
    case _:
        Logger.error("Invalid value, must be 0-8, STOPING..")
        sys.exit()


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

    # Load the process system (deprecated for now)
    ts_routines()

    # Load the file system
    FS_routines()


def set_boot(value):

    """ This function is used to set the kernel level (boot order). """

    from Libs.pyLogger.Logger import Logger

    str_value = str(value)
    int_value = int(value)

    match int_value:
        case 0: Logger.info("{} | Kernel level set to: Black screen of death", str_value)
        case 1: Logger.info("{} | set to: Red screen of death", str_value)
        case 2: Logger.info("{} | Kernel level set to: Green screen of death", str_value)
        case 3: Logger.info("{} | Kernel level set to: BIOS", str_value)
        case 4: Logger.info("{} | Kernel level set to: Installer", str_value)
        case 5: Logger.info("{} | Kernel level set to: Bootloader", str_value)
        case 6: Logger.info("{} | Kernel level set to: Login", str_value)
        case 7: Logger.info("{} | Kernel level set to: Desktop", str_value)
        case 8: Logger.info("{} | Kernel level set to: Boot", str_value)
        case _:
            Logger.error("Invalid value, must be 0-8, STOPING..")
            sys.exit()

    JSON.set(BOOT_DATA_FILE, "Boot_phase", int_value)


class boot:
    """
    Start a boot process.

    Arguments:
        `master : [Misc]` The parent widget or window.
        `screen : [Misc]` The screen to be displayed.
        `time : [int]` The time to wait before to display the screen.

    Example:
        >>> boot(root, Desktop, 5000) # Wait 5 seconds before to display the Desktop screen.
    """

    def __init__(self, master: Misc, screen: Misc, time: int):

        from System.Shell.Boot.Bootloader import Bootloader

        self.master = master
        self.screen = screen

        Bootloader(self.master, time)

        self.master.after(time  + 1000, screen, self.master)



def boot_check(master):
    """
    This function is used to check if the boot process is complete.
    """

    from System.Shell.Boot.BIOS import BIOS
    from System.Shell.Boot.Desktop.Desktop import Desktop
    from System.Shell.Boot.Installer import Os_Installer
    from System.Shell.Boot.Login import Login

    # Here the variables of the boot order are checked and the corresponding function is executed:
    if isBSOD:
        bug_check(master, "0xDEADDEAD" , "#ffffff", "#000000")

    elif isRSOD:
        bug_check(master, "0xDEADDEAD" , "#ffffff", "#ba0000")

    elif isGSOD:
        bug_check(master, "0xDEADDEAD" , "#ffffff", "#00ba00")

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
