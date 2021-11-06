# System variables (| Variable | True/False/int |)
import os
import datetime

Kernel_lvl = "NULL"  # Kernel main variable

Is_FAIL =           False  # 0
Is_in_BIOS =        False  # 1
Is_in_INSTALLER =   False  # 2
Is_in_Boot =        False  # 3
Is_in_Login =       False  # 4
Is_in_Desktop =     False  # 5
Is_Boot =           False  # NULL

# Boot order
if Kernel_lvl == 0:  # Fail message

    Is_FAIL = True

elif Kernel_lvl == 1:  # BIOS Screen

    Is_in_BIOS = True

elif Kernel_lvl == 2:  # OS Installer

    Is_in_INSTALLER = True

elif Kernel_lvl == 3:  # Bootloader

    Is_in_Boot = True

elif Kernel_lvl == 4:  # Login Screen

    Is_in_Login = True

elif Kernel_lvl == 5:  # In the desktop

    Is_in_Desktop = True

elif Kernel_lvl == "NULL":  # Normal boot

    Is_Boot = True


# Implements a Logger, this will be used to log all the errors and information in a file in the Logs folder.
def Logger(Log_Message):

    # If the file does not exist, it creates it in the path where this project is, inside the Logs folder.
    if not os.path.exists("Logs"):
        os.makedirs("Logs")

    current_time = str(datetime.datetime.now())

    # Open the file and write the message.
    with open("Logs/Log.txt", "a") as Log_File:
        Log_File.write(current_time + " | " + Log_Message + "\n")


# Define the Routines() method, inside there will be functions and things that will be executed when calling this method.
def routines():

    if Is_Boot:  # Normal boot

        Logger("Starting from Normal boot")

    elif Is_in_BIOS:  # BIOS Screen

        Logger("Starting from BIOS Screen")

    elif Is_in_INSTALLER:  # OS Installer

        Logger("Starting from OS Installer")

    elif Is_in_Boot:  # Bootloader

        Logger("Starting from Bootloader")

    elif Is_in_Login:  # Login Screen

        Logger("Starting from Login Screen")

    elif Is_in_Desktop:  # In the desktop

        Logger("Starting from In the desktop")

    elif Is_FAIL:  # Fail message

        Logger("Fail message, STOPING...")

    else:  # Unknown

        Logger("Unknown boot method!")

    
