"""
    Module Name:
        Kernel.py

    Abstract:
        This module implements the debug fuctions and boot utilities.

    Author:
        TheBigEye 2-apr-2022
"""

import json
import os
import re
import subprocess
import sys
from tkinter import BOTH, Label, Misc

from Libs.pyLogger.Logger import Logger
from System.utils.vars import Assets_directory

BUGCHECK_DATA_FILE = (Assets_directory + "/Data/System data/Kernel/Bugcheck.json")

# Checkers ---------------------------------------------------------------------------------------------------------------------

def screen_check(master: Misc) -> None:
    """ This function checks if the system is running in a supported resolution. """

    # get the window resolution from the master
    window_height = master.winfo_height()
    window_width = master.winfo_width()

    # get the system resolution
    system_height = master.winfo_screenheight()
    system_width = master.winfo_screenwidth()

    # check if the window resolution is greater than the system resolution, if so, then print a warning message
    if window_height > system_height or window_width > system_width:
        Logger.warning("The window resolution is greater than the system resolution.")
        Logger.warning("The window resolution is: " + str(window_height) + "x" + str(window_width))
        Logger.warning("The system resolution is: " + str(system_height) + "x" + str(system_width))

def python_modules_check():
    """ This function checks if the current python have the needed moduels. """

    def module_not_found(module_name: str):
        """ This function prints a warning message if the module is not found. """

        Logger.warning("Oh no!, The module " + module_name + " not found, is required for the system to work.")

    # check if tkinter, tkinterweb, psutils and pyllow are installed, if not, print a warning message, if all the modules are found, then print a success message
    if not sys.modules.get("tkinter"): module_not_found("tkinter") # Jajaj, its impossible... but just in case..
    elif not sys.modules.get("psutil"): module_not_found("psutil")
    elif not sys.modules.get("pyllow"):  module_not_found("pyllow")
    else:
        Logger.info("All the needed modules are installed.")

# Getters ----------------------------------------------------------------------------------------------------------------------

def get_desktop_enviroment() -> str:
    """ Get the desktop enviroment. """
    if sys.platform in ["win32", "cygwin"]:
        return "windows"
    elif sys.platform == "darwin":
        return "mac"
    else: # Most likely either a POSIX system or something not much common
        desktop_session = os.environ.get("DESKTOP_SESSION")
        if desktop_session is not None: # easier to match if we doesn't have  to deal with caracter cases
            desktop_session = desktop_session.lower()
            if desktop_session in ["gnome","unity", "cinnamon", "mate", "xfce4", "lxde", "fluxbox", "blackbox", "openbox", "icewm", "jwm", "afterstep", "trinity", "kde"]:
                return desktop_session

            ## Special cases ##
            # Canonical sets $DESKTOP_SESSION to Lubuntu rather than LXDE if using LXDE.
            # There is no guarantee that they will not do the same with the other desktop environments.
            elif "xfce" in desktop_session or desktop_session.startswith("xubuntu"): return "xfce4"
            elif desktop_session.startswith("ubuntu"): return "unity"
            elif desktop_session.startswith("lubuntu"): return "lxde"
            elif desktop_session.startswith("kubuntu"): return "kde"
            elif desktop_session.startswith("razor"): return "razor-qt" # e.g. razorkwin
            elif desktop_session.startswith("wmaker"): return "windowmaker" # e.g. wmaker-common

        if os.environ.get('KDE_FULL_SESSION') == 'true':
            return "kde"
        elif os.environ.get('GNOME_DESKTOP_SESSION_ID'):
            if "deprecated" not in os.environ.get('GNOME_DESKTOP_SESSION_ID'):
                return "gnome2"
        #From http://ubuntuforums.org/showthread.php?t=652320
        elif is_running("xfce-mcs-manage"):
            return "xfce4"
        elif is_running("ksmserver"):
            return "kde"

    Logger.warning("Could not detect the desktop environment.")
    return "unknown"

def is_running(process: str) -> bool:
    """
    This function checks if the given process is running

    Arguments:
        `process`: `[str]` The process to check if it is running.

    Returns:
        `True` if the process is running, `False` otherwise.

    Example:
        >>> is_running("python")
        >>> True
    """

    try: #Linux/Unix
        s = subprocess.Popen(["ps", "axw"],stdout=subprocess.PIPE)
    except: #Windows
        s = subprocess.Popen(["tasklist", "/v"],stdout=subprocess.PIPE)
    for x in s.stdout:
        if re.search(process, x):
            return True

    Logger.warning("The process " + process + " is not running.")
    return False

