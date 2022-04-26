"""
    Module Name:
        Kernel.py

    Abstract:
        This module implements the debug fuctions and boot utilities.

    Author:
        TheBigEye 2-apr-2022
"""

import json
import sys
from tkinter import BOTH, Label, Misc

from System.Utils.Logger import Logger
from System.Utils.Vars import Disk_directory

# TODO: implement a bootloader class for able restart the system

Bugcheck_data_directory = (Disk_directory + "/System/Bugcheck/Bugcheck.json")


class bug_check:

    """
    Show the BSOD, RSOD, GSOD or a custom SOD.
    """

    def __init__(self, master: Misc, error_id: str, msg_color: str, bg_color: str):

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

        Logger.fail("RSOD! The system has failed with code {}", error_id)

        # Load the bugcheck data from the json file.
        with open(Bugcheck_data_directory, 'r') as f:
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

                self.shutdown_time -= 1

                if self.shutdown_time > -1:
                    self.countdown.after(1000, start)
                else:
                    self.master.destroy()
                    sys.exit()

            update()

        start()
