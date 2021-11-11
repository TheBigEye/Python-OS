import json

Kernel_lvl = 5  # Kernel main variable

Is_FAIL =           False  # 0
Is_in_BIOS =        False  # 1
Is_in_INSTALLER =   False  # 2
Is_in_Boot =        False  # 3
Is_in_Login =       False  # 4
Is_in_Desktop =     False  # 5
Is_Boot =           False  # 6


# Boot order
match Kernel_lvl:
    case 0:
        Is_FAIL = True  # Fail message
    case 1:
        Is_in_BIOS = True  # BIOS Screen
    case 2:
        Is_in_INSTALLER = True  # OS Installer
    case 3:
        Is_in_Boot = True  # Bootloader
    case 4:
        Is_in_Login = True  # Login Screen
    case 5:
        Is_in_Desktop = True  # In the desktop
    case 6:
        Is_Boot = True  # Normal boot


# Define the Routines() method, inside there will be functions and things that will be executed when calling this method.
def routines():
    pass

FileSystem = []

# the .json will have this structure:
# [
#   {
#       "FolderName": "",
#       "FolderContent": [
#           {
#               "FileName": "",
#               "FileExtension": "",
#               "FileContent": ""
#           }
#       ]
#   }
# ]

def Create_folder(FolderName):
    
    FileSystem.append({
        "FolderName": FolderName,
        "FolderContent": []
    })

    # save the folder in FileSystem
    def save_folder():
        with open("Disk/FileSystem.json", "w") as file:
            json.dump(FileSystem, file)
    
    save_folder()


def Create_file(FileName, FileExtension, FileContent):

    # move the file to the ROOT folder
    FileSystem[0]["FolderContent"].append({
        "FileName": FileName,
        "FileExtension": FileExtension,
        "FileContent": FileContent
    })

    # save the file in FileSystem
    def save_file():
        with open("Disk/FileSystem.json", "w") as file:
            json.dump(FileSystem, file)
    
    save_file()


def Read_file(FileName, FileExtension):
    # get the file content
    FileContent = FileSystem[FileName]["FileContent"]

    return FileContent


def Delete_file(FileName, FileExtension):
    for folder in FileSystem:
        for file in folder["FolderContent"]:
            if file["FileName"] == FileName and file["FileExtension"] == FileExtension:
                folder["FolderContent"].remove(file)

    # save the file in FileSystem
    def save_file():
        with open("Disk/FileSystem.json", "w") as file:
            json.dump(FileSystem, file)
    
    save_file()


def Delete_folder(FolderName):
    FileSystem.remove(FolderName)

    # save the folder in FileSystem
    def save_folder():
        with open("Disk/FileSystem.json", "w") as file:
            json.dump(FileSystem, file)
    
    save_folder()


def Rename_file(FileName, FileExtension, NewFileName, NewFileExtension):
    FileSystem[FileName]["FileName"] = NewFileName
    FileSystem[FileName]["FileExtension"] = NewFileExtension

    # save the file in FileSystem
    def save_file():
        with open("Disk/FileSystem.json", "w") as file:
            json.dump(FileSystem, file)
    
    save_file()


def Rename_folder(FolderName, NewFolderName):
    FileSystem[FolderName]["FolderName"] = NewFolderName

    # save the folder in FileSystem
    def save_folder():
        with open("Disk/FileSystem.json", "w") as file:
            json.dump(FileSystem, file)
    
    save_folder()


def Move_file(FileName, FileExtension, Folder):
    FileSystem[Folder]["FolderContent"].append(FileName)

    # save the file in FileSystem
    def save_file():
        with open("Disk/FileSystem.json", "w") as file:
            json.dump(FileSystem, file)
    
    save_file()


def Move_folder(FolderName, NewFolderName):
    FileSystem[FolderName]["FolderName"] = NewFolderName

    # save the folder in FileSystem
    def save_folder():
        with open("Disk/FileSystem.json", "w") as file:
            json.dump(FileSystem, file)
    
    save_folder()


def Copy_file(FileName, FileExtension, Folder):
    FileSystem[Folder]["FolderContent"].append(FileName)

    # save the file in FileSystem
    def save_file():
        with open("Disk/FileSystem.json", "w") as file:
            json.dump(FileSystem, file)
    
    save_file()


def Copy_folder(FolderName, NewFolderName):
    FileSystem[NewFolderName]["FolderContent"].append(FolderName)

    # save the folder in FileSystem
    def save_folder():
        with open("Disk/FileSystem.json", "w") as file:
            json.dump(FileSystem, file)
    
    save_folder()


def Open_file( FileName, FileExtension):
    # get the file content
    FileContent = FileSystem[FileName]["FileContent"]

    return FileContent


def Open_folder(FolderName):
    # get the folder content
    FolderContent = FileSystem[FolderName]["FolderContent"]

    return FolderContent


def Save_FileSystem():
    with open("Disk/FileSystem.json", "w") as file:
        json.dump(FileSystem, file)


def Load_FileSystem():

    global FileSystem

    with open("Disk/FileSystem.json", "r") as file:
        FileSystem = json.load(file)

# get the filesystem content as string, like: Filename.extension | file content | file extension
def Get_FileSystem():
    FileSystem_string = ""

    for folder in FileSystem:
        for file in folder["FolderContent"]: 
            FileSystem_string += folder["FolderName"] + "/" + file["FileName"] + "." + file["FileExtension"] + " ( " + file["FileContent"] + " ) "+ "\n"

    return FileSystem_string
