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
import os
from tkinter import Misc

from System.Core.FileSystem import fs_routines
from System.Core.Kernel import bug_check
from System.Core.TaskSystem import ts_routines

from System.UI.Boot.BIOS import BIOS
from System.UI.Boot.Desktop import Desktop
from System.UI.Boot.Installer import Os_Installer
from System.UI.Boot.Login import Login

from System.Utils.Utils import json_get, json_set, Logger
from System.Utils.Vars import Disk_directory

# Load the boot value from boot.json
Kernel_lvl = json_get(Disk_directory, "Boot.json", "Boot")

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
match Kernel_lvl:
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
        Logger.fail("Invalid value, must be 0-8, STOPING..")
        sys.exit()


def check_os():

    """
    This function is used to check if the system is running on Linux, Windows or Mac.
    """

    global in_linux, in_windows, in_mac

    if platform.system() == "Linux": in_linux = True
    elif platform.system() == "Windows": in_windows = True
    elif platform.system() == "Darwin": in_mac = True


def routines():

    """
    Used to execute the first tasks in the first seconds of system startup.
    """

    check_os()

    Logger.log("----------- Starting system execution -----------")
    Logger.log("System started at: {}", datetime.datetime.now())

    # In what os is running the system?
    if in_linux: Logger.log("Running on Linux")
    elif in_windows: Logger.log("Running on Windows")
    elif in_mac: Logger.log("Running on Mac")
    else:
        Logger.warning("Unknown OS, starting anyway...")

    # Load the process system (deprecated for now)
    ts_routines()

    # Load the file system
    fs_routines()


def delete_logs():

    """
    This function is used to delete the logs.
    """

    # Get the relative path of the Logs folder
    logs_path = os.path.join(os.getcwd(), "Logs")

    # Get the list of files inside the Logs folder
    logs_files = os.listdir(logs_path)

    # Delete the files inside the Logs folder
    for file in logs_files:
        os.remove(os.path.join(logs_path, file))
        print("Deleted log: " + os.path.join(logs_path, file))


def set_boot(value):

    """
    This function is used to set the kernel level (boot order).
    """

    from System.Utils.Utils import print_info

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
            Logger.fail("Invalid value, must be 0-8, STOPING..")
            sys.exit()

    json_set(Disk_directory, "Boot.json", "Boot", int_value)


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

        from System.UI.Boot.Bootloader import Boot_loader

        self.master = master
        self.screen = screen

        Boot_loader(self.master, time)

        self.master.after(time  + 1000, screen, self.master)


def boot_check(master):
    """
    This function is used to check if the boot process is complete.
    """

    # Here the variables of the boot order are checked and the corresponding function is executed:
    if isBSOD:
        bug_check(master, "0xDEADDEAD" , "#ffffff", "#000000")

    elif isRSOD:
        bug_check(master, "0xDEADDEAD" , "#ffffff", "#ba0000")

    elif isGSOD:
        bug_check(master, "0xDEADDEAD" , "#ffffff", "#00ba00")

    elif isBIOS:
        boot(master, BIOS, 0)
        Logger.log("Starting from BIOS/UEFI")

    elif isINSTALLER:
        boot(master, Os_Installer, 5000) # Start the installer
        Logger.log("Starting from non-graphical mode")

    elif isBootloader:
        boot(master, Desktop, 60000) # Starts the boot loader
        Logger.log("Starting from bootloader")

    elif isLogin:
        boot(master, Login, 0) # Start the login
        Logger.log("Starting from Login") # Not used

    elif isDesktop:
        boot(master, Desktop, 0) # Start the desktop
        Logger.log("Starting from desktop")

    elif isBoot:
        boot(master, Desktop, 10000) # Start the general boot
        Logger.log("Starting from normal boot")

    # In case the boot order fails, stop the program and write the following:
    else:
        Logger.fail("Invalid or not found boot order, STOPPING...")
        sys.exit()
