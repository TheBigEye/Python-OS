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

    fs[""] = {
        "Data": {},
        "System": {},
        "Users": {
            username: {}
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

    if directory == "..":
        if len(current_dir) > 0:
            current_dir.pop()

    else:
        # check if the directory exists
        if directory not in current_dictionary():
            print_error("Directory " + directory + " does not exist")
            return

        else:
            current_dir.append(directory)

    print_info("Current directory: " + str("/" + "/".join(current_dir) ) )

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
    d[name_and_extension] = ""
    fs.sync()


def edit_file(name_and_extension, content):
    global fs

    # Check if the file exists
    if name_and_extension not in current_dictionary():
        print_error("File " + name_and_extension + " does not exist")
        return

    print_info("Editing file " + name_and_extension)
    d = current_dictionary()
    d[name_and_extension] = content
    fs.sync()


def get_file_content(name_and_extension):
    global fs

    # Check if the file exists
    if name_and_extension not in current_dictionary():
        print_error("File " + name_and_extension + " does not exist")
        return

    print_info("Getting content of file " + name_and_extension)
    d = current_dictionary()
    return d[name_and_extension]


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


    for i in directory:
        tree += "|--" + i + '\n'

        for j in directory[i]:
            tree += "|   |--" + j + '\n'

            for k in directory[i][j]:
                tree += "|   |   |--" + k + '\n'

                for l in directory[i][j][k]:
                    tree += "|   |   |   |--" + l + "..." + '\n'

    return tree

