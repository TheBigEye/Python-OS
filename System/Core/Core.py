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

from System.Core.FileSystem import fs_routines
from System.Core.TaskSystem import ts_routines
from System.Utils.Utils import (json_get, json_set, print_error, print_log, print_warning)

# Load the boot value from boot.json
Kernel_lvl = json_get("Boot.json", "Boot")

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
        print_error("Invalid Kernel_lvl value, must be 0-8, STOPPING...")
        sys.exit()


# Check base system (is running on linux, windows or mac)
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

    print_log("----------- Starting system execution -----------")
    print_log("Started log at: " + str(datetime.datetime.now()))

    # In what os is running the system?
    if in_linux: print_log("Running on Linux")
    elif in_windows: print_log("Running on Windows")
    elif in_mac: print_log("Running on Mac")
    else:
        print_warning("Unknown OS, starting anyway...")

    # Load the process system
    ts_routines()

    # Load the file system
    fs_routines()


def delete_logs():

    """
    This function is used to delete the logs.
    """

    # Delete the files inside the Logs folder using the os module
    import os

    from System.Utils.Utils import print_info

    # Get the relative path of the Logs folder
    logs_path = os.path.join(os.getcwd(), "Logs")

    # Get the list of files inside the Logs folder
    logs_files = os.listdir(logs_path)

    # Print an information message
    print_info("Deleting files from the Logs folder")

    # Delete the files inside the Logs folder
    for file in logs_files:
        os.remove(os.path.join(logs_path, file))
        print("Deleted log: " + os.path.join(logs_path, file))


def set_boot(value):

    """
    This function is used to set the kernel level.
    """

    from System.Utils.Utils import print_info

    json_set("Boot.json", "Boot", int(value))
    print_info("Boot set to: " + str(value))
