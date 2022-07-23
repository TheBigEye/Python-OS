"""
    Module Name:
        FileSystem.py

    Abstract:
        This module implements the file system and related functions

    Author:
        TheBigEye 21-Jan-2022
"""

import datetime
import json
import os
import random
import shelve
from shelve import Shelf

from Libs.pyLogger.Logger import Logger
from Libs.pyUtils.pyData import JSON
from System.Utils.Vars import Assets_directory, Disk_directory

# ------------------------------------------------------------ [ Init ] ------------------------------------------------------------

FS_DISK_DATA_FILES = [
    (Disk_directory + "/FS/Filesystem.dat"), # save the file system
    (Disk_directory + "/FS/Filesystem.bak"), # save the file system backup
    (Disk_directory + "/FS/Filesystem.dir")  # save the file system structure
]

FS_DISK_FILE = (Disk_directory + "/FS/Filesystem")
BOOT_DATA_FILE = (Assets_directory + "/Data/System data/Boot/Boot.json")
FS_STRUCTURE_FILE = (Assets_directory + "/Data/System data/File system/FS.txt")

# read or make the file system data file
FS = shelve.open(FS_DISK_FILE, writeback=True)
current_dir = []

def FS_routines():

    def check_boot():
        if JSON.get(BOOT_DATA_FILE, "FS_mounted") != False:
            return

        Logger.error("File system is not mounted, installing ...")

        # delete the old file system
        if os.path.exists(FS_DISK_DATA_FILES[0]): os.remove(FS_DISK_DATA_FILES[0]) # delete the .dat file
        if os.path.exists(FS_DISK_DATA_FILES[1]): os.remove(FS_DISK_DATA_FILES[1]) # delete the .bak file
        if os.path.exists(FS_DISK_DATA_FILES[2]): os.remove(FS_DISK_DATA_FILES[2]) # delete the .dir file

        FS_model = shelve.open(FS_DISK_FILE, writeback=True)
        FS_install(FS_model)

        JSON.set(BOOT_DATA_FILE, "FS_mounted", True)

        Logger.debug("File system installed successfully")

    check_boot()
    Logger.info("File system ready!")

# ------------------------------------------------------------ [ Utils ] ------------------------------------------------------------

def FS_write(FS: Shelf):
    """
    Write the file system changes to the disk
    """

    FS.sync()

def FS_install(FS: Shelf):
    Username = "User"

    # Load the File system structure file
    with open(FS_STRUCTURE_FILE, 'r') as fs_structure:
        fs_data = fs_structure.read()

        # Get the %User% from the structure and change it to the username
        fs_data = fs_data.replace("%User%", Username)

        # Set the structure to the File system
        FS[""] = json.loads(fs_data)

        # save the File system
        FS.sync()

def FS_current_dictionary():
    """Return a dictionary representing the files in the current directory"""
    dir = FS[""]
    for key in current_dir:
        dir = dir[key]
    return dir

# ------------------------------------------------------------ [ Commands ] ------------------------------------------------------------

def List_directory() -> str:

    """
    List the files in the current directory

    Return:
        A string with the files aand  folders in the current directory
    """

    directory_data = ("Contents of directory " + str("/" + "/".join(current_dir) ) + '/:' + "\n")

    # show orderly alphabetically
    for element in sorted(FS_current_dictionary()):
        if "." in element:
            # Get metadata
            File_extension = str(element.split(".")[1] + " file")
            File_size = str(get_file_size(element))
            File_date = str(get_file_date(element))

            # Show the file
            directory_data += (" " + element + " " * (20 - len(element)) + " " + File_extension + " " * (10 - len(File_extension)) + " " + File_size + " " * (10 - len(File_size)) + " " + File_date + "\n")
        else:
            directory_data += (" " + element + "/\n")

    return directory_data

def Change_directory(directory) -> str: # cd equivalent

    """
    Change the current directory
    """

    # if the directory contains a dot and extension like .txt, cannot change directory into it
    if "." in directory and directory.split(".")[1] != "":

        return str("Cannot change the directory into a file")

    # if the directory is .., go to the parent directory
    if directory == "..":
        if len(current_dir) > 0:
            current_dir.pop()
        return str("Directory changed to " + str("/" + "/".join(current_dir) ) )

    # if the directory is a subdirectory, go to the subdirectory
    if directory in FS_current_dictionary():
        current_dir.append(directory)
        return str("Directory changed to " + str("/" + "/".join(current_dir)))

    return str("Directory " + directory + " does not exist")

# ------------------------------------------------------------ [ Files ] ------------------------------------------------------------

