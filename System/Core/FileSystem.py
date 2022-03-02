import datetime
import random
import shelve
from System.Core.KeysSystem import add_key, get_value

from System.Utils.Utils import print_error, print_info, print_warning

fs = shelve.open('Disk/FS/Filesystem', writeback=True)
current_dir = []

def fs_routines():

    # Check the registry if the filesystem is installed
    if get_value("PYTHON-OS", "System", "FS", "Created") == "False":
        install(fs)
        add_key("PYTHON-OS", "System", "FS", "Created", "True", "str")
        print_info("File system mounted")

    print_info("File System loaded")


def install(fs):
    # create root and others
    username = "User"

    # default filesystem
    fs[""] = {
        "bin": {},
        "etc": {},
        "home": {
            username: {
                "Desktop": {},
                "Documents": {},
                "Music": {}
            }
        },
        "opt": {},
        "tmp": {},
        "usr": {
            "bin": {},
            "lib": {}
        },
        "var": {
            "log": {}
        }
    }

def current_dictionary():
    """Return a dictionary representing the files in the current directory"""
    d = fs[""]
    for key in current_dir:
        d = d[key]
    return d

def ls():
    list_dir = ""

    list_dir += "Contents of directory " + str("/" + "/".join(current_dir) ) + '/:' + "\n"

    for i in current_dictionary():
        list_dir += "   " + i + '\n'

    return list_dir

def cd(directory):

    # if the directory contains a dot and extension like .txt, cannot cd into it
    if "." in directory:
        if directory.split(".")[1] != "":
            print_warning("Cannot cd into file")
            return

    global current_dir

    # if the directory is .., go to the parent directory
    if directory == "..":
        if len(current_dir) > 0:
            current_dir.pop()
        return

    # if the directory is a subdirectory, go to the subdirectory
    if directory in current_dictionary():
        current_dir.append(directory)
        return

    print_error("Directory " + directory + " does not exist")

def mkdir(name):

    global fs

    # Check if the directory already exists in the current directory
    if name in current_dictionary():
        print_error("Directory " + name +" already exists in " + str("/" + "/".join(current_dir) ) )
        return

    print_info("Creating directory: " + name)
    # create an empty directory there and sync back to shelve dictionary!
    d = current_dictionary()[name] = {}
    fs.sync()

def mkfile(argument):
    global fs

    # Get the name and extension
    name = argument.split(".")[0]
    extension = argument.split(".")[1]

    name_and_extension = name + "." + extension

    # Check if the file already exists in the current directory
    if name_and_extension in current_dictionary():
        print_warning("File " + name + "." + extension + " already exists, overwriting")

        # add a random number to the name
        name = name + "-" + str(random.randint(0, 512) + random.randint(0, 512)) # imposible to have a file with the same name :)
        name_and_extension = name + "." + extension

        # create the file
        directory = current_dictionary()
        directory[name_and_extension] = ""
        return

    print_info("Created file " + name_and_extension + " in " + str("/" + "/".join(current_dir) ) )
    d = current_dictionary()
    d[name_and_extension] = {
            "Metadata": {
                "Created": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Modified": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            },
            "Data": ""
        }
    fs.sync()


def edit_file(name_and_extension, content):
    global fs

    # Check if the file exists
    if name_and_extension not in current_dictionary():
        print_error("File " + name_and_extension + " does not exist")
        return

    print_info("Editing file " + name_and_extension)
    d = current_dictionary()
    d[name_and_extension] = {
            "Metadata": {
                "Created": d[name_and_extension]["Metadata"]["Created"],
                "Modified": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            },
            "Data": content
        }

    fs.sync()


def get_file_content(name_and_extension):
    global fs

    # Check if the file exists
    if name_and_extension not in current_dictionary():
        print_error("File " + name_and_extension + " does not exist")
        return

    print_info("Getting content of file " + name_and_extension)
    d = current_dictionary()
    return d[name_and_extension]["Data"]


def get_file_metadata(name_and_extension):
    global fs

    meta = ""

    # Check if the file exists
    if name_and_extension not in current_dictionary():
        print_error("File " + name_and_extension + " does not exist")
        return

    print_info("Getting metadata of file " + name_and_extension)
    d = current_dictionary()
    meta += "File: " + name_and_extension + "\n"
    meta += "Created: " + d[name_and_extension]["Metadata"]["Created"] + "\n"
    meta += "Modified: " + d[name_and_extension]["Metadata"]["Modified"] + "\n"
    return meta


def rmdir(name):
    global fs

    # Check if the directory exists
    if name not in current_dictionary():
        print_error("Directory " + name + " does not exist")
        return

    print_info("Deleting directory " + name)
    d = current_dictionary()
    del d[name]
    fs.sync()


def rmfile(name_and_extension):
    global fs

    # Check if the file exists
    if name_and_extension not in current_dictionary():
        print_error("File " + name_and_extension + " does not exist")
        return

    print_info("Deleting file " + name_and_extension)
    d = current_dictionary()
    del d[name_and_extension]
    fs.sync()


def tree(*args):
    global fs

    tree = ""

    # if no argument is given, print the whole tree
    if args[0] == "$null":

        directory = current_dictionary()
        tree += "Contents of directory " + str("/" + "/".join(current_dir) ) + '/:' + "\n"

    elif args[0] in current_dictionary():

        directory = current_dictionary()[args[0]]
        tree += "Contents of directory " + str("/" + "/".join(current_dir) ) + '/' + args[0] + '/:' + "\n"

    for deep_1 in directory:
        if "." in deep_1:
            continue
        tree += "|----" + deep_1 + '\n'

        for deep_2 in directory[deep_1]:
            if "." in deep_2:
                continue
            tree += "|    |----" + deep_2 + '\n'

            for deep_3 in directory[deep_1][deep_2]:
                if "." in deep_3:
                    continue
                tree += "|    |    |----" + deep_3 + '\n'

                for deep_4 in directory[deep_1][deep_2][deep_3]:
                    if "." in deep_4:
                        continue
                    tree += "|    |    |    |----" + deep_4 + "... etc" + '\n'

    return tree