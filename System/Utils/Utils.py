import inspect
import os
import datetime
from tkinter import PhotoImage

from System.Utils.Vars import Assets_dir

# Loggers ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# A Logger, this will be used to log all the errors and information in a file in the Logs folder.
def Logger(Log_Message):

    # If the file does not exist, it creates it in the path where this project is, inside the Logs folder.
    if not os.path.exists("Logs"):
        os.makedirs("Logs")

    # Get the current date.
    current_date = str(datetime.date.today())
    # Get the current time, only hours, minutes and seconds.
    current_time = str(datetime.datetime.now())[11:19]

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


def print_log(message):
    print(f"{CharColors.LOG}[{inspect.stack()[1][3]}] {CharColors.ENDC}" + message)
    Logger("[{}] {}".format(inspect.stack()[1][3], message))


def print_error(message):
    print(f"{CharColors.FAIL}[ERROR] {CharColors.ENDC}" + message)
    Logger("[ERROR] " + message)


def print_warning(message):
    print(f"{CharColors.WARNING}[WARNING] {CharColors.ENDC}" + message)
    Logger("[WARNING] " + message)


def print_info(message):
    print(f"{CharColors.INFO}[INFO] {CharColors.ENDC}" + message)
    Logger("[INFO] " + message)


# Tiempo  --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Esta funcion retorna el tiempo como String.
def Get_Current_Time():
    current_time = str(datetime.datetime.now())
    return current_time


# Esta funcion retorna la fecha en un string.
def Get_Current_Date():
    current_date = str(datetime.date.today())
    return current_date


# Esta funcion retorna el tiempo y la fecha en un string.
def Get_Current_Date_Time():
    current_date_time = str(datetime.datetime.now())
    return current_date_time


def Execute(master, Loading_time: float, Function, *args):
    global Open, Loading_cursor, Normal_cursor

    # the Display_Terminal() function will run in different threads, so we need to use the tkinter.after() method to call it
    # after the start_menu is closed
    def Open():
        Function(*args)

    def Loading_cursor():
            master.config(cursor="wait")

    def Normal_cursor():
            master.config(cursor="")

    master.after(100, Loading_cursor)
    master.after(Loading_time, Open)
    master.after(1512, Normal_cursor)


def get_asset(path):

    path = path.replace("Assets/", "/")
    Asset = PhotoImage(file= Assets_dir + path)

    return Asset













