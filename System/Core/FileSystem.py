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

from Libs.pyLogger.Logger import Logger
from System.Utils.Utils import get_json, set_json
from System.Utils.Vars import Assets_directory

File_System = shelve.open('Disk/FS/Filesystem', writeback=True)
current_dir = []

def fs_routines():

    # laod boot data
    with open(Assets_directory + "/Data/Boot data/Boot.json", "r") as boot_data_file:
        boot_data = json.load(boot_data_file)

    def check_boot():
        if get_json(Assets_directory + "/Data/Boot data/Boot.json", "FS_mounted") != False:
            return

        Logger.error("File system is not mounted, installing...")

        # delete the .dat, bak and dir files in Disk/FS/ for avoid errors
        if os.path.exists("Disk/FS/Filesystem.dat"): os.remove("Disk/FS/Filesystem.dat")
        if os.path.exists("Disk/FS/Filesystem.bak"): os.remove("Disk/FS/Filesystem.bak")
        if os.path.exists("Disk/FS/Filesystem.dir"): os.remove("Disk/FS/Filesystem.dir")

        File_System = shelve.open('Disk/FS/Filesystem', writeback=True)
        install(File_System)

        set_json(Assets_directory + "/Data/Boot data/Boot.json", "FS_mounted", True)

        Logger.log("File system installed successfully")

    check_boot()
    Logger.info("File system ready!")

def install(File_System):
    Username = "User"

    # Load the File system structure file
    with open('Assets/Data/Boot data/FS', 'r') as fs_structure:
        fs_data = fs_structure.read()

        # Get the %User% from the structure and change it to the username
        fs_data = fs_data.replace("%User%", Username)

    # Set the structure to the File system
    File_System[""] = json.loads(fs_data)

    # save the File system
    File_System.sync()

def current_dictionary():
    """Return a dictionary representing the files in the current directory"""
    dir = File_System[""]
    for key in current_dir:
        dir = dir[key]

    return dir

def ls():

    """
    List the files in the current directory
    """

    list_dir = ""

    list_dir += "Contents of directory " + str("/" + "/".join(current_dir) ) + '/:' + "\n"

    # show orderly alphabetically
    for key in sorted(current_dictionary()):
        list_dir += "   " + key + "\n"

    return list_dir

def cd(directory):

    """
    Change the current directory
    """

    # if the directory contains a dot and extension like .txt, cannot cd into it
    if "." in directory and directory.split(".")[1] != "":

        return str("Cannot cd into file")

    global current_dir

    # if the directory is .., go to the parent directory
    if directory == "..":
        if len(current_dir) > 0:
            current_dir.pop()
        return str("Directory changed to " + str("/" + "/".join(current_dir) ) )

    # if the directory is a subdirectory, go to the subdirectory
    if directory in current_dictionary():
        current_dir.append(directory)
        return str("Directory changed to " + str("/" + "/".join(current_dir)))

    return str("Directory " + directory + " does not exist")

def mkdir(name):

    """
    Create a directory
    """

    global File_System

    # Check if the directory already exists in the current directory
    if name in current_dictionary():
        return str("Directory " + name +" already exists in " + str("/" + "/".join(current_dir) ) )

    # create an empty directory there and sync back to shelve dictionary!
    dir = current_dictionary()
    dir[name] = {}
    File_System.sync()

    return str("Directory " + name + " created in " + str("/" + "/".join(current_dir) ) )

