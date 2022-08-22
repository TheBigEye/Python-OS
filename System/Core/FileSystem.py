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
import re
import shelve
from shelve import Shelf
from typing import Any, Dict, List, Union

from Libs.pyLogger.Logger import Logger
from Libs.pyUtils.pyData import JSON

from System.utils.vars import Assets_directory, Disk_directory

FS_DISK_DATA_FILES = [
    (Disk_directory + "/FS/Filesystem.dat"), # save the file system
    (Disk_directory + "/FS/Filesystem.bak"), # save the file system backup
    (Disk_directory + "/FS/Filesystem.dir")  # save the file system structure
]

FS_DISK_FILE = (Disk_directory + "/FS/Filesystem")
BOOT_DATA_FILE = (Assets_directory + "/Data/System data/Boot/Boot.json")
FS_STRUCTURE_FILE = (Assets_directory + "/Data/System data/File system/FS.txt")

# TODO: in case some future version of python no longer supports shelve, port this to sqlite3

# read or make the file system data file
FS_data = shelve.open(FS_DISK_FILE, writeback=True)
current_dir = []

def FS_routines() -> None:
    """ Run the file system routines """

    def check_boot():

        """ Check if in the boot the file system is mounted """

        if JSON.get(BOOT_DATA_FILE, "FS_mounted") is not False:
            return

        Logger.error("File system is not mounted, installing ...")

        # delete the old file system
        if os.path.exists(FS_DISK_DATA_FILES[0]): os.remove(FS_DISK_DATA_FILES[0]) # delete the .dat file
        if os.path.exists(FS_DISK_DATA_FILES[1]): os.remove(FS_DISK_DATA_FILES[1]) # delete the .bak file
        if os.path.exists(FS_DISK_DATA_FILES[2]): os.remove(FS_DISK_DATA_FILES[2]) # delete the .dir file

        FS_model = shelve.open(FS_DISK_FILE, writeback=True)
        install(FS_model)

        JSON.set(BOOT_DATA_FILE, "FS_mounted", True)

        Logger.debug("File system installed successfully")

    check_boot()
    Logger.info("File system ready!")

def write(FS_data: Shelf):
    """ Write the file system changes to the disk """

    FS_data.sync()

def install(FS_image: Shelf) -> None:
    """
    Install the file system

    Arguments:
        FS: the file system database file
    """

    Username = "User"

    # Load the File system structure file
    with open(FS_STRUCTURE_FILE, 'r') as structure:
        data = structure.read()

        # Get the %User% from the structure and change it to the username
        data = data.replace("%User%", Username)

        # Set the structure to the File system
        FS_image[""] = json.loads(data)

        # save the File system
        FS_image.sync()

def current_dictionary() -> Dict[str, Dict[str, Union[Dict[str, Dict[Any, Any]], Dict[str, str], str]]]:
    this_directory = FS_data[""]

    for key in current_dir:
        this_directory = this_directory[key]

    return this_directory

def list_directory() -> str:
    """
    List the files in the current directory

    Return:
        A string with the files and folders in the current directory
    """

    directory_data = ""
    current_directory = current_dictionary()

    # show orderly alphabetically
    for element in sorted(current_directory):
        if "." in element:
            # Get metadata
            File_extension = str(str(element).split(".")[1] + " file")
            File_size = str(get_file_size(element))
            File_date = str(get_file_date(element))

            # Show the file
            directory_data += str(" " + element + " " * (20 - len(element)) + " " + File_extension + " " * (10 - len(File_extension)) + " " + File_size + " " * (10 - len(File_size)) + " " + File_date + "\n")
        else:
            directory_data += str(" " + element + "/" + " " * (20 - len(element + "/")) + " " + "--- dir" + "\n")

    return directory_data

