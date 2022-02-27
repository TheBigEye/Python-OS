import json
import time

from System.Utils.Utils import print_info

FileSystem = [] # Here the file system is temporarily saved and loaded

def fs_routines():
    load_filesystem()

    print_info("File System loaded")

# Extensions ----------------------------------------------------------------------------------------------------------------------------

Index_file_ext = "pfs"
Python_script_extension = "pys"

# File system functions ---------------------------------------------------------------------------------------------------------------------

FileSystem_directory = "Disk/System/Files.json"

def save_file():

    global FileSystem

    with open(FileSystem_directory, "w") as file:
        json.dump(FileSystem, file, indent=4)


def save_folder():

    global FileSystem

    with open(FileSystem_directory, "w") as folder:
        json.dump(FileSystem, folder, indent=4)


def save_filesystem():

    global FileSystem

    with open(FileSystem_directory, "w") as fs:
        json.dump(FileSystem, fs, indent=4)

def load_filesystem():

    global FileSystem

    with open(FileSystem_directory, "r") as fs:
        FileSystem = json.load(fs)


def create_drive(drive_letter):
    drive = {
        "drive": drive_letter + ":",
        "content": []
    }
    FileSystem.append(drive)
    save_filesystem()


def delete_drive(drive_letter):
    for drive in FileSystem:
        if drive["drive"] == drive_letter:
            FileSystem.remove(drive)
            save_filesystem()


def create_folder(path):
    load_filesystem()

    drive_letter = path.split("/")[0]
    folder_name = path.split("/")[1]

    for drive in FileSystem:
        if drive["drive"] == drive_letter:
            for folder in drive["content"]:
                if folder["name"] == folder_name:
                    print("Folder already exists")
                    return

            folder = {
                "type": "folder",
                "name": folder_name,
                "files": []
            }
            drive["content"].append(folder)
            save_filesystem()


def delete_folder(path):
    load_filesystem()

    drive_letter = path.split("/")[0]
    folder_name = path.split("/")[1]

    for drive in FileSystem:
        if drive["drive"] == drive_letter:
            for folder in drive["content"]:
                if folder["name"] == folder_name:
                    drive["content"].remove(folder)
                    save_filesystem()


def create_file(path):
    load_filesystem()

    drive_letter = path.split("/")[0]
    folder_name = path.split("/")[1]

    file_name = path.split("/")[2].split(".")[0]
    file_extension = path.split("/")[2].split(".")[1]


    for drive in FileSystem:
        if drive["drive"] == drive_letter:
            for folder in drive["content"]:
                if folder["name"] == folder_name:
                    for file in folder["files"]:
                        if file["name"] == file_name:
                            print("File already exists")
                            return

                    file = {
                        "type": "file",
                        "name": file_name,
                        "extension": file_extension,
                        "metadata": {
                            "size": "empty",
                            "date": time.strftime("%d/%m/%y"),
                            "time": time.strftime("%H:%M:%S")
                        },
                        "content": ""
                    }
                    folder["files"].append(file)
                    save_filesystem()


def delete_file(path):
    load_filesystem()

    drive_letter = path.split("/")[0]
    folder_name = path.split("/")[1]

    file_name = path.split("/")[2].split(".")[0]
    file_extension = path.split("/")[2].split(".")[1]

    for drive in FileSystem:
        if drive["drive"] == drive_letter:
            for folder in drive["content"]:
                if folder["name"] == folder_name:
                    for file in folder["files"]:
                        if file["name"] == file_name and file["extension"] == file_extension:
                            folder["files"].remove(file)
                            save_filesystem()


def edit_file(path, content):
    load_filesystem()

    drive_letter = path.split("/")[0]
    folder_name = path.split("/")[1]

    file_name = path.split("/")[2].split(".")[0]
    file_extension = path.split("/")[2].split(".")[1]

    # calculate size of content in bytes
    size = len(content)

    for drive in FileSystem:
        if drive["drive"] == drive_letter:
            for folder in drive["content"]:
                if folder["name"] == folder_name:
                    for file in folder["files"]:
                        if file["name"] == file_name and file["extension"] == file_extension:
                            file["content"] = content
                            file["metadata"]["size"] = size
                            file["metadata"]["date"] = time.strftime("%d/%m/%y")
                            file["metadata"]["time"] = time.strftime("%H:%M:%S")

    save_filesystem()


def dir():
    load_filesystem()

    dir_list = ""

    # dir scheme
    # C:/
    #       folder1/
    #              file1.ext    20/10/2019  10:00:00
    #              file2.ext    20/10/2019  10:00:00
    #
    #       folder2/
    #              file3.ext    20/10/2019  10:00:00

    for drive in FileSystem:
        dir_list += drive["drive"] + "/" + "\n"
        for folder in drive["content"]:
            dir_list += "    " + folder["name"] + "/\n"
            for file in folder["files"]:
                dir_list += "        " + file["name"] + "." + file["extension"] + "    " + file["metadata"]["date"] + "  " + file["metadata"]["time"] + "\n"

    return dir_list


def dir_tree():

    load_filesystem()

    tree_list = ""

    # tree scheme
    # C:
    # ├─── folder1
    # │    ├─── file1.ext
    # │    └─── file2.ext
    # |
    # └─── folder2
    #      └─── file3.ext

    for drive in FileSystem:
        tree_list += drive["drive"] + "\n"
        for folder in drive["content"]:

            if folder == drive["content"][-1]:
                tree_list += "└─── " + folder["name"] + "\n"

                for file in folder["files"]:

                    if file == folder["files"][-1]:
                        tree_list += "     └─── " + file["name"] + "." + file["extension"] + "\n"
                        tree_list += "        \n" # next folder separation
                    else:
                        tree_list += "     ├─── " + file["name"] + "." + file["extension"] + "\n"
            else:
                tree_list += "├─── " + folder["name"] + "\n"

                for file in folder["files"]:

                    if file == folder["files"][-1]:
                        tree_list += "│    └─── " + file["name"] + "." + file["extension"] + "\n"
                        tree_list += "│       \n" # next folder separation
                    else:
                        tree_list += "│    ├─── " + file["name"] + "." + file["extension"] + "\n"

    return tree_list


