"""
    Module Name:
        Utils.py

    Abstract:
        This module contains uncategorized functions but useful for the project.

    Author:
        TheBigEye 8-jul-2021

"""

import datetime
import json
import os
import urllib.request
from tkinter import PhotoImage

from PIL import Image, ImageTk
from System.Utils.Colormap import color_hex_rgb, color_str_rgb
from System.Utils.Logger import Logger
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


def Asset(Folder_name: str, File_name_and_extension: str):

    """ Return the image file from the file name of a folder within the Assets folder

    Arguments:
        `Folder_name : [str]` The name of the folder where the image is.
        `File_name_and_extension : [str]` The name (and extension) of the image file.

    Returns:
        `PhotoImage : [PhotoImage object]` The image file.

    Example:
        >>> an_image = Asset("Icons", "Icon.png")

    """

    # First: Search the folder inside from Assets folder and save the path
    for root, dirs, files in os.walk(Assets_directory):
        for folder in dirs:
            if folder == Folder_name:
                folder_path = os.path.join(root, folder)
                break

    # Second: Search the file inside the folder and save the path
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(File_name_and_extension):
                return PhotoImage(file = os.path.join(root, file))

    Logger.warning("The file {} does not exist in the folder {}", File_name_and_extension, Folder_name)


# My masterpiece!!
def Asset_color(Folder_name: str ,File_name_and_extension: str, Size: str, From_color: str, To_color: str):

    """ Return a image file from a folder within the Assets folder

    Arguments:
        `Folder_name : [str]` The name of the folder where the image is.
        `File_name_and_extension : [str]` The name (and extension) of the image file.
        `Size : [str]` The new size of the image, if you not want to change the size, just put `"null"`.
        `From_color : [str]` The color A of the image (is the color which will be replaced).
        `To_color : [str]` The color B of the image (replace ).

    Returns:
        `PhotoImage : [PhotoImage object]` The image file with the changes.

    Example:
        >>> # This example will return the image from Images folder with a new size and background color
        >>> an_image = Asset_color("Images", "Image.png", "100x100", "#FF00FF", "#F0CF00")
    """

    # Search the folder inside from Assets folder (also subdirectories)
    for root, dirs, files in os.walk(Assets_directory):
        for folder in dirs:
            if folder == Folder_name:
                folder_path = os.path.join(root, folder)
                break

    # and earch the file inside the folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(File_name_and_extension):
                img = Image.open(os.path.join(root, file))
                img = img.convert("RGBA")
                image_data = img.getdata()

                # change image color
                img.putdata(replace_color(image_data, From_color, To_color))

                # resize image
                if Size != "null":
                    Size = Size.split("x")
                    img = img.resize((int(Size[0]), int(Size[1])), Image.ANTIALIAS)

                # return new image
                return ImageTk.PhotoImage(img)

    Logger.warning("The file {} does not exist in the folder {}", File_name_and_extension, Folder_name)


def replace_color(image_data, From_color: str, To_color: str):

    """ Return a image file from a folder within the Assets folder

    Arguments:
        `image_data : [list]` The image data.
        `From_color : [str]` The color A of the image (is the color which will be replaced).
        `To_color : [str]` The color B of the image (replace ).

    Returns:
        `PhotoImage : [PhotoImage object]` The image file with the changes.

    Example:
        >>> # This example will return the new image data with the colors changes
        >>> image_data = replace_color(image_data, "#FF00FF", "#F0CF00")
    """

    # detect if from_color is in hex or string
    if From_color[0] == "#":
        From_color = color_hex_rgb(From_color)
    else:
        From_color = color_str_rgb(From_color)

    # detect if to_color is in hex or string
    if To_color[0] == "#":
        To_color = color_hex_rgb(To_color)
    else:
        # convert string color rgb
        To_color = color_str_rgb(To_color)

    # replace colors
    newData = []
    for item in image_data:
        if item[0] == From_color[0] and item[1] == From_color[1] and item[2] == From_color[2]:
            newData.append(To_color + (255,))
        else:
            newData.append(item)

    return newData

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
def internet_on():
    try:
        response = urllib.request.urlopen('http://www.google.com', timeout=1)
        if response.code == 200:
            return True
    except:
        return False


def json_get(Folder: str, json_file: str, key: str):
    """
    Return the value of a key from a json file.

    Arguments:
        `Folder : [str]` The name of the folder where the json file is.
        `json_file : [str]` The name (and extension) of the json file.
        `key : [str]` The key of the value you want to get.

    Returns:
        `value : [str]` The value of the key.

    Example:
        >>> value = json_get("Settings", "Settings.json", "key")
        >>> print(value)

    """

    for root, dirs, files in os.walk(Folder):
        for file in files:

            if file.endswith(json_file):
                with open(os.path.join(root, file), 'r') as f:
                    data = json.load(f)
                    return data[key]


def json_set(Folder, json_file, key, value):
    """
    Set the value of a key from a json file.

    Arguments:
        `Folder : [str]` The name of the folder where the json file is.
        `json_file : [str]` The name (and extension) of the json file.
        `key : [str]` The key of the value you want to set.
        `value : [str]` The value of the key.

    Example:
        >>> json_set("Settings", "Settings.json", "key", "value")
    """

    for root, dirs, files in os.walk(Folder):
        for file in files:

            if file.endswith(json_file):
                with open(os.path.join(root, file), 'r') as f:
                    data = json.load(f)
                    data[key] = value
                    with open(os.path.join(root, file), 'w') as f:
                        json.dump(data, f, indent=4)


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


def data_set(Folder_name, json_file, key, value):

    for root, dirs, files in os.walk(Assets_directory + "/Data"):
        for folder in dirs:
            if folder == Folder_name:
                folder_path = os.path.join(root, folder)
                break

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(json_file):
                with open(os.path.join(root, file), 'r') as f:
                    data = json.load(f)
                    data[key] = value
                    with open(os.path.join(root, file), 'w') as f:
                        json.dump(data, f, indent=4)


def data_get(Folder_name, json_file, key):

    for root, dirs, files in os.walk(Assets_directory + "/Data"):
        for folder in dirs:
            if folder == Folder_name:
                folder_path = os.path.join(root, folder)
                break

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(json_file):
                with open(os.path.join(root, file), 'r') as f:
                    data = json.load(f)
                    return data[key]

# -------------------------------------------[ End ]------------------------------------------- #