def change_directory(directory: str) -> int: # cd equivalent

    """
    Change the current directory

    Return:
        0: If the directory exists and the current directory is changed.
        1: If the directory does not exist.
        2: If the directory is not a directory.
    """

    # if the directory contains a dot and extension like .txt, cannot change directory into it
    if "." in directory and directory.split(".")[1] != "":
        return 2 # cannot change the directory into a file

    # if the directory is .., go to the parent directory
    if directory == ".." or directory == "<-":
        if len(current_dir) > 0:
            current_dir.pop()
        return 0 # success

    # if the directory is a subdirectory, go to the subdirectory
    if directory in current_dictionary():
        current_dir.append(directory)
        return 0 # success

    return 1 # directory not found

def make_directory(directory_name) -> int: # mkdir equivalent

    """
    Create a directory

    Return:
        0: If the directory is created successfully.
        1: If the directory already exists.
        2: If the directory name is invalid.
    """

    # Check if the directory already exists in the current directory
    if directory_name in current_dictionary():
        return 1 # directory already exists

    #Check if the name have a . in it, if so, it is a file and cannot be a directory
    if "." in directory_name:
        return 2 # cannot create a directory with a file name

    # create an empty directory there and sync back to shelve dictionary!
    this_directory = current_dictionary()
    this_directory[directory_name] = {}
    FS_data.sync()

    return 0 # Directory created successfully

