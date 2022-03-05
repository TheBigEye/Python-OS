import datetime
import json
import os
import random
import shelve

from System.Utils.Utils import print_error, print_info, print_warning

fs = shelve.open('Disk/FS/Filesystem', writeback=True)
current_dir = []

def fs_routines():

    # laod boot data
    with open('Disk/Boot.json', 'r') as f:
        boot_data = json.load(f)

    def check_boot():
        if boot_data["FS_mounted"] != "False":
            return
        print_error("File system is not mounted")

        # delete the .dat, bak and dir files in  Disk/FS/
        if os.path.exists("Disk/FS/Filesystem.dat"): os.remove("Disk/FS/Filesystem.dat")
        if os.path.exists("Disk/FS/Filesystem.bak"): os.remove("Disk/FS/Filesystem.bak")
        if os.path.exists("Disk/FS/Filesystem.dir"): os.remove("Disk/FS/Filesystem.dir")

        fs = shelve.open('Disk/FS/Filesystem', writeback=True)
        install(fs)

        boot_data["FS_mounted"] = "True"

        with open("Disk/Boot.json", "w") as f:
            json.dump(boot_data, f, indent=4)

        print_info("File system installed")

    check_boot()
    print_info("File system ready!")

def install(fs):
    # create root and others
    username = "User"

    # default filesystem
    fs[""] = {
        "Home": {
            "Programs": {},
            username: {
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
    fs.sync()

def current_dictionary():
    """Return a dictionary representing the files in the current directory"""
    d = fs[""]
    for key in current_dir:
        d = d[key]
    return d

def ls():
    list_dir = ""

    list_dir += "Contents of directory " + str("/" + "/".join(current_dir) ) + '/:' + "\n"

    # show orderly alphabetically
    for key in sorted(current_dictionary()):
        list_dir += f"   {key}" + "\n"

    return list_dir

def cd(directory):

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

    return str(f"Directory {directory} does not exist")

def mkdir(name):

    global fs

    # Check if the directory already exists in the current directory
    if name in current_dictionary():
        return str(
            f"Directory {name} already exists in "
            + str("/" + "/".join(current_dir))
        )


    # create an empty directory there and sync back to shelve dictionary!
    d = current_dictionary()[name] = {}
    fs.sync()

    return str(f"Directory {name} created in " + str("/" + "/".join(current_dir) ))

def mkfile(argument):
    global fs

    # Get the name and extension
    name = argument.split(".")[0]
    extension = argument.split(".")[1]

    name_and_extension = f'{name}.{extension}'

    # Check if the file already exists in the current directory
    if name_and_extension in current_dictionary():
        print_warning(f"File {name}.{extension} already exists, overwriting")

        # add a random number to the name
        name = f'{name}-{str(random.randint(0, 512) + random.randint(0, 512))}'
        name_and_extension = f'{name}.{extension}'

        # create the file
        directory = current_dictionary()
        directory[name_and_extension] = ""
        return

    print_info(
        f"Created file {name_and_extension} in "
        + str("/" + "/".join(current_dir))
    )

    d = current_dictionary()
    d[name_and_extension] = {
            "Metadata": {
                "Extension": extension,
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
        return str(f"File {name_and_extension} does not exist")

    d = current_dictionary()
    d[name_and_extension] = {
            "Metadata": {
                "Extension": d[name_and_extension]["Metadata"]["Extension"],
                "Created": d[name_and_extension]["Metadata"]["Created"],
                "Modified": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            },
            "Data": content
        }

    fs.sync()

    return str(f"File {name_and_extension} edited")


def get_file_content(name_and_extension):
    global fs

    # Check if the file exists
    if name_and_extension not in current_dictionary():
        print_error(f"File {name_and_extension} does not exist")
        return

    print_info(f"Getting content of file {name_and_extension}")
    d = current_dictionary()
    return d[name_and_extension]["Data"]


def get_file_metadata(name_and_extension):
    global fs

    meta = ""

    # Check if the file exists
    if name_and_extension not in current_dictionary():
        print_error(f"File {name_and_extension} does not exist")
        return

    print_info(f"Getting metadata of file {name_and_extension}")
    d = current_dictionary()
    meta += f"File: {name_and_extension}" + "\n"
    meta += "Created: " + d[name_and_extension]["Metadata"]["Created"] + "\n"
    meta += "Modified: " + d[name_and_extension]["Metadata"]["Modified"] + "\n"
    return meta


def rmdir(name):
    global fs

    # Check if the directory exists
    if name not in current_dictionary():
        return str(f"Directory {name} does not exist")

    d = current_dictionary()
    del d[name]
    fs.sync()

    return str(f"Directory {name} deleted")


def rmfile(name_and_extension):
    global fs

    # Check if the file exists
    if name_and_extension not in current_dictionary():
        print_error(f"File {name_and_extension} does not exist")
        return

    print_info(f"Deleting file {name_and_extension}")
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

    for deep_1 in sorted(directory):
        if "." in deep_1:
            continue
        tree += f"|----{deep_1}" + '\n'

        for deep_2 in sorted(directory[deep_1]):
            if "." in deep_2:
                continue
            tree += f"|    |----{deep_2}" + '\n'

            for deep_3 in sorted(directory[deep_1][deep_2]):
                if "." in deep_3:
                    continue
                tree += f"|    |    |----{deep_3}" + '\n'

                for deep_4 in sorted(directory[deep_1][deep_2][deep_3]):
                    if "." in deep_4:
                        continue
                    tree += f"|    |    |    |----{deep_4}... etc" + '\n'

    return tree
