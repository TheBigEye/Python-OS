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

from System.Utils.Utils import Logger

File_System = shelve.open('Disk/FS/Filesystem', writeback=True)
current_dir = []

def fs_routines():

    # laod boot data
    with open('Disk/Boot.json', 'r') as f:
        boot_data = json.load(f)

    def check_boot():
        if boot_data["FS_mounted"] != "False":
            return
        Logger.fail("File system is not mounted, installing...")

        # delete the .dat, bak and dir files in Disk/FS/ for avoid errors
        if os.path.exists("Disk/FS/Filesystem.dat"): os.remove("Disk/FS/Filesystem.dat")
        if os.path.exists("Disk/FS/Filesystem.bak"): os.remove("Disk/FS/Filesystem.bak")
        if os.path.exists("Disk/FS/Filesystem.dir"): os.remove("Disk/FS/Filesystem.dir")

        File_System = shelve.open('Disk/FS/Filesystem', writeback=True)
        install(File_System)

        boot_data["FS_mounted"] = "True"

        with open("Disk/Boot.json", "w") as f:
            json.dump(boot_data, f, indent=4)

        Logger.info("File system installed successfully")

    check_boot()
    Logger.info("File system ready!")

def install(File_System):
    # create root and others
    Username = "User"

    # default filesystem structure
    File_System[""] = {
        "Home": {
            "Programs": {},
            Username: {
                "Desktop": {},
                "Documents": {},
                "Music": {}
            }
        },
        "System": {
            "Core": {
                "Temp": {},
            },
            "Boot": {},
            "Lib": {}
        }
    }

    # sync the filesystem
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
        Logger.fail("File {} does not exist", name_and_extension)
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
        Logger.fail("File {} does not exist", name_and_extension)
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
        Logger.fail("File {} does not exist", name_and_extension)
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

    for deep_1 in sorted(directory):
        if "." in deep_1:
            continue
        tree += "|----" + deep_1 + '\n'

        for deep_2 in sorted(directory[deep_1]):
            if "." in deep_2:
                continue
            tree += "|    |----" + deep_2 + '\n'

            for deep_3 in sorted(directory[deep_1][deep_2]):
                if "." in deep_3:
                    continue
                tree += "|    |    |----" + deep_3 + '\n'

                for deep_4 in sorted(directory[deep_1][deep_2][deep_3]):
                    if "." in deep_4:
                        continue
                    tree += "|    |    |    |----" + deep_4 + "... etc" + '\n'

    return tree
