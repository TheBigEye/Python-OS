"""

    Module name:
        Vars.py

    Abstract:
        This module implements the variables that are used in the program.

    Author:

        TheBigEye 29-oct-2021

"""

import os
import platform
from Libs.pyLogger.Logger import Logger

# Relative paths (used to be able to execute the program from anywhere)
Assets_directory = os.path.join(os.getcwd(), "Assets")
Assets_directory = Assets_directory.replace("\\", "/")

Disk_directory = os.path.join(os.getcwd(), "Disk")
Disk_directory = Disk_directory.replace("\\", "/")

Logs_directory = os.path.join(os.getcwd(), "Logs")
Logs_directory = Logs_directory.replace("\\", "/")

# Cursors
if platform.system() == "Windows":

    Cursor = "@" + "Assets/Cursors/Windows/Cursor.cur"
    XCursor = "@" + "Assets/Cursors/Windows/XCursor.cur"
    XCursor_2 = "@" + "Assets/Cursors/Windows/XCursor-2.cur"
    Hand= "@" + "Assets/Cursors/Windows/Hand.cur"
    Hand_2 = "@" + "Assets/Cursors/Windows/Hand-2.cur"
    Loading= "@" + "Assets/Cursors/Windows/Loading.cur"

# FIX FIX: Custom cursors for linux doesnt works well
elif platform.system() == "Linux":

    # if have xorg server
    #if os.path.exists("/etc/X11"):
    #    Cursor = "@" + "Assets/Cursors/Linux/Cursor.xbm"
    #    XCursor = "@" + "Assets/Cursors/Linux/XCursor.xbm"
    #    XCursor_2 = "@" + "Assets/Cursors/Linux/XCursor-2.xbm"
    #    Hand= "@" + "Assets/Cursors/Linux/Hand.xbm"
    #    Hand_2 = "@" + "Assets/Cursors/Linux/Hand-2.xbm"
    #    Loading= "@" + "Assets/Cursors/Linux/Loading.xbm"

    #else:

        # if don't have xorg server
        #Logger.error("Error while loading cursors. Please install xorg server.")

    # set the fallback cursors
    Cursor = "arrow"
    XCursor = "arrow"
    XCursor_2 = "arrow"
    Hand= "arrow"
    Hand_2 = "arrow"
    Loading= "arrow"
