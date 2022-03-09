import datetime
import inspect
import json
import os
import urllib.request
from tkinter import PhotoImage

from PIL import Image, ImageTk
from System.Utils.Colormap import color_hex_rgb, color_str_rgb
from System.Utils.Vars import Assets_directory, Disk_directory, Loading, XCursor_2

# -------------------------------------------[ Logger ]------------------------------------------- #

def Logger(Log_Message):

    # Make the logs folder.
    if not os.path.exists("Logs"):
        os.makedirs("Logs")

    # Get the current date.
    current_date = str(datetime.date.today())
    # Get the current time, only hours, minutes and seconds.
    current_time = str(datetime.datetime.now())

    # Open the file and write the message.
    with open("Logs/Log_" + current_date + ".log", "a") as Log_File:
        Log_File.write(current_time + " | " + Log_Message + "\n")


class Style:
    FAIL = '\033[91m'
    LOG = '\033[92m'
    WARNING = '\033[93m'
    INFO = '\033[94m'

    HEADER = '\033[95m'
    CYAN = '\033[96m'

    WHITE = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    GREEN_BLOCK = '\x1b[5;30;42m'
    RED_BLOCK = '\x1b[5;30;41m'
    YELLOW_BLOCK = '\x1b[5;30;43m'
    BLUE_BLOCK = '\x1b[0;30;46m'


def print_log(message):

    """
    This function will print a log message in the console.
    """

    print(f"{Style.GREEN_BLOCK}[LOG]{Style.WHITE} [{inspect.stack()[1][3]}] {Style.UNDERLINE}[ln: {inspect.stack()[1][2]}]{Style.WHITE} " + message)
    Logger("[LOG] [{}] [ln: {}] {}".format(inspect.stack()[1][3], inspect.stack()[1][2], message))


def print_error(message):

    """
    This function will print an error message in the console.
    """

    print(f"{Style.RED_BLOCK}[ERROR]{Style.WHITE} " + message)
    Logger("[ERROR] " + message)


def print_warning(message):

    """
    This function will print a warning message in the console.
    """

    print(f"{Style.YELLOW_BLOCK}[WARNING]{Style.WHITE} " + message)
    Logger("[WARNING] " + message)


def print_info(message):

    """
    This function will print an info message in the console.
    """

    print(f"{Style.BLUE_BLOCK}[INFO]{Style.WHITE} " + message)
    Logger("[INFO] " + message)


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


def Asset(file_name_and_extension):

    """
    This function will return the image file from the file name inside Assets folder
    """

    for root, dirs, files in os.walk(Assets_directory):
        for file in files:

            if file.endswith(file_name_and_extension):
                return PhotoImage(file = os.path.join(root, file))

    print_warning("Asset not found: " + file_name_and_extension)
    return None

# my masterpiece!!
def Asset_color(file_name_and_extension, from_color, to_color):

    for root, dirs, files in os.walk(Assets_directory):
        for file in files:

            if file.endswith(file_name_and_extension):
                img = Image.open(os.path.join(root, file))
                img = img.convert("RGBA")
                image_data = img.getdata()

                # detect if from_color is in hex or string
                if from_color[0] == "#":
                    from_color = color_hex_rgb(from_color)
                else:
                    from_color = color_str_rgb(from_color)

                # detect if to_color is in hex or string
                if to_color[0] == "#":
                    to_color = color_hex_rgb(to_color)
                else:
                    # convert string color rgb
                    to_color = color_str_rgb(to_color)

                # replace colors
                newData = []
                for item in image_data:
                    if item[0] == from_color[0] and item[1] == from_color[1] and item[2] == from_color[2]:
                        newData.append(to_color + (255,))
                    else:
                        newData.append(item)

                img.putdata(newData)
                return ImageTk.PhotoImage(img)


def Asset_colored(file_name_and_extension, hue_value):

    for root, dirs, files in os.walk(Assets_directory):
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

def json_get(json_file, key):
    for root, dirs, files in os.walk(Assets_directory):
        for file in files:

            if file.endswith(json_file):
                with open(os.path.join(root, file), 'r') as f:
                    data = json.load(f)
                    return data[key]

    for root, dirs, files in os.walk(Disk_directory):
        for file in files:

            if file.endswith(json_file):
                with open(os.path.join(root, file), 'r') as f:
                    data = json.load(f)
                    return data[key]


def json_set(json_file, key, value):

    for root, dirs, files in os.walk(Assets_directory):
        for file in files:

            if file.endswith(json_file):
                with open(os.path.join(root, file), 'r') as f:
                    data = json.load(f)
                    data[key] = value
                    with open(os.path.join(root, file), 'w') as f:
                        json.dump(data, f, indent=4)

    for root, dirs, files in os.walk(Disk_directory):
        for file in files:

            if file.endswith(json_file):
                with open(os.path.join(root, file), 'r') as f:
                    data = json.load(f)
                    data[key] = value
                    with open(os.path.join(root, file), 'w') as f:
                        json.dump(data, f, indent=4)

def Image_getcolor(image, x, y):
    # get pixel color and return into hex format, like "#ff0000"

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
