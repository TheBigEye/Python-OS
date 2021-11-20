import inspect
import os
import datetime

# Loggers ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# A Logger, this will be used to log all the errors and information in a file in the Logs folder.
def Logger(Log_Message):

    # If the file does not exist, it creates it in the path where this project is, inside the Logs folder.
    if not os.path.exists("Logs"):
        os.makedirs("Logs")
    current_time = str(datetime.datetime.now())

    # Open the file and write the message.
    with open("Logs/Log.txt", "a") as Log_File:
        Log_File.write(current_time + " | " + Log_Message + "\n")


# Improved version.
def Logger_improved(Log_Message):
    
    # If the file does not exist, it creates it in the path where this project is, inside the Logs folder.
    if not os.path.exists("Logs"):
        os.makedirs("Logs")

    # Get the current date.
    current_date = str(datetime.date.today())
    # Get the current time, only hours, minutes and seconds.
    current_time = str(datetime.datetime.now())[11:19]
    
    # Open the file and write the message.
    with open("Logs/Log_" + current_date + ".txt", "a") as Log_File:
        Log_File.write(current_time + " | " + Log_Message + "\n")


# Print ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class CHAR_colors:
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
    print(f"{CHAR_colors.LOG}[LOG] {CHAR_colors.ENDC}" + message)
    Logger_improved(message)


def print_error(message):    
    print(f"{CHAR_colors.FAIL}[ERROR] {CHAR_colors.ENDC}" + message)
    Logger_improved("[ERROR] " + message)


def print_warning(message):
    print(f"{CHAR_colors.WARNING}[WARNING] {CHAR_colors.ENDC}" + message)
    Logger_improved("[WARNING] " + message)


def print_info(message):
    print(f"{CHAR_colors.INFO}[INFO] {CHAR_colors.ENDC}" + message)
    Logger_improved("[INFO] " + message)


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