def make_directory(directory_name) -> str: # mkdir equivalent

    """
    Create a directory
    """

    # Check if the directory already exists in the current directory
    if directory_name in FS_current_dictionary():
        return str("Directory " + directory_name +" already exists in " + str("/" + "/".join(current_dir) ) )

    #Check if the name have a . in it, if so, it is a file and cannot be a directory
    if "." in directory_name:
        return str("Cannot create a directory with . in the name")

    # create an empty directory there and sync back to shelve dictionary!
    dir = FS_current_dictionary()
    dir[directory_name] = {}
    FS.sync()

    return str("Directory " + directory_name + " created in " + str("/" + "/".join(current_dir) ) )

def make_file(file_name) -> str: # touch equivalent

    """
    Create a file in the current directory
    """

    # Get the name and extension
    name = file_name.split(".")[0]
    extension = file_name.split(".")[1]

    name_and_extension = name + "." + extension

    # Check if the file already exists in the current directory
    if name_and_extension in FS_current_dictionary():
        Logger.warning("File {} already exists, overwriting", name_and_extension)

        # add a random number to the name, imposible to have a file with the same name :)
        name = name + "-" + str(random.randint(0, 512) + random.randint(0, 512))
        name_and_extension = name + "." + extension

        # create the file
        directory = FS_current_dictionary()
        directory[name_and_extension] = ""
        return

    Logger.info("Created file {} in {}", name_and_extension, str("/" + "/".join(current_dir)))

    dir = FS_current_dictionary()
    dir[name_and_extension] = {
            "Metadata": {
                "Extension": extension,
                "Created": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Modified": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            },
            "Data": ""
        }

    FS.sync()

    return str("File " + name_and_extension + " created in " + str("/" + "/".join(current_dir) ) )


def edit_file(file_name, content):

    """
    Edit the content of the file
    """

    # Check if the file exists
    if file_name not in FS_current_dictionary():
        return str("File " + file_name + " does not exist")

    dir = FS_current_dictionary()
    dir[file_name] = {
            "Metadata": {
                "Extension": dir[file_name]["Metadata"]["Extension"],
                "Created": dir[file_name]["Metadata"]["Created"],
                "Modified": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            },
            "Data": content
        }

    FS.sync()

    return str("File " + file_name + " edited")


def get_file_content(name_and_extension):

    """
    Return the content of the file
    """

    # Check if the file exists
    if name_and_extension not in FS_current_dictionary():
        Logger.error("File {} does not exist", name_and_extension)
        return

    Logger.info("Getting content of file {}", name_and_extension)

    dir = FS_current_dictionary()
    return dir[name_and_extension]["Data"]


def get_file_metadata(name_and_extension):

    """
    Return a dictionary with the metadata of the file
    """

    metadata_data = ""

    # Check if the file exists
    if name_and_extension not in FS_current_dictionary():
        Logger.error("File {} does not exist", name_and_extension)
        return

    Logger.info("Getting metadata of file {}", name_and_extension)

    dir = FS_current_dictionary()
    metadata_data += "File: " + name_and_extension + "\n"
    metadata_data += "Created: " + dir[name_and_extension]["Metadata"]["Created"] + "\n"
    metadata_data += "Modified: " + dir[name_and_extension]["Metadata"]["Modified"] + "\n"
    return metadata_data


def rmdir(name):

    """
    Remove a directory
    """

    # Check if the directory exists
    if name not in FS_current_dictionary():
        return str("Directory " + name + " does not exist")

    dir = FS_current_dictionary()
    del dir[name]
    FS.sync()

    return str("Directory " + name + " deleted")


def rmfile(name_and_extension):

    """
    Delete a file from the current directory
    """

    # Check if the file exists
    if name_and_extension not in FS_current_dictionary():
        Logger.error("File {} does not exist", name_and_extension)
        return

    Logger.info("Deleting file {}", name_and_extension)

    dir = FS_current_dictionary()
    del dir[name_and_extension]
    FS.sync()


def tree(*args):

    """
    Prints the tree of the current directory
    """

    tree = ""

    # if no argument is given, print the whole tree
    if len(args[0]) == 0:

        directory = FS_current_dictionary()
        tree += "Contents of " + str("/" + "/".join(current_dir) ) + '/:' + "\n"

    elif args[0] in FS_current_dictionary():

        directory = FS_current_dictionary()[args[0]]
        tree += "Contents of " + str("/" + "/".join(current_dir) ) + '/' + args[0] + '/:' + "\n"

    # if the direcotry not exists, return an error message
    else:
        return str("Directory " + args[0] + " does not exist at " + str("/" + "/".join(current_dir) ) )

    for deep_1 in sorted(directory):
        # ignore files, like: something.extension
        if "." not in deep_1:

            # if the directory is empty
            if len(directory[deep_1]) == 0:
                # Check if is the last dir in the current directory
                if deep_1 == sorted(directory)[-1]:
                    if len(directory) == 1:
                        tree += "└─── " + deep_1 + "\n"
                    else:
                        tree += "├─── " + deep_1 + "\n"
                else:
                    if len(directory) == 1:
                        tree += "└─── " + deep_1 + "\n"
                    else:
                        tree += "├─── " + deep_1 + "\n"

            else:
                # Check if is the last dir in the current directory
                if deep_1 == sorted(directory)[-1]:
                    if deep_1 == sorted(directory)[-2]:
                        tree += '└─── ' + deep_1 + "\n"
                    else:
                        if len(directory) == 1:
                            tree += '├─── ' + deep_1 + "\n"
                        else:
                            tree += "└─── " + deep_1 + "\n"

                else:
                    if deep_1 == sorted(directory)[-2]:
                        tree += '└─── ' + deep_1 + "\n"
                    else:
                        tree += '├─── ' + deep_1 + "\n"

                for deep_2 in sorted(directory[deep_1]):
                    # ignore files, like: something.extension
                    if "." not in deep_2:
                        # Check if is the last dir in the first directory
                        if deep_2 == sorted(directory[deep_1])[-1]:

                            if deep_2 == sorted(directory[deep_1])[-2]:
                                tree += '    ├─── ' + deep_2 + "\n"
                            else:
                                if deep_1 == sorted(directory)[-1]:
                                    tree += '    └─── ' + deep_2 + "\n"
                                else:
                                    if deep_1 == sorted(directory)[-2]:
                                        tree += '    └─── ' + deep_2 + "\n"
                                    else:
                                        tree += "|   └─── " + deep_2 + "\n"
                        else:
                            if deep_2 == sorted(directory[deep_1])[-2]:
                                if deep_1 == sorted(directory)[-1]:
                                    tree += '    ├─── ' + deep_2 + "\n"
                                else:
                                    if deep_1 == sorted(directory)[-2]:
                                        tree += '    ├─── ' + deep_2 + "\n"
                                    else:
                                        tree += '|   ├─── ' + deep_2 + "\n"

                            else:
                                if deep_2 == sorted(directory[deep_1])[-3]:
                                    tree += "    ├─── " + deep_2 + "\n"
                                else:
                                    tree += "|   └─── " + deep_2 + "\n"

    return tree

def get_folders():

    """
    Return a list with the folders of the current directory
    """

    directory = FS_current_dictionary()
    folders = []

    for deep_1 in sorted(directory):
        # ignore files, like: something.extension
        if "." not in deep_1:
            folders.append(deep_1)

    return folders

def get_files():

    """
    Return a list with the files of the current directory
    """

    directory = FS_current_dictionary()
    files = []

    for deep_1 in sorted(directory):
        # ignore files, like: something.extension
        if "." in deep_1:
            files.append(deep_1)

    return files

def get_files_and_folders_list():

    """
    Return a list with the files and folders of the current directory
    """

    directory = FS_current_dictionary()
    files_and_folders = []

    for deep_1 in sorted(directory):
        # ignore files, like: something.extension
        if "." in deep_1:
            files_and_folders.append(deep_1)
        else:
            files_and_folders.append(deep_1)

    return files_and_folders

def get_current_directory():

    """
    Return the current directory
    """

    return "/" + "/".join(current_dir)

def get_file_date(name_and_extension):

    """
    Return the created date of the file from the metadata
    """

    # Check if the file exists
    if name_and_extension not in FS_current_dictionary():
        Logger.error("File {} does not exist", name_and_extension)
        return

    # Get the metadata of the file
    dir = FS_current_dictionary()
    meta = str(dir[name_and_extension]["Metadata"]["Created"])

    # Return the created date of the file
    return meta

def get_file_size(name_and_extension):
    # Get the file content and caculate the size in bytes

    # Check if the file exists
    if name_and_extension not in FS_current_dictionary():
        Logger.error("File {} does not exist", name_and_extension)
        return

    # Get the metadata of the file
    dir = FS_current_dictionary()
    content = str(dir[name_and_extension]["Data"])
    content_size = len(content)

    # Return the size in bytes
    size = str(content_size) + " bytes"
    return size
