
import datetime

from System.Core.FileSystem import fs_routines
from System.Core.TaskSystem import ts_routines
from System.Utils.Utils import print_log

Kernel_lvl = 6 # Main kernel variable

# Each screen has an ID
Is_FAIL = False         # 0
Is_in_BIOS = False      # 1
Is_in_INSTALLER = False # 2
Is_in_Boot = False      # 3
Is_in_Login = False     # 4
Is_in_Desktop = False   # 5
Is_Boot = False         # 6


# Start the boot order
if Kernel_lvl == 0:
    Is_FAIL = True

elif Kernel_lvl == 1:
    Is_in_BIOS = True

elif Kernel_lvl == 2:
    Is_in_INSTALLER = True

elif Kernel_lvl == 3:
    Is_in_Boot = True

elif Kernel_lvl == 4:
    Is_in_Login = True

elif Kernel_lvl == 5:
    Is_in_Desktop = True

elif Kernel_lvl == 6:
    Is_Boot = True


# Routines, are the first tasks that are executed in the first seconds of system startup
def routines():

    print_log("")
    print_log("---------- Starting system execution ----------")
    print_log("Start date and time: " + str(datetime.datetime.now()))

    # Load the process system
    ts_routines()

    # Load the file system
    fs_routines()


def delete_logs():
    # Delete the files inside the Logs folder using the os module
    import os

    from System.Utils.Utils import print_info

    # Get the relative path of the Logs folder
    Logs_path = os.path.join(os.getcwd(), "Logs")

    # Get the list of files inside the Logs folder
    Logs_files = os.listdir(Logs_path)

    # Print an information message
    print_info("Deleting files from the Logs folder")

    # Delete the files inside the Logs folder
    for file in Logs_files:
        os.remove(os.path.join(Logs_path, file))
        print(os.path.join(Logs_path, file))
