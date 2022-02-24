import datetime
import inspect
import json
import os
import urllib.request
from tkinter import PhotoImage

from System.Utils.Vars import Assets_directory

# Loggers ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# A Logger, this will be used to log all the errors and information in a file in the Logs folder.
def Logger(Log_Message):

    # If the file does not exist, it creates it in the path where this project is, inside the Logs folder.
    if not os.path.exists("Logs"):
        os.makedirs("Logs")

    # Get the current date.
    current_date = str(datetime.date.today())
    # Get the current time, only hours, minutes and seconds.
    current_time = str(datetime.datetime.now())

    # Open the file and write the message.
    with open("Logs/Log_" + current_date + ".log", "a") as Log_File:
        Log_File.write(current_time + " | " + Log_Message + "\n")


# Print ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class CharColors:
    FAIL = '\033[91m'
    LOG = '\033[92m'
    WARNING = '\033[93m'
    INFO = '\033[94m'

    HEADER = '\033[95m'
    OKCYAN = '\033[96m'

    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    GREEN_BLOCK = '\x1b[5;30;42m'
    RED_BLOCK = '\x1b[5;30;41m'
    YELLOW_BLOCK = '\x1b[5;30;43m'
    BLUE_BLOCK = '\x1b[0;30;46m'


def print_log(message):

    # example: [LOG][module_name][line_number] message.
    print(f"{CharColors.GREEN_BLOCK}[LOG]{CharColors.ENDC} [{inspect.stack()[1][3]}] {CharColors.UNDERLINE}[ln: {inspect.stack()[1][2]}]{CharColors.ENDC} " + message)
    Logger("[LOG] [{}] [ln: {}] {}".format(inspect.stack()[1][3], inspect.stack()[1][2], message))


def print_error(message):
    print(f"{CharColors.RED_BLOCK}[ERROR]{CharColors.ENDC} " + message)
    Logger("[ERROR] " + message)


def print_warning(message):
    print(f"{CharColors.YELLOW_BLOCK}[WARNING]{CharColors.ENDC} " + message)
    Logger("[WARNING] " + message)


def print_info(message):
    print(f"{CharColors.BLUE_BLOCK}[INFO]{CharColors.ENDC} " + message)
    Logger("[INFO] " + message)


# Time --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# This function returns the time as a String.
def Get_Current_Time():
    current_time = str(datetime.datetime.now())
    return current_time

# This function returns the date in a string.
def Get_Current_Date():
    current_date = str(datetime.date.today())
    return current_date


# This function returns the time and date in a string.
def Get_Current_Date_Time():
    current_date_time = str(datetime.datetime.now())
    return current_date_time


# Misc --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# This function will execute a function with a loading time.
def Execute(master, Loading_time: float, Function, *args):
    global Open, Loading_cursor, Normal_cursor

    def Open():
        Function(*args)

    def Loading_cursor():
            master.config(cursor="wait")

    def Normal_cursor():
            master.config(cursor = "")

    master.after(100, Loading_cursor)
    master.after(Loading_time, Open)
    master.after(1512, Normal_cursor)


# This function will return the image file from the file name inside Assets folder.
def Asset(file_name_and_extension):

    for root, dirs, files in os.walk(Assets_directory):
        for file in files:

            if file.endswith(file_name_and_extension):
                return PhotoImage(file = os.path.join(root, file))

    print_warning("Asset not found: " + file_name_and_extension)
    return None


# Check if the internet is on.
def internet_on():
    try:
        response = urllib.request.urlopen('http://www.google.com', timeout=1)
        if response.code == 200:
            return True
    except:
        return False


def json_get(json_file_path, key):
    # get the key value from the json file as UTF8
    with open(json_file_path, encoding="utf8") as json_file:
        data = json.load(json_file)
        return data[key]

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------