def make_file(file_name: str) -> int:

    """
    Create a empty file in the current directory

    Return:
        0: If the file is created successfully.
        1: If the file already exists.
        2: If the file name is invalid. (only letters, numbers, spaces and underscores are allowed).
        3: If the file name is too long (max 48 characters).
        4: If the file name is too short (min 1 character).
    """

    # Get the name and extension
    name = file_name.split(".")[0]
    extension = file_name.split(".")[1]
    name_and_extension = str(name + "." + extension)

    if name_and_extension in current_dictionary(): return 1 # Check if the file already exists in the current directory
    if not re.match("^[a-zA-Z0-9_ ]+$", name): return 2# Check if the file name is invalid
    if len(name) > 48: return 3 # Check if the file name is too long
    if len(name) < 1: return 4 # Check if the file name is too short

    # If all is good, create the file
    this_directory = current_dictionary()
    this_directory[name_and_extension] = {
        "Metadata": {
            "Extension": extension,
            "Created": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Modified": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        "Data": ""
    }

    FS_data.sync()

    return 0 # File created successfully

def edit_file(file_name, content):

    """
    Edit the content of the file
    """

    # Check if the file exists
    if file_name not in current_dictionary():
        return str("File " + file_name + " does not exist")

    this_directory = current_dictionary()
    this_directory[file_name] = {
            "Metadata": {
                "Extension": this_directory[file_name]["Metadata"]["Extension"],
                "Created": this_directory[file_name]["Metadata"]["Created"],
                "Modified": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            },
            "Data": content
        }

    FS_data.sync()

    return str("File " + file_name + " edited")


def move_file(file_name, destination):

    """
    Move the file to another directory

    Return:
        0: If the file is moved successfully.
        1: If the file does not exist.
        2: If the destination directory does not exist.
        3: If the destination is not a directory.
        4: If the file already exists in the destination directory.
    """

    # Check if the file exists in the current directory
    if file_name not in current_dictionary():
        return 1 # File does not exist

    # if the destination is .. or <-, move the file to the parent directory
    if destination == ".." or destination == "<-":

        # FIXME: Check if the file already exists in the parent directory, actually,
        # the functiom exists, but cannot move back to the parent directory a file from depth 3 folder

        # copy the file and save in  a variable
        file_data = current_dictionary()[file_name]

        # get the parent directory
        parent_directory = current_dir[:-1]

        # check if the file already exists in the parent directory
        if file_name in FS_data["/".join(parent_directory)]:
            return 4

        # delete the file from the current directory
        del current_dictionary()[file_name]

        # go to the parent directory
        if len(current_dir) > 0:
            current_dir.pop()

        # copy the file to the parent directory
        current_dictionary()[file_name] = file_data

        FS_data.sync()

        return 0 # success
    else:

        # Check if the destination is a directory
        if destination not in current_dictionary():
            return 2 # Destination directory does not exist

        if "." in destination:
            return 3 # Destination is not a directory

        # get the parent destination directory
        parent_directory = current_dictionary()[destination]

        # check if the file already exists in the destination directory
        if file_name in parent_directory:
            return 4

        # Move the file
        this_directory = current_dictionary()
        this_directory[destination][file_name] = this_directory[file_name]
        del this_directory[file_name]

        FS_data.sync()
        return 0 # success


def get_file_content(name_and_extension: str):

    """
    Return the content of the file
    """

    # Check if the file exists
    if name_and_extension not in current_dictionary():
        Logger.error("File {} does not exist", name_and_extension)
        return

    Logger.info("Getting content of file {}", name_and_extension)

    this_directory = current_dictionary()
    this_file = this_directory[name_and_extension]["Data"]

    return this_file

def get_file_metadata(name_and_extension: str):

    """
    Return a dictionary with the metadata of the file
    """

    metadata = ""

    # Check if the file exists
    if name_and_extension not in current_dictionary():
        Logger.error("File {} does not exist", name_and_extension)
        return

    Logger.info("Getting metadata of file {}", name_and_extension)

    this_directory = current_dictionary()
    this_file = this_directory[name_and_extension]

    metadata += "File: " + name_and_extension + "\n"
    metadata += "Created: " + this_file["Metadata"]["Created"] + "\n"
    metadata += "Modified: " + this_file["Metadata"]["Modified"] + "\n"

    return metadata

def remove_directory(name: str) -> int:

    """
    Remove a directory
    """

    # Check if the directory exists
    if name not in current_dictionary():
        return 1 # directory not found

    # Check if the direcotry is not a file
    if "." in name:
        return 2 # cannot remove a file

    this_directory = current_dictionary()
    del this_directory[name]
    FS_data.sync()

    return 0 # Directory removed successfully


def remove_file(name_and_extension) -> None:

    """
    Delete a file from the current directory
    """

    this_directory = current_dictionary()

    # Check if the file exists
    if name_and_extension not in this_directory:
        Logger.error("File {} does not exist", name_and_extension)
        return

    Logger.info("Deleting file {}", name_and_extension)
    del this_directory[name_and_extension]

    FS_data.sync()

def get_folders() -> List[str]:
    """ Return a list with the folders of the current directory """

    directory = current_dictionary()
    folders = []

    for deep_1 in sorted(directory):
        # ignore files, like: something.extension
        if "." not in deep_1:
            folders.append(deep_1)

    return folders

def get_files() -> List[str]:
    """ Return a list with the files of the current directory """

    directory = current_dictionary()
    files = []

    for deep_1 in sorted(directory):
        # ignore files, like: something.extension
        if "." in deep_1:
            files.append(deep_1)

    return files

def get_files_and_folders_list():
    """ Return a list with the files and folders of the current directory """

    directory = current_dictionary()
    files_and_folders = []

    for deep_1 in sorted(directory):
        # ignore files, like: something.extension
        if "." in deep_1:
            files_and_folders.append(deep_1)
        else:
            files_and_folders.append(deep_1)

    return files_and_folders

def get_current_directory() -> str:
    """ Return the current directory """

    return "/" + "/".join(current_dir)

def get_file_date(name_and_extension: str) -> str:
    """ Get the file creation date from the metadata """

    this_directory = current_dictionary()

    # Check if the file exists
    if name_and_extension not in this_directory:
        Logger.error("File {} does not exist", name_and_extension)
        return

    # Get the metadata of the file
    this_file = this_directory[name_and_extension]
    metadata = str(this_file["Metadata"]["Created"])

    # Return the created date of the file
    return metadata

def get_file_size(name_and_extension: str) -> str:
    """ Get the file content and caculate the size in bytes """

    this_directory = current_dictionary()

    # Check if the file exists
    if name_and_extension not in this_directory:
        Logger.error("File {} does not exist", name_and_extension)
        return

    # Get the metadata of the file

    this_file = this_directory[name_and_extension]
    content = str(this_file["Data"])
    content_size = len(content)

    # Return the size in bytes
    size = str(content_size) + " bytes"
    return size