def KRNL_get_os() -> str:
    """ This function return the OS name. """
    return str(os.name)


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class KRNL_Bug_check:
    """
    Show the BSOD, RSOD, GSOD or a custom SOD.

    Arguments:
        `master` : `[Misc]` The parent widget for place the BSOD.
        `error_id` : `[str]` The error id, like a memory dump 0x12345678.
        `msg_color` : `[str]` The hex color of the message.
        `bg_color` : `[str]` The hex color of the background.

    Returns:
        `None`

    Example:
        >>> KRNL_Bug_check(master, "0x12345678", "FFFFFF", "000000")
    """

    def __init__(self, master: Misc, error_id: str, msg_color: str, bg_color: str) -> None:

        """ Initialize the bug checker. """

        self.master = master
        self.error_id = error_id
        self.msg_color = msg_color

        # Creates the second color a little darker
        self.msg_color_2 = "#%02x%02x%02x" % (

            # the las value is the intensity
            min(255, int(msg_color[1:3], 16) - 24), # Red
            min(255, int(msg_color[3:5], 16) - 24), # Green
            min(255, int(msg_color[5:7], 16) - 24)  # Blue
        )
        self.bg_color = bg_color

        self.master.configure(background=self.bg_color)

        self.base = Label(self.master, bg=self.bg_color)
        self.base.pack(fill=BOTH, expand=True)

        Logger.error("BSOD! The system has failed with code {}", error_id)

        # Load the bugcheck data from the json file.
        with open(BUGCHECK_DATA_FILE, 'r') as f:
            data = json.load(f)

            self.emote = data["Emote"]
            self.message = data["Messagge"]
            self.comment = data["Comment"]
            self.shutdown_time = data["Shutdown_time"]

            # If the shurdow time not is int, convert it to int
            if not isinstance(self.shutdown_time, int):
                self.shutdown_time = int(self.shutdown_time)

            for key, value in data["Codes"].items():
                if key == self.error_id:
                    self.error_code = value["name"]
                    self.error_info = value["description"]

        def start():
            """ Start the BSoD. """

            # remove all the widgets from self.base
            for widget in self.base.winfo_children():
                widget.destroy()

            # The emote
            self.emote_label = Label(
                self.base,
                text = self.emote,
                font = ("Segoe UI", 69),
                bg =self.bg_color,
                fg=self.msg_color
            )
            self.emote_label.place(x = 32, y = 48)

            # The message which will be displayed
            self.message_label = Label(
                self.base,
                text = self.message,
                font = ("Segoe UI", 16),
                bg =self.bg_color,
                fg=self.msg_color_2
            )
            self.message_label.place(x = 32, y = 195)

            # The quick binds for shutdown
            self.tip = Label(
                self.base,
                text = "Press Ctrl+Alt+Del to shutdown immediately",
                font = ("Segoe UI", 10),
                bg =self.bg_color,
                fg=self.msg_color_2
            )
            self.base.bind("<Control-Alt-Delete>", lambda event: sys.exit())
            self.tip.place(x = 32, y = 278)

            # The countdown, the time to shutdown, when it reaches 0, the program will quit
            self.countdown = Label(
                self.base,
                text = "Shutting down in: " + str(self.shutdown_time) + " seconds",
                font = ("Segoe UI", 13),
                bg =self.bg_color,
                fg=self.msg_color_2
            )
            self.countdown.place(x = 32, y = 255)

            self.id = Label(self.base, text = "Error ID: " + self.error_id, font = ("Segoe UI", 11), bg =self.bg_color, fg=self.msg_color_2)
            self.brief_info = Label(self.base, text = "Brief info: " + self.error_info, font = ("Segoe UI", 12), bg =self.bg_color, fg=self.msg_color_2)

            # The error code, like 0x00000001 (memmory bytes)
            self.stop_code = Label(
                self.base,
                text = "Stop Code: " + self.error_code,
                font = ("Segoe UI", 12),
                bg =self.bg_color,
                fg=self.msg_color_2
            )
            self.stop_code.place(x = 32, y = 330)

            self.comment_label = Label(self.base, text = self.comment, font = ("Segoe UI", 11), bg =self.bg_color, fg=self.msg_color_2)

            self.brief_info.place(x = 32, y = 350)
            self.id.place(x = 32, y = 370)
            self.comment_label.place(x = 32, y = 425)

            def update():
                """ Update the countdown and refresh the display. """

                self.shutdown_time -= 1

                if self.shutdown_time > -1:
                    for widgets in self.base.winfo_children():
                        widgets.update_idletasks()
                    self.countdown.after(1000, start)
                else:
                    for widget in self.master.winfo_children():
                        widget.destroy()

                    master.after(2000, sys.exit)

            update()

        start()
