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
def print_log(message):
    print(message)
    Logger_improved(message)


def print_error(message):    
    print("[ERROR] " + message)
    Logger_improved("[ERROR] " + message)


def print_warning(message):
    print("[WARNING] " + message)
    Logger_improved("[WARNING] " + message)


def print_info(message):
    print("[INFO] " + message)
    Logger_improved("[INFO] " + message)


# Time and date --------------------------------------------------------------------------------------------------------------------------------------------------------------------

# A function that will return the current time in a string format.
def Get_Current_Time():
    return str(datetime.datetime.now())


# A function that will return the current date in a string format.
def Get_Current_Date():
    return str(datetime.date.today())


# A function that will return the current date and time in a string format.
def Get_Current_Date_Time():
    return str(datetime.datetime.now())