def mkfile(argument):

    """
    Create a file in the current directory
    """

    global File_System

    # Get the name and extension
    name = argument.split(".")[0]
    extension = argument.split(".")[1]

    name_and_extension = name + "." + extension

    # Check if the file already exists in the current directory
    if name_and_extension in current_dictionary():
        Logger.warning("File {} already exists, overwriting", name_and_extension)

        # add a random number to the name, imposible to have a file with the same name :)
        name = name + "-" + str(random.randint(0, 512) + random.randint(0, 512))
        name_and_extension = name + "." + extension

        # create the file
        directory = current_dictionary()
        directory[name_and_extension] = ""
        return

    Logger.info("Created file {} in {}", name_and_extension, str("/" + "/".join(current_dir)))

    dir = current_dictionary()
    dir[name_and_extension] = {
            "Metadata": {
                "Extension": extension,
                "Created": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Modified": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            },
            "Data": ""
        }

    # convert dir[name_and_extension] to json sctructure and print it
    for key in dir[name_and_extension]:
        print(key, ":", dir[name_and_extension][key])



    File_System.sync()


def edit_file(name_and_extension, content):

    """
    Edit the content of the file
    """

    global File_System

    # Check if the file exists
    if name_and_extension not in current_dictionary():
        return str("File " + name_and_extension + " does not exist")

    dir = current_dictionary()
    dir[name_and_extension] = {
            "Metadata": {
                "Extension": dir[name_and_extension]["Metadata"]["Extension"],
                "Created": dir[name_and_extension]["Metadata"]["Created"],
                "Modified": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            },
            "Data": content
        }

    File_System.sync()

    return str("File " + name_and_extension + " edited")


def get_file_content(name_and_extension):

    """
    Return the content of the file
    """

    global File_System

    # Check if the file exists
    if name_and_extension not in current_dictionary():
        Logger.error("File {} does not exist", name_and_extension)
        return

    Logger.info("Getting content of file {}", name_and_extension)

    dir = current_dictionary()
    return dir[name_and_extension]["Data"]


def get_file_metadata(name_and_extension):

    """
    Return a dictionary with the metadata of the file
    """

    global File_System

    meta = ""

    # Check if the file exists
    if name_and_extension not in current_dictionary():
        Logger.error("File {} does not exist", name_and_extension)
        return

    Logger.info("Getting metadata of file {}", name_and_extension)

    dir = current_dictionary()
    meta += "File: " + name_and_extension + "\n"
    meta += "Created: " + dir[name_and_extension]["Metadata"]["Created"] + "\n"
    meta += "Modified: " + dir[name_and_extension]["Metadata"]["Modified"] + "\n"
    return meta


def rmdir(name):

    """
    Remove a directory
    """

    global File_System

    # Check if the directory exists
    if name not in current_dictionary():
        return str("Directory " + name + " does not exist")

    dir = current_dictionary()
    del dir[name]
    File_System.sync()

    return str("Directory " + name + " deleted")


def rmfile(name_and_extension):

    """
    Delete a file from the current directory
    """

    global File_System

    # Check if the file exists
    if name_and_extension not in current_dictionary():
        Logger.error("File {} does not exist", name_and_extension)
        return

    Logger.info("Deleting file {}", name_and_extension)

    dir = current_dictionary()
    del dir[name_and_extension]
    File_System.sync()


def tree(*args):

    """
    Prints the tree of the current directory
    """

    global File_System

    tree = ""

    # if no argument is given, print the whole tree
    if args[0] == "$null":

        directory = current_dictionary()
        tree += "Contents of " + str("/" + "/".join(current_dir) ) + '/:' + "\n"

    elif args[0] in current_dictionary():

        directory = current_dictionary()[args[0]]
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

    global File_System

    directory = current_dictionary()
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

    global File_System

    directory = current_dictionary()
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

    global File_System

    directory = current_dictionary()
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

    # example of current_dir: ['root', 'folder', 'folder2']
    # return '/root/folder/folder2'
    return "/" + "/".join(current_dir)

def get_file_date(name_and_extension):

    """
    Return the created date of the file from the metadata
    """

    global File_System

    # Check if the file exists
    if name_and_extension not in current_dictionary():
        Logger.error("File {} does not exist", name_and_extension)
        return

    # Get the metadata of the file
    dir = current_dictionary()
    meta = str(dir[name_and_extension]["Metadata"]["Created"])

    # Return the created date of the file
    return meta

def get_file_size(name_and_extension):
    # Get the file content and caculate the size in bytes
    global File_System

    # Check if the file exists
    if name_and_extension not in current_dictionary():
        Logger.error("File {} does not exist", name_and_extension)
        return

    # Get the metadata of the file
    dir = current_dictionary()
    content = str(dir[name_and_extension]["Data"])
    content_size = len(content)

    # Return the size in bytes
    size = str(content_size) + " bytes"
    return size
