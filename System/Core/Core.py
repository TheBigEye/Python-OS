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
from tkinter import BOTH, Frame, Label, Misc

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


class bug_check(Frame):

    """
    This class is used to show the BSOD, RSOD, GSOD or a custom SOD screen.
    """

    def __init__(self, master: Misc, msg_string: str, error_id: str, msg_color: str, msg_color_2 :str, bg_color: str, shutdown_time: int):
        super().__init__(master)

        self.master = master
        self.msg_string = msg_string
        self.error_id = error_id
        self.msg_color = msg_color
        self.msg_color_2 = msg_color_2
        self.bg_color = bg_color
        self.shutdown_time = shutdown_time

        self.master.configure(background=self.bg_color)

        self.base = Label(self.master, bg=self.bg_color)
        self.base.pack(fill=BOTH, expand=True)

        def shutdown():

            self.emote = Label(self.base, text = "Ouch.", font = ("Segoe UI", 70), bg =self.bg_color, fg=self.msg_color)
            self.emote.place(x = 32, y = 48)

            self.msg = Label(self.base, text = self.msg_string, font = ("Segoe UI", 17), bg =self.bg_color, fg=self.msg_color_2)
            self.msg.place(x = 32, y = 200)

            match self.error_id:
                case "0x00000000":
                    self.error_code = "NO_ERROR"
                    self.error_info = "No error has occurred."
                case "0x00000001":
                    self.error_code = "APC_INDEX_MISMATCH"
                    self.error_info = "An APC was delivered with an invalid index value."
                case "0x00000002":
                    self.error_code = "DEVICE_QUEUE_NOT_BUSY"
                    self.error_info = "An attempt was made to execute a device driver without first calling DeviceQueueStart."
                case "0x00000003":
                    self.error_code = "INVALID_AFFINITY_SET"
                    self.error_info = "An attempt was made to execute a thread on an invalid processor."
                case "0x00000004":
                    self.error_code = "INVALID_DATA_ACCESS_TRAP"
                    self.error_info = "An attempt was made to access memory using an invalid address."
                case "0x00000005":
                    self.error_code = "INVALID_PROCESS_ATTACH_ATTEMPT"
                    self.error_info = "An attempt was made to attach to a process that is not part of the system."
                case "0x00000006":
                    self.error_code = "INVALID_PROCESS_DETACH_ATTEMPT"
                    self.error_info = "An attempt was made to detach from a process that is not part of the system."
                case "0x00000007":
                    self.error_code = "INVALID_SOFTWARE_INTERRUPT"
                    self.error_info = "An attempt was made to execute a software interrupt that is not part of the system."
                case "0x00000008":
                    self.error_code = "IRQL_NOT_DISPATCH_LEVEL"
                    self.error_info = "An attempt was made to execute a thread at an invalid IRQL level."
                case "0x00000009":
                    self.error_code = "IRQL_NOT_GREATER_OR_EQUAL"
                    self.error_info = "An attempt was made to execute a thread at an IRQL lower than APC_LEVEL."
                case "0x0000000A":
                    self.error_code = "IRQL_NOT_LESS_OR_EQUAL"
                    self.error_info = "An attempt was made to execute a thread at an IRQL higher than DISPATCH_LEVEL."
                case "0x0000000B":
                    self.error_code = "NO_EXCEPTION_HANDLING_SUPPORT"
                    self.error_info = "An attempt was made to execute a thread that does not have an exception handler."
                case "0xDEADDEAD":
                    self.error_code = "MANUALLY_INITIATED_CRASH"
                    self.error_info = "A crash was manually initiated by the User."


            self.code = Label(self.base, text = "Stop code: " + self.error_code, font = ("Segoe UI", 12), bg =self.bg_color, fg=self.msg_color_2)
            self.code.place(x = 32, y = 338)

            self.einfo = Label(self.base, text = "Brief info: " + self.error_info, font = ("Segoe UI", 12), bg =self.bg_color, fg=self.msg_color_2)
            self.einfo.place(x = 32, y = 360)

            self.id = Label(self.base, text = "Error ID: " + self.error_id, font = ("Segoe UI", 12), bg =self.bg_color, fg=self.msg_color_2)
            self.id.place(x = 32, y = 380)

            self.warning = Label(self.base, text = "This is a bug, please report it to the developers.", font = ("Segoe UI", 12), bg =self.bg_color, fg=self.msg_color_2)
            self.warning.place(x = 32, y = 430)

            self.countdown = Label(self.base, text = "Shutting down in " + str(self.shutdown_time) + " seconds.", font = ("Segoe UI", 14), bg =self.bg_color, fg=self.msg_color_2)
            self.countdown.place(x = 32, y = 260)

            self.tip = Label(self.base, text = "Press Ctrl+Alt+Del to shutdown.", font = ("Segoe UI", 8), bg =self.bg_color, fg=self.msg_color_2)
            self.tip.place(x = 32, y = 285)


            self.shutdown_time -= 1

            if self.shutdown_time > -1:
                self.countdown.after(1000, shutdown)
            else:
                self.master.destroy()
                sys.exit()

        shutdown()
