"""
    Module Name:
        Utils.py

    Abstract:
        This module contains uncategorized functions but useful for the project.

    Author:
        TheBigEye 8-jul-2021

"""

import datetime
import os
import urllib.request

from PIL import Image, ImageTk
from System.Utils.Colormap import Color
from Libs.pyLogger.Logger import Logger
from System.Utils.Vars import Assets_directory, Loading, Logs_directory, XCursor_2

# -------------------------------------------[ Time ]------------------------------------------- #

def Get_Current_Time():

    """
    Return the current time in a string.
    """

    return str(datetime.datetime.now())

def Get_Current_Date():

    """
    Return the current date in a string.
    """

    return str(datetime.date.today())

def Get_Current_Date_Time():

    """
    Return the current date and time in a string.
    """

    return str(datetime.datetime.now())


# -------------------------------------------[ Misc ]------------------------------------------- #

def Execute(master, Loading_time: float, Function, *args):

    """
    This function will execute a function with a loading time.
    """

    from System.Core.Core import in_windows

    global Open, Loading_cursor, Normal_cursor

    def Open():
        Function(*args)

    def Loading_cursor():

        if in_windows:
            master.config(cursor=Loading)
        else:
            master.config(cursor="wait")

    def Normal_cursor():

        if in_windows:
            master.config(cursor=XCursor_2)
        else:
            master.config(cursor="")

    master.after(100, Loading_cursor)
    master.after(Loading_time, Open)
    master.after(1000, Normal_cursor)


def Asset_colored(Folder_name, file_name_and_extension, hue_value):

    # First: Search the folder inside from Assets folder and save the path
    for root, dirs, files in os.walk(Assets_directory):
        for folder in dirs:
            if folder == Folder_name:
                folder_path = os.path.join(root, folder)
                break

    # Second: Search the file inside the folder and save the path
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(file_name_and_extension):
                img = Image.open(os.path.join(root, file))
                img = img.convert("RGBA")
                image_data = img.getdata()

                # change image hue value
                newData = []
                for item in image_data:
                    newData.append(tuple(int(item[i] * hue_value) for i in range(3)) + (255,))

                img.putdata(newData)
                return ImageTk.PhotoImage(img)

# Check if the internet is on.
def check_internet():
    try:
        response = urllib.request.urlopen('http://www.google.com', timeout=1)
        if response.code == 200:
            return True
    except:
        Logger.warning("Check your internet connection")
        return False

def Image_getcolor(image, x, y):

    for root, dirs, files in os.walk(Assets_directory):
        for file in files:

            if file.endswith(image):
                img = Image.open(os.path.join(root, file))
                img = img.convert("RGBA")
                image_data = img.getdata()

                color = image_data[y * img.size[0] + x]
                color = "#%02x%02x%02x" % (color[0], color[1], color[2])
                color = color.upper()
                return color

# -------------------------------------------[ End ]------------------------------------------- #
