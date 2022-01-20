import json

Kernel_lvl = 6  # Kernel main variable

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
        "FolderContent": [ 
            {
                "FileName": "Index",
                "FileExtension": "pfs",
                "FileContent": "..."
            }
        ]
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
    return FileSystem[FileName]["FileContent"]


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
    for folder in FileSystem:
        for file in folder["FolderContent"]:
            if file["FileName"] == FileName and file["FileExtension"] == FileExtension:
                file["FileName"] = NewFileName
                file["FileExtension"] = NewFileExtension

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
    # for
    for folder in FileSystem:
        for file in folder["FolderContent"]:
            if file["FileName"] != "Index" and file["FileExtension"] != "pfs":
                if file["FileName"] == FileName and file["FileExtension"] == FileExtension:
                    # Get the file content
                    FileContent = file["FileContent"]
                    folder["FolderContent"].remove(file)
        
                    # Get the folder number.
                    FolderNumber = 0
                    for folder in FileSystem:
                        if folder["FolderName"] == Folder:
                            break
                        FolderNumber += 1
                    
                    FileSystem[FolderNumber]["FolderContent"].append({
                        "FileName": FileName,
                        "FileExtension": FileExtension,
                        "FileContent": FileContent
                    })

    

    # save the file in FileSystem
    def save_file():
        with open("Disk/FileSystem.json", "w") as file:
            json.dump(FileSystem, file)
    
    save_file()


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
    return FileSystem[FileName]["FileContent"]


def Open_folder(FolderName):
    return FileSystem[FolderName]["FolderContent"]


def Save_FileSystem():
    with open("Disk/FileSystem.json", "w") as file:
        json.dump(FileSystem, file)


def Load_FileSystem():

    global FileSystem

    with open("Disk/FileSystem.json", "r") as file:
        FileSystem = json.load(file)


def Get_FileSystem():

    Load_FileSystem()

    FileSystem_string = ""

    for folder in FileSystem:
        for file in folder["FolderContent"]: 
            FileSystem_string += folder["FolderName"] + "/" + file["FileName"] + "." + file["FileExtension"] + " [" + file["FileContent"] + "] "+ "\n"

    return FileSystem_string


def Tree_FileSystem():

    Load_FileSystem()

    FileSystem_string = ""

    for folder in FileSystem:
        FileSystem_string += folder["FolderName"] + "\n"
        for file in folder["FolderContent"]: 
            FileSystem_string += "   " + file["FileName"] + "." + file["FileExtension"] + "\n"

    return FileSystem_string


def Tree_FileSystem_Advanced():
    FileSystem_string = ""

    for folder in FileSystem:
        FileSystem_string += folder["FolderName"] + ">──┐" + "\n"

        for file in folder["FolderContent"]: 
            if file["FileName"] == "Index" and file["FileExtension"] == "pfs":
                FileSystem_string += "     ├─ Index.pfs\n"
            elif file == folder["FolderContent"][-1]:
                FileSystem_string += "     └─ " + file["FileName"] + "." + file["FileExtension"] + "\n"
            else:
                FileSystem_string += "     ├─ " + file["FileName"] + "." + file["FileExtension"] + "\n"

    return FileSystem_string

def Format_FileSystem():
    global FileSystem

    FileSystem = []

    # save the file in FileSystem
    def save_file():
        with open("Disk/FileSystem.json", "w") as file:
            json.dump(FileSystem, file)
    
    save_file()

# Import_file, import a real file and its content to the file system, example: import_file(C:/Users/User/Desktop/file.txt, "txt", folder)
def Import_file(FilePath, Folder):
    # get the file content
    with open(FilePath, "r") as file:
        FileContent = file.read()

    # get the file name without the extension
    FileName = FilePath.split("/")[-1].split(".")[0]
    
    # get the file extension
    FileExtension = FilePath.split("/")[-1].split(".")[1]

    # get the folder number
    FolderNumber = 0
    for folder in FileSystem:
        if folder["FolderName"] == Folder:
            break
        FolderNumber += 1


    # add the file to the file system
    FileSystem[FolderNumber]["FolderContent"].append({
        "FileName": FileName,
        "FileExtension": FileExtension,
        "FileContent": FileContent
    })

    # save the file in FileSystem
    def save_file():
        with open("Disk/FileSystem.json", "w") as file:
            json.dump(FileSystem, file)
    
    save_file()

# Execute_file, if the file has the extension pys, it will execute the code that has as its content as python code.
def Execute_file(FileName, FileExtension):
    # get the file content
    for folder in FileSystem:
        for file in folder["FolderContent"]:
                if file["FileName"] == FileName and file["FileExtension"] == FileExtension:
                    # Get the file content
                    FileContent = file["FileContent"]

    # if the file has the extension pys, it will execute the code that has as its content as python code.
    if FileExtension == "pys":
        exec(FileContent)


